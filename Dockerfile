FROM  python:3.12-rc-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

ENTRYPOINT [ "python3" ]

CMD ["src/main.py"]
