from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/calculate")
def get_grade(request: Request) -> dict:
    ...