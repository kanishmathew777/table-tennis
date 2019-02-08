FROM python:3.7

COPY requirements.txt /backend/requirements.txt

WORKDIR /backend

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY start.sh /backend/start.sh

COPY . /backend

RUN python manage.py migrate

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["/backend/start.sh"]
