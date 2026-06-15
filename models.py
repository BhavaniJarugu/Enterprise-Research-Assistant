from dataclasses import dataclass

@dataclass
class ResearchQuery:
    query:str

@dataclass
class ResearchResult:
    answer:str

@dataclass
class Source:
    name:str
    content:str
