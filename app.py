import streamlit as st
from agents.research_agent import ResearchAgent
from agents.market_standards_agent import MarketStandardsAgent
from agents.resource_collector_agent import ResourceCollectorAgent
from agents.bonus_genai_agent import BonusGenAIAgent

# Title
st.title("🧠 Multi-Agent AI Use Case Generator")
st.write("Upload a Company or Industry Name to Generate AI/GenAI Solutions")

# Input box
company_name = st.text_input("Enter Company or Industry Name:")

if st.button("Generate AI Solutions"):
    if company_name:
        # Initialize agents
        researcher = ResearchAgent()
        market_agent = MarketStandardsAgent()
        resource_collector = ResourceCollectorAgent()
        bonus_agent = BonusGenAIAgent()

        with st.spinner("Researching Industry and Company..."):
            industry_info, key_offerings = researcher.research_company(company_name)

        with st.spinner("Analyzing Market Standards and Generating Use Cases..."):
            use_cases = market_agent.generate_use_cases(industry_info, key_offerings)

        with st.spinner("Finding Resources and Datasets..."):
            datasets = resource_collector.collect_resources(use_cases)

        with st.spinner("Generating Bonus GenAI Solutions..."):
            bonus_solutions = bonus_agent.propose_bonus_solutions(company_name)

        # Output
        st.success("✅ Research and Use Case Generation Completed!")

        st.subheader("📄 Industry Info:")
        st.write(industry_info)

        st.subheader("🏢 Key Offerings:")
        for offering in key_offerings:
            st.write("- ", offering)

        st.subheader("🎯 Generated Use Cases:")
        for i, case in enumerate(use_cases, 1):
            st.write(f"{i}. {case}")

        st.subheader("📚 Datasets and Resources:")
        for link in datasets:
            st.markdown(f"- [{link}]({link})", unsafe_allow_html=True)

        st.subheader("💡 Bonus GenAI Solutions:")
        for suggestion in bonus_solutions:
            st.write(f"- {suggestion}")

    else:
        st.error("❗ Please enter a company or industry name.")

