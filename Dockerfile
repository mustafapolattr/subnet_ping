FROM python:3.12-slim

LABEL maintainer="Mustafa Polat"

COPY requirements.txt /tmp/requirements.txt
COPY . /opt/app-root/src/

WORKDIR /opt/app-root/src/

RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8004

CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]