FROM python:3.11

WORKDIR /heart-disease-api

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

ENV PATH="/etc/poetry/bin:$PATH"

COPY ../poetry.lock /heart-disease-api/
COPY ../pyproject.toml /heart-disease-api/
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-ansi 
COPY .. .

# EXPOSE 8000

CMD ["uvicorn", "ml_deployment.heartdiseaseapp:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["sleep", "infinity"]