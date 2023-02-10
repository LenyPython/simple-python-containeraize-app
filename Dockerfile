FROM  3.12-rc-alpine

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /src/ .

CMD ["uvicorn","main:app", "--reload"]
