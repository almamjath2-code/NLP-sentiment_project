#this is orginal order by number wise
import re
import contractions

def clean_text(text):
    #1.
    text = str(text).lower()
    #2.fix smart quotes FIRST
    text = text.replace("’", "'")
    #3.remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    #4. expand contractions (BEST STEP) this change text like "don't" to "do not" and "it's" to "it is"
    text = contractions.fix(text)
    #5. remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    #6. remove numbers
    text = re.sub(r'\d+', '', text)
    #7.remove punctuation like !,?,.,, etc but keep spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    #8. remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    #9. remove repeated characters (like "soooo" to "soo")
    text = re.sub(r'(.)\1+', r'\1\1', text)
    #10. remove non-ASCII characters (like emojis or special symbols)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    #11. remove words with less than 3 characters (like "is", "a", "to", etc)
    text = " ".join([w for w in text.split() if len(w) > 2])

    return text