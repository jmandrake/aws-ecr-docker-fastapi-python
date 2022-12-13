from textblob import TextBlob
import wikipedia


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for names"""

    results = wikipedia.search(name)
    return results


def phrase(name):
    """Returns phrase from Wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
