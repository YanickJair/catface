FROM python:{{ cookiecutter.python_version }}-slim AS base

ENV PYTHONUNBUFFERED True
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /root/
COPY . .

RUN apt-get update && apt-get install build-essential -y

RUN pip install --upgrade pip setuptools wheel

COPY pip.conf /etc/pip.conf

RUN pip install -r requirements.txt

CMD ["python", "-m", "{{ cookiecutter.project_slug }}"]
