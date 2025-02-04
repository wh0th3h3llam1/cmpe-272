# import pandas as pd
# from textblob import TextBlob
#
# # Load CSV file
# df = pd.read_csv("input_test.csv", header=None)
#
# # Assuming the tweet text is in the 6th column (index 5)
# df["Sentiment"] = df[5].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
#
# # Function to categorize sentiment
# def categorize_sentiment(score):
#     if score > 0:
#         return "Positive"
#     elif score < 0:
#         return "Negative"
#     else:
#         return "Neutral"
#
# df["Sentiment_Label"] = df["Sentiment"].apply(categorize_sentiment)
#
# # Save the results to an Excel file
# df[[5, "Sentiment_Label"]].to_excel("sentiment_results.xlsx", index=False, header=["Text", "Sentiment"])
#
# print("Sentiment analysis completed! Check sentiment_results.xlsx")


import pandas as pd
from textblob import TextBlob

# Load the CSV file
df = pd.read_csv("input_test.csv", header=None)

# Assuming the tweet text is in the 6th column (index 5)
df["Sentiment"] = df[5].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Function to categorize sentiment
def categorize_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment_Label"] = df["Sentiment"].apply(categorize_sentiment)

# Save the results to an Excel file
df[[5, "Sentiment_Label"]].to_excel("sentiment_results.xlsx", index=False, header=["Text", "Sentiment"])

print("Sentiment analysis completed! Check sentiment_results.xlsx")
