import tweepy
import logging
from config import create_api
from datetime import datetime,timedelta
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def isValid(tweetDate):
    deadline = datetime.now().replace(tzinfo=None) - timedelta(days = 5)
    if tweetDate.replace(tzinfo=None) < deadline:
        return True
    return False

def deleteTweets(api):
    for status in tweepy.Cursor(api.user_timeline).items(500):
        if isValid(status.created_at):
            api.destroy_status(status.id)
            logger.info("status deleted with id {id}".format(id=status.id))

def main():
    api = create_api()

    while True:
        try:
            deleteTweets(api)
        except tweepy.TweepyException:
            time.sleep(86400)
            logger.info("Sleeping for 24hours")
            continue
        except StopIteration:
            break


if __name__ == "__main__":
    main()