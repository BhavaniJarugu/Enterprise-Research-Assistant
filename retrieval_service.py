class RetrievalService:

    def __init__(self):
        self.sources = [
            'Enterprise Knowledge Base',
            'Research Repository',
            'Policy Documents'
        ]

    def retrieve(self, query):
        return self.sources

    def rank(self, documents):
        return documents[:5]
