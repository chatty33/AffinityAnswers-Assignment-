import re ## regular expression ki library

def calculate_profanity_score(sentence, racial_slurs):
    sentence = sentence.lower()
    words = re.findall(r'\w+', sentence)  # Extract words from the sentence
    profanity_score = sum(word in racial_slurs for word in words)
    return profanity_score

def main():
    racial_slurs = {'sale', 'kutte', 'kamine'}  # Set of racial slurs / gaalis

    # Read tweets from the file
    with open('tweets.txt', 'r') as file:
        tweets = file.readlines()

    # Calculate vulgarness/profanity score for each tweet i.e. count no. of gaalis in sentence
    for tweet in tweets:
        score = calculate_profanity_score(tweet, racial_slurs)
        print(f"Tweet: {tweet.strip()}")
        print(f"Profanity Score: {score}\n")

if __name__ == '__main__':
    main()
