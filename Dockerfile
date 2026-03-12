FROM python:3.14

WORKDIR /app

COPY ./requirements/prod.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]