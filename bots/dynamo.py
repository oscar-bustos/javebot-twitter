import boto3
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tweets')

logger = logging.getLogger()
logger.info("creation_date_time " + str(table.creation_date_time))


def save_tweet(tweet):
    print(f"{tweet.user.name}:{tweet.text}")

    try:
        table.put_item(
            Item={
                'id': tweet.id_str,
                'json': str(tweet._json),
            }
        )
    except Exception as e:
        logger.error("Error saving tweet", exc_info=True)
        raise e



