FROM python:3.13-slim AS builder

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

FROM python:3.13-slim AS runner

WORKDIR /app

COPY --from=builder /install /usr/local

COPY src ./src
RUN chmod +x src/start.sh

EXPOSE 8000

ENV PYTHONPATH=./src

ENTRYPOINT ["src/start.sh"]
