from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """ "Search wikipedia"""

    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def sumarize_wikipedia(name):
    """Sumarize wikipedia"""
    print(f"Finding wikipedia sumary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Gets text blob object and returns"""

    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia name and returns phrases"""

    text = sumarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases


# golden_state_warriors = wikipedia.summary("Golden State Warriors")
# blob.noun_phrases
