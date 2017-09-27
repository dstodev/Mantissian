# Main
FROM python:latest
MAINTAINER Daniel Stotts
RUN apt-get update

ENV PROJECT /opt/project
WORKDIR ${PROJECT}

# Install necessary packages

# Install necessary Python modules
RUN pip install sanic
RUN pip install jinja2

# Install other things

# Add project files
ADD . ${PROJECT}
ENTRYPOINT ["python", "main.py"]

EXPOSE 80 443
