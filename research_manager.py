from agents import Runner, trace, gen_trace_id
from search_agent import search_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from writer_agent import writer_agent, ReportData
from email_agent import email_agent
import asyncio


class ResearchManager:

    async def run(self, query: str):
        """ Run the deep seatch process, yeild the status updates and final report """
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/{trace_id}")
            yield f"View trace: https://platform.openai.com/traces/{trace_id}"

            print("Starting research...")
            search_plan = await self.plan_searches(query)
            yield "Searches planned, beginning search..."

            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, writing report..."

            report = await self.write_report(query, search_results)
            yield "Report completed, sending email..."

            await self.send_email(report)
            yield "Email sent, research topic complete"
            yield report.markdown_report

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """ Plan the searches to perform for the query """
        print("Planning searches...")
        result = await Runner.run(planner_agent, f"Query: {query}")

        print(f"Will perform {len(result.final_output.searches)} searches")
        return result.final_output_as(WebSearchPlan)
    
    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        """ Perform the searches for the given query """
        print("Searching...")
        num_completed = 0
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]

        results = []

        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
            num_completed += 1
            print(f"Searching... {num_completed}/{len(tasks)} completed")

        print(f"Finished searching")
        return results
    
    async def search(self, item: WebSearchItem) -> str | None:
        """ Perform a search for the query """
        input = f"Search term: {item.query}\nReason for searching: {item.reason}"
        try:
            result = await Runner.run(search_agent, input)
            return str(result.final_output)
        except Exception as e:
            return None
        
    async def write_report(self, query: str, search_results: list[str]) -> ReportData:
        """ Write the report for the query """
        print("Analyzing report output...")
        input = f"Original query: {query}\nSummarized search results: {search_results}"
        result = await Runner.run(writer_agent, input)

        print("Finished writing report")
        return result.final_output_as(ReportData)
    
    async def send_email(self, report: ReportData) -> None:
        print("Drafting email...")
        result = await Runner.run(email_agent, report.markdown_report)

        print("Email sent")
        return report