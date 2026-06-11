#Stage 1 -- Builder
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrage pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

#Stage 2 -- runtime
FROM python:3.12-slim AS runtime

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

CMD ["python", "worker.py"]
