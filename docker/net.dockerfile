FROM python:3.12-slim

WORKDIR /app

COPY README.md ./
COPY uv.lock ./
COPY .env ./
COPY src/ ./
COPY pyproject.toml ./

RUN apt-get update && apt-get install -y curl bash && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH"

ENV PATH="/root/.local/bin:$PATH"

RUN uv sync
# RUN uv sync --python /usr/local/bin/python3.12

EXPOSE 8888

CMD ["uv", "run", "uvicorn", "cat.api.main:app", "--host", "0.0.0.0", "--port", "8888"]