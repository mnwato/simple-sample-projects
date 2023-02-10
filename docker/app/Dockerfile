FROM python:3.11.1-slim-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install --upgrade -r requirements.txt

COPY ./ /code/app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
CMD ["python3", "app/main.py"]