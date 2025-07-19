
# 📦 Python Excel Export Service

A lightweight, containerized microservice to generate Excel `.xlsx` files from JSON data and upload them to **ArvanCloud S3-compatible object storage**.

This service is designed to be triggered by a Laravel backend via HTTP and returns a public download URL for the Excel file.

---

## 🚀 Features

- Accepts structured JSON payload with column headers and rows.
- Generates `.xlsx` file using `pandas` and `openpyxl`.
- Uploads to ArvanCloud S3-compatible storage.
- Returns a public download URL immediately.
- Optionally sends a webhook back to Laravel.

---

## 📡 API Endpoint

### `POST /api/export`

**Request Body:**

```json
{
  "job_id": "export-12345",
  "columns": ["Name", "Email", "Joined"],
  "data": [
    ["Alice", "alice@example.com", "2023-01-01"],
    ["Bob", "bob@example.com", "2023-01-02"]
  ],
  "webhook_url": "https://your-laravel-app.com/api/webhooks/export-complete"
}
```

**Response:**

```json
{
  "status": "success",
  "url": "https://cdn.example.com/bucket/exports/export-12345.xlsx"
}
```

---

## 🛠 Configuration

Create a `.env` file in the root directory:

```env
ARVAN_ACCESS_KEY=your-access-key
ARVAN_SECRET_KEY=your-secret-key
ARVAN_ENDPOINT=https://s3.ir-thr-at1.arvanstorage.ir
ARVAN_BUCKET=your-bucket-name
ARVAN_PUBLIC_URL=https://your-cdn-link.ir-thr-at1.arvanstorage.ir/your-bucket-name
```

---

## 🐳 Docker

### Build Image

```bash
docker build -t excel-export-service .
```

### Run Container

```bash
docker run -d -p 8000:8000 --env-file .env --name excel-export excel-export-service
```

---

## 🧩 Project Structure

```
excel-export-service/
├── app/
│   ├── main.py
│   ├── exporter.py
│   └── requirements.txt
├── Dockerfile
└── .env
```

---

## ⚙️ Dependencies

- FastAPI
- Pandas
- OpenPyXL
- Boto3
- Uvicorn
- Requests

Install manually via:

```bash
pip install -r app/requirements.txt
```

---

## 🧪 Test with CURL

```bash
curl -X POST http://localhost:8000/api/export \
  -H "Content-Type: application/json" \
  -d @export_payload.json
```

---

## 📬 License

MIT – Use and modify freely.
