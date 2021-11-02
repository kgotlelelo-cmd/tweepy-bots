import tweepy
import logging
from config import create_api
from advice import tweetAdvice
from datetime import datetime,timedelta
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def isValid(tweetDate):
    deadline = datetime.now().replace(tzinfo=None) - timedelta(days = 3)
    if tweetDate.replace(tzinfo=None) < deadline:
        return True
    return False

def deleteTweets(api):

    i = 0
    v = 0

    for status in tweepy.Cursor(api.user_timeline).items(500):
        v = v + 1
        if isValid(status.created_at):
            api.destroy_status(status.id)
            i = i + 1
            logger.info("status deleted with id : {id}".format(id=status.id))
            logger.info("Number of status deleted : {i}".format(i=i))
    
    logger.info("Total tweets deleted per {v}: {i}".format(i=i,v=v))

    if i == 0:
        logger.info("Done for the day No tweets are older than 3 days in the timeline")
        raise tweepy.TweepyException

def main():
    api = create_api()

    while True:
        try:
            tweetAdvice(api)
            deleteTweets(api)
        except tweepy.TweepyException:
            logger.info("Sleeping for 24hours")
            time.sleep(86400)
            continue
        except StopIteration:
            break


if __name__ == "__main__":
    main()