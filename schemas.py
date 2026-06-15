from pydantic import BaseModel

class ResearchRequest(BaseModel):
    query:str

class ResearchResponse(BaseModel):
    answer:str

class SourceResponse(BaseModel):
    sources:list[str]

class SummaryResponse(BaseModel):
    summary:str
