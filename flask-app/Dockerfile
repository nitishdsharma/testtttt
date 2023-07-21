# This Dockerfile creates a distroless image which can be used in any environment.

From python:3.8
WORKDIR /app
COPY ./* ./
RUN pip install -r requirements.txt
EXPOSE 5002
CMD ["python", "flaskapp.py"]
