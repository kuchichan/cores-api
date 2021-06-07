FROM python:3.8 as build-python

ADD requirements.txt /
ADD rocket-cores /rocket-cores
RUN pip install --upgrade pip && pip install -r requirements.txt

FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

COPY --from=build-python /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/

ADD cores_app /code/cores_app
ADD load_cores.py /code/
ADD cores_app /code/

WORKDIR /code/
EXPOSE 80

CMD ["uvicorn" "cores_app.main:app", "--host=0.0.0.0", "--port=80"]
