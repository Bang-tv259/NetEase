FROM python:3.12-slim

WORKDIR /app

COPY README.md ./
COPY uv.lock ./
COPY .env ./
COPY src/ ./src
COPY pyproject.toml ./

RUN apt-get update && apt-get install -y curl bash && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH" && \
    uv --version

ENV PATH="/root/.local/bin:$PATH"

RUN uv sync --python /usr/local/bin/python3.12

EXPOSE 8888

CMD ["uv", "run", "python3","src/cat/api/main.py"]