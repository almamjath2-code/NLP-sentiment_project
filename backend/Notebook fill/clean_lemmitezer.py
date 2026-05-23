#
from nltk.corpus import wordnet
from nltk import pos_tag
import joblib

all_stopwords = joblib.load("stopwords.pkl")


def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    

    
  #it can reduce words correctly like runnig to run .
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

#stopwords_set = build_stopwords(text)


def after_cleaning_text(text):
    words = text.split()
    tagged_words = pos_tag(words)

    cleaned_words = []

   

    for w, pos in tagged_words:
        if w in all_stopwords:#add my auto remove after visulization stop words
            continue

        wn_pos = get_wordnet_pos(pos)

        lemma = lemmatizer.lemmatize(w, wn_pos)

        # 🔥 fix for verbs (important)
        if wn_pos == 'v' and lemma == w:
            lemma = lemmatizer.lemmatize(w, 'v')

        cleaned_words.append(lemma)

    return " ".join(cleaned_words)   
#