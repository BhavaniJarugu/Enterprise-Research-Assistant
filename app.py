from fastapi import FastAPI
from schemas import ResearchRequest
from research_service import ResearchService

app = FastAPI(title='Enterprise Research Assistant')
service = ResearchService()

@app.get('/health')
def health():
    return {'status':'healthy'}

@app.post('/research')
def research(req: ResearchRequest):
    return service.research(req.query)
