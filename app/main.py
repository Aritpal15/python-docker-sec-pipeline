from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(
    title="Secure Data Pipeline API",
    version="1.0.0"
)


class DataPayload(BaseModel):
    key: str
    value: Any


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check() -> Dict[str, str]:
    return {"status": "healthy", "service": "data-processor"}


@app.post("/process", status_code=status.HTTP_200_OK)
def process_data(payload: DataPayload) -> Dict[str, Any]:
    if not payload.key.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Key cannot be empty"
        )

    processed_value = str(payload.value).upper()
    return {
        "processed": True,
        "input_key": payload.key,
        "result": processed_value
    }
