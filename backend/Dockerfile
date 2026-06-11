# Stage 1 - Builder
FROM python:3.12-slim AS Builder

WORKDIR /app

#Install dependencies into a prefix we can copy cleanly
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

#Stage 2 - Runtime
FROM python:3,12-slim AS runtime

WORKDIR /app

#Copy only installed packages from builder - no pip, no cache
COPY --from=builder /install /usr/local

#Copy application code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

