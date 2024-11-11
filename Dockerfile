FROM artifactory.laforge.cloud.bpifrance.fr/docker-io/python:3.12.6-slim-bookworm

ENV HOME=/python-docker

ENV PYTHONPATH='/python-docker'

WORKDIR /python-docker

# Install Pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock from your host to the container
COPY Pipfile Pipfile.lock ./

# Install project dependencies
RUN pipenv install --deploy --ignore-pipfile --python $(which python)

# Copy the content of the local src directory to the working directory in the container
COPY . ./

# Change permissions
RUN chmod -R 777 /python-docker

ENTRYPOINT ["pipenv", "run", "python", "-m","techcareback.main"]
