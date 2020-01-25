import re
import string
import spacy
from unidecode import unidecode
from bs4 import BeautifulSoup


__all__ = ["TextProcessor"]


class TextProcessor:

    def __init__(self, language='en_core_web_sm'):
        self.language = language
        self.nlp = spacy.load(self.language)

    def strip_html(self, text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text(separator=" ")

    def remove_accents(self, text):
        return unidecode(text)

    def remove_punct(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def remove_stopwords(self, text):
        return ' '.join([el.text for el in self.nlp(text) if not el.is_stop])

    def lemmatize(self, text):
        return ' '.join([el.lemma_ for el in self.nlp(text) if el.lemma_ not in ["-PRON-"]])

    def remove_spaces(self, text):
        return re.sub('\s+', ' ', text).strip()

    # def remove_digits

    # def remove_ner

    def tokenize(self, text):
        return [token.text for token in self.nlp(text)]

    def preprocess(self, text):
        return self.tokenize(self.remove_spaces(self.remove_accents(self.remove_stopwords(
                self.lemmatize(self.remove_punct(self.remove_punct(self.strip_html(text)).lower()))))).strip())
