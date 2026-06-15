class ReasoningService:

    def generate(self, query, docs):
        return f'Research answer generated for {query}'

    def summarize(self, text):
        return text[:300]

    def evaluate(self, answer):
        return {'score': 90}
