FROM python:latest 

WORKDIR /app

COPY requirements.txt .
RUN pip install --noc-cache-dir -r requirements.txt

RUN pip install pytest

COPY . .

CMD ["pytest"]

CMD ["python", "pysnake.py"]
