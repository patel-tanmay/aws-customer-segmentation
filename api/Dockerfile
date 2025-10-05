# ==============================
# 1️⃣ Base image
# ==============================
FROM python:3.11-slim

# ==============================
# 2️⃣ Set working directory
# ==============================
WORKDIR /app

# ==============================
# 3️⃣ Copy requirements
# ==============================
COPY requirements.txt .
COPY api/requirements.txt ./api_requirements.txt

# ==============================
# 4️⃣ Install dependencies
# ==============================
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r api_requirements.txt

# ==============================
# 5️⃣ Copy application files
# ==============================
COPY api ./api
COPY models ./models

# ==============================
# 6️⃣ Expose port and start API
# ==============================
EXPOSE 8080
CMD ["uvicorn", "api.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
