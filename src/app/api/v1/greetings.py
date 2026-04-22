from enum import Enum

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["greetings"])


class Language(str, Enum):
    PT = "pt"
    EN = "en"
    ES = "es"
    IT = "it"


@router.get("/hello/{name}")
def greetings(name: str, lang: Language = Language.PT):
    if lang == Language.EN:
        return {"message": f"Hello, {name}!"}
    elif lang == Language.ES:
        return {"message": f"¡Hola, {name}!"}
    elif lang == Language.IT:
        return {"message": f"Ciao, {name}!"}
    return {"message": f"Olá, {name}!"}
