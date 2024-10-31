from fastapi import APIRouter
from ..models.chat import AutoCompleteModel
from transformers import pipeline

router = APIRouter()


def generate_response(message: str):
    generator = pipeline("text-generation", model="gpt2")
    return generator(message)


@router.post("/autocomplete/")
async def autocomplete(body: AutoCompleteModel):
    response = generate_response(body.phrase)
    return {"assistant": response[0]["generated_text"]}
