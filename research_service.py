from retrieval_service import RetrievalService
from reasoning_service import ReasoningService

class ResearchService:

    def __init__(self):
        self.retrieval = RetrievalService()
        self.reasoning = ReasoningService()

    def research(self, query):
        docs = self.retrieval.retrieve(query)
        answer = self.reasoning.generate(query, docs)
        return {'answer': answer, 'sources': docs}
