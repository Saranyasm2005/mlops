FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "predict.py"]