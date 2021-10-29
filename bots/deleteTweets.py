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

    i = 0
    v = 0

    for status in tweepy.Cursor(api.user_timeline).items(1000):
        v = v + 1
        logger.info("{v}".format(v=v))
        if isValid(status.created_at):
            api.destroy_status(status.id)
            i = i + 1
            logger.info("status deleted with id : {id}".format(id=status.id))
            logger.info("Number of status deleted : {i}".format(i=i))
    
    logger.info("Total tweets deleted per 500: {i}".format(i=i))
    if i == 0:
        logger.info("Done for the day No tweets are older than 5 days in the 500 batch")
        raise tweepy.TweepyException

def main():
    api = create_api()

    while True:
        try:
            deleteTweets(api)
        except tweepy.TweepyException:
            logger.info("Sleeping for 24hours")
            time.sleep(86400)
            continue
        except StopIteration:
            break


if __name__ == "__main__":
    main()