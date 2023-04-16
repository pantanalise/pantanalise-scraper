import pandas as pd
import snscrape.modules.twitter as sntwitter
from datetime import datetime
from multiprocessing import Pool
import pytz

timezone = pytz.timezone("America/Campo_Grande")


def get_tweets(max_tweets):
    searched_tweets = []
    for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(
            "lang:pt min_faves:1000 since:2022-01-01 until:2022-12-31"
        ).get_items()
    ):
        if i >= max_tweets:
            break
        print(tweet.content)
        searched_tweets.append(
            (tweet.date, tweet.content, tweet.likeCount, tweet.retweetCount, "")
        )

    return searched_tweets


if __name__ == "__main__":
    start = datetime.now()
    print(f"Started at {start}")

    with Pool() as pool:
        searched_tweets = pool.map(get_tweets, [10])

    searched_tweets = [tweet for tweets in searched_tweets for tweet in tweets]

    df = pd.DataFrame(
        searched_tweets, columns=["Datetime", "Text", "Likes", "Retweets", "Feeling"]
    )
    df["Datetime"] = df["Datetime"].apply(
        lambda x: x.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    )

    with pd.ExcelWriter("test.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)

    end = datetime.now()
    print(f"Ended at {end}. Total time: {end - start}")