FROM python:3-buster

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

WORKDIR /app
COPY facke_data_server facke_data_server

ENV PYTHONPATH="/app:$PYTHONPATH"

CMD ["python", "-m", "facke_data_server"]
