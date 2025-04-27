from agents.research_agent import ResearchAgent
from agents.market_standards_agent import MarketStandardsAgent
from agents.resource_collector_agent import ResourceCollectorAgent
from agents.bonus_genai_agent import BonusGenAIAgent

def main():
    # Input from user
    company_name = input("Enter the company or industry name: ")

    # Initialize agents
    researcher = ResearchAgent()
    market_agent = MarketStandardsAgent()
    resource_collector = ResourceCollectorAgent()
    bonus_agent = BonusGenAIAgent()

    # Step 1: Research the Company/Industry
    industry_info, key_offerings = researcher.research_company(company_name)

    # Step 2: Generate Market Standards and Use Cases
    use_cases = market_agent.generate_use_cases(industry_info, key_offerings)

    # Step 3: Collect Resources for Use Cases
    datasets = resource_collector.collect_resources(use_cases)

    # Step 4: Bonus GenAI Solutions
    bonus_solutions = bonus_agent.propose_bonus_solutions(company_name)

    # Step 5: Output results
    print("\n\n=== Final Report ===")
    print(f"Company/Industry: {company_name}")
    print(f"\nIndustry Info: {industry_info}")
    print(f"\nKey Offerings: {key_offerings}")
    print("\nUse Cases:")
    for i, case in enumerate(use_cases, 1):
        print(f"{i}. {case}")

    print("\nDatasets and Resources:")
    for link in datasets:
        print(f"- {link}")

    print("\nBonus GenAI Suggestions:")
    for suggestion in bonus_solutions:
        print(f"- {suggestion}")

    # Save outputs
    with open("instaresz-assignment/final_report.md", "w") as f:
        f.write(f"# Final Report for {company_name}\n\n")
        f.write(f"## Industry Info:\n{industry_info}\n\n")
        f.write(f"## Key Offerings:\n{key_offerings}\n\n")
        f.write("## Use Cases:\n")
        for case in use_cases:
            f.write(f"- {case}\n")
        f.write("\n## Bonus GenAI Suggestions:\n")
        for suggestion in bonus_solutions:
            f.write(f"- {suggestion}\n")

    with open("instaresz-assignment/dataset_links.md", "w") as f:
        f.write("# Dataset Links\n\n")
        for link in datasets:
            f.write(f"- [{link}]({link})\n")

if __name__ == "__main__":
    main()
