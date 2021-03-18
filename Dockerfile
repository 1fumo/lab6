FROM python:3.7-alpine 
WORKDIR /
COPY . / 
RUN  pip install -r requirements.txt
EXPOSE 80
CMD ["python", "myapp.py"]
