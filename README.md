# FAQ-Agent

FAQ-Agent is an assistant for answering frequently asked questions built as a simple, extensible question-answering agent. It can be used to serve an FAQ over an API, run locally for interactive queries, or be extended to index your own documentation and knowledge sources.

> NOTE: This is a generic README scaffold I created because I couldn't retrieve the repository's existing README. Replace examples and placeholders below with the repo's actual commands, filenames, and configuration as needed.

## Features
- Ingest FAQ data from CSV/JSON or other document sources
- Create/search an embedding index for semantic retrieval
- Answer user questions using a language model with retrieved context
- REST API and CLI examples included
- Optional vector store support (FAISS, SQLite/pgvector, etc.)

## Getting started

### Requirements
- Python 3.8+ (or change to your project's runtime)
- (Optional) Docker
- An API key for your chosen LLM provider (e.g., OpenAI, Anthropic, etc.)

### Install (Python)
```bash
# create venv and activate
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows

# install dependencies (replace with actual file in repo)
pip install -r requirements.txt
```

### Configuration
Create a .env file (or export env vars) with the values below (adjust keys to match your implementation):
```env
OPENAI_API_KEY=sk-xxxxxx
MODEL=gpt-4o-mini
VECTOR_STORE=faiss
FAISS_INDEX_PATH=./data/faiss_index
DATA_DIR=./data
FLASK_PORT=8080
```

### Preparing FAQ data
Supported input formats:
- CSV with columns: question, answer
- JSON list of { "question": ..., "answer": ... }
- Plain text / Markdown documents (one doc per file)

Example CSV (data/faqs.csv):
```csv
question,answer
"What are the hours?","We are open 9am–5pm Monday–Friday."
"How do I reset my password?","Click 'Forgot password' on the login page and follow instructions."
```

Index the data (example command — replace with actual script name):
```bash
python scripts/index_faqs.py --input data/faqs.csv --index-path ./data/faiss_index
```

## Usage

### Run locally (CLI)
Basic interactive CLI:
```bash
python cli.py --index ./data/faiss_index
# then type questions interactively
```

### Run API (example with Flask/FastAPI)
Start the server:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port 8080
# OR for FastAPI: uvicorn app:app --reload --port 8080
```

Example curl to ask a question:
```bash
curl -X POST "http://localhost:8080/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I reset my password?"}'
```

Response:
```json
{
  "answer": "Click 'Forgot password' on the login page and follow instructions.",
  "source_context": [
    {
      "id": "faq-23",
      "text": "Click 'Forgot password' on the login page and follow instructions."
    }
  ]
}
```

## Development
- Run tests:
```bash
pytest
```
- Lint:
```bash
flake8 .
```
- Format:
```bash
black .
```

## Docker (optional)
Example Dockerfile snippet:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
```

Build and run:
```bash
docker build -t faq-agent .
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8080:8080 faq-agent
```

## Architecture (high level)
1. Data ingestion: convert source documents to plain text docs with metadata
2. Embedding: embed documents and store in vector store
3. Retrieval: given a query, retrieve top-K relevant docs
4. Generation: compose prompt with retrieved context and call LLM for final answer
5. API/CLI layer: serve user requests and return answers + provenance

## Contributing
Contributions are welcome. Typical workflow:
- Fork the repository
- Create a feature branch
- Add tests
- Open a pull request with a clear description

Please follow the repository's code style and add tests for new behavior.

## Troubleshooting
- If answers seem off: increase number of retrieved documents or improve prompt templates.
- If indexing fails: check input file format and encoding.
- For performance: consider using a persisted vector store backend and batching embeddings.

## License
Specify the appropriate license (e.g., MIT). Replace this line with the real license used in the repository.

## Contact
For questions about this project, open an issue on the repository or contact the maintainers.
