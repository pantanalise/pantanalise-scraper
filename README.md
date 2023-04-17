# Twitter Scraper

## Script description

This Python script scrapes Twitter data using the `snscrape` library and saves the results to an Excel file. The script searches for Portuguese tweets with at least 1000 likes, posted between January 1, 2022 and December 31, 2022. The script uses the `multiprocessing` library to speed up the data collection process by running multiple instances of the `get_tweets` function in parallel. The script also converts the date and time of each tweet to the timezone "America/Campo_Grande" and saves it to the Excel file.

## Requirements

- Python 3.x
- pandas
- snscrape
- pytz

## Usage

1. Install the required libraries if necessary:
   ```
   pip install pandas snscrape pytz
   ```
2. Save the script to your local machine.
3. Open a terminal window and navigate to the directory where the script is saved.
4. Run the script using the command:
   ```
   python script_name.py
   ```
   Replace "script_name.py" with the name of the file where you saved the script.
5. The script will start running and display the progress in the terminal. Once finished, it will save the results to an Excel file named "test.xlsx" in the same directory as the script.

## Parameters

The script contains one parameter: `max_tweets`, which sets the maximum number of tweets to scrape. By default, it is set to 10. To change the value, modify the number inside the square brackets in the line:

```python
searched_tweets = pool.map(get_tweets, [max_tweets])
```

## Output

The script saves the results to an Excel file named "test.xlsx" in the same directory as the script. The file contains one sheet named "Sheet1" with the following columns:

- Datetime: the date and time of the tweet in the format "YYYY-MM-DD HH:MM:SS timezone"
- Text: the content of the tweet
- Likes: the number of likes the tweet has received
- Retweets: the number of times the tweet has been retweeted
- Feeling: an empty column that will be used to record a sentiment analysis score.
