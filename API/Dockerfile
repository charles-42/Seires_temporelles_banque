FROM python:3.9

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV PYTHONUNBUFFERED 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


# charles42/time_series:
# docker tag ts_api:latest charles42/time_series:latest