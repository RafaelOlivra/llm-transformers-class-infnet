from pydantic import BaseModel


class AutoCompleteModel(BaseModel):
    phrase: str
