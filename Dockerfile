FROM python:3.9-slim-buster
RUN pip install --upgrade pip
WORKDIR /usr/src/app

COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt 

CMD ["python", ".SampleCode/run_workflow.py"]
