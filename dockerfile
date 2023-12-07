FROM python:3.8
WORKDIR /app
COPY call_api.py .
COPY env.yml .
COPY requirments.txt .
RUN apt-get update
ADD main.py .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirments.txt 


EXPOSE 3306

CMD ["python", "main.py"]