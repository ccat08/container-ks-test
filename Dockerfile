FROM python:3.11-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
RUN useradd app
RUN mkdir -p /usr/src/app/instance && chown app:app /usr/src/app/instance
USER app
CMD ["python", "src/app.py"]
