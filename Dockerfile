#base image
FROM python:3.12.3

#set a directory for the app
WORKDIR /myapp

#copy all files to container
COPY . .

#install dependencies
RUN pip install --no-cache-dir -r Requirements.txt

EXPOSE 5000

#run the command
CMD ["python", "./PCA.py"]
