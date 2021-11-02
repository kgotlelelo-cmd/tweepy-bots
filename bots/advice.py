import requests
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweetAdvice(api):
    #link should be stored in enviromental variables
    response = requests.get("https://api.adviceslip.com/advice").json()
    text = list(response.values())[0].get("advice")
    hashtag = "  #adviceBot"
    tweet = text + hashtag
    api.update_status(tweet)
    logger.info("tweet of the day: "+tweet)