import requests
from googlesearch import search

class ResearchAgent:
    def research_company(self, company_name):
        query = f"{company_name} industry and key offerings"
        results = list(search(query, num_results=3))

        industry_info = f"Found industry information for {company_name}."
        key_offerings = []

        # Dummy Parsing (Later improve with BeautifulSoup if needed)
        for link in results:
            key_offerings.append(f"Refer to {link}")

        return industry_info, key_offerings
