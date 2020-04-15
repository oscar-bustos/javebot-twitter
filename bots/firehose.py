import boto3
import logging
import json

firehose = boto3.client('firehose')
logger = logging.getLogger()


def save_tweet(tweet):
    print(f"{tweet.user.name}:{tweet.text}")

    try:

        response = firehose.put_record(
            DeliveryStreamName='twitter-stream',
            Record={
                'Data': json.dumps(tweet._json).replace("'", '"').encode()
            }
        )

    except Exception as e:
        logger.error("Error saving tweet", exc_info=True)
        raise e



