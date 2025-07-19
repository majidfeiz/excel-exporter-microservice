from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.exporter import generate_and_upload_excel

app = FastAPI()

class ExportRequest(BaseModel):
    job_id: str
    columns: list[str]
    data: list[list]
    webhook_url: str

@app.post("/api/export")
async def export_excel(request: ExportRequest):
    result_url = generate_and_upload_excel(
        request.job_id,
        request.columns,
        request.data
    )

    # Send webhook back
    import requests
    requests.post(request.webhook_url, json={
        "job_id": request.job_id,
        "download_url": result_url
    })

    return {"status": "success", "url": result_url}
