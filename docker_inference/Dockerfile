# -------------------------------
# Step 1: Base Image
# -------------------------------
FROM python:3.9-slim

# -------------------------------
# Step 2: Set Environment Variables
# -------------------------------
ENV PYTHONUNBUFFERED=TRUE
ENV PORT=8080
ENV PATH="/opt/ml/code:${PATH}"

# -------------------------------
# Step 3: Install Dependencies
# -------------------------------
COPY requirements.txt /opt/ml/code/requirements.txt
RUN pip install --no-cache-dir -r /opt/ml/code/requirements.txt

# -------------------------------
# Step 4: Copy Model & Inference Code
# -------------------------------
COPY inference.py /opt/ml/code/inference.py
COPY models /opt/ml/model

# -------------------------------
# Step 5: Expose SageMaker Ports
# -------------------------------
EXPOSE 8080

# -------------------------------
# Step 6: Define Entrypoint
# -------------------------------
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "inference:app"]
