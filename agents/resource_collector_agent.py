from googlesearch import search

class ResourceCollectorAgent:
    def collect_resources(self, use_cases):
        datasets = []
        for case in use_cases:
            query = f"dataset for {case} Kaggle GitHub Huggingface"
            try:
                result = list(search(query, num_results=1))
                if result:
                    datasets.append(result[0])
            except Exception as e:
                print(f"Error fetching dataset for {case}: {str(e)}")
        return datasets
