import spacy

def get_nlp_object():
    return spacy.load('de_core_news_sm')