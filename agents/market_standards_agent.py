from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re

class MarketStandardsAgent:
    def generate_use_cases(self, industry_info, key_offerings):
        industry = industry_info.split()[0]  # crude industry name extraction
        query = f"AI and GenAI use cases in {industry} industry"
        
        # Perform Google Search
        result_links = list(search(query, num_results=5))
        
        use_cases = []
        
        for link in result_links:
            try:
                page = requests.get(link, timeout=5)
                soup = BeautifulSoup(page.text, "html.parser")
                paragraphs = soup.find_all('p')
                
                for para in paragraphs[:5]:
                    text = para.get_text().strip()
                    if len(text) > 30:
                        # Break paragraph into sentences
                        sentences = re.split(r'[.!?]', text)
                        for sentence in sentences:
                            sentence = sentence.strip()
                            if 20 < len(sentence) < 180:  # reasonable sentence length
                                if any(keyword in sentence.lower() for keyword in ['ai', 'genai', 'machine learning', 'automation', 'llm']):
                                    use_cases.append(sentence)
            except Exception as e:
                print(f"Error fetching {link}: {e}")
        
        # Deduplicate and clean
        use_cases = list(set(use_cases))
        
        if not use_cases:
            # Fallback examples
            use_cases = [
                f"AI-driven process automation in {industry} sector",
                f"Customer sentiment analysis using GenAI in {industry}",
                f"Predictive maintenance using ML for {industry} equipment",
                f"Chatbots and Virtual Assistants powered by LLMs for {industry}",
                f"Automated Report Generation using GenAI for {industry} analytics"
            ]

        # Attach references
        use_cases.append(f"Refer to sources: {', '.join(result_links)}")
        
        return use_cases
