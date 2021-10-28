# tweepy-bots

## requirements
Python3 and pip or pip3

Docker && Docker-compose are optional

## Running Locally
python3 -m venv venv

source ./venv/bin/activate

pip3 install tweepy

pip3 freeze > requirements.txt

export CONSUMER_KEY=""

export CONSUMER_SECRET=""

export ACCESS_TOKEN=""

export ACCESS_TOKEN_SECRET=""


## Running via docker
add .env.dev file in env folder and place ur twitter credentials and name of the host and image to used int the docker compose

docker-compose --env-file ./env/.env.dev up --build

docker-compose --env-file ./env/.env.dev up -d //if didn't run the previous command
