FROM python:3.8-alpine3.11

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "./app.py"]
