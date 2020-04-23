FROM python:3
ADD flask_test.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 8787
CMD [ "python", "./flask_test.py"]
