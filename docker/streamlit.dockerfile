FROM python:3.12-slim


RUN apt-get update && apt-get install -y curl bash && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH"

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /streamlit
COPY .env /streamlit/
COPY uv.lock /streamlit/
COPY packages/dev_ui/README.md ./
COPY packages/dev_ui /streamlit/
# COPY packages/dev_ui/pyproject.toml ./


RUN uv sync

CMD [".venv/bin/streamlit", "run", "src/dev_ui/ui/Homepage.py", "--server.port=8501", "--server.address=0.0.0.0"]
