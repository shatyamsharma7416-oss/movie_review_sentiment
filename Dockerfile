FROM python:3.12-slim
WORKDIR /user/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["streamlit", "run", "main.py", "--server.port", "10000", "--server.address", "0.0.0.0"]