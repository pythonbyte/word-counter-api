import re
from nltk.util import ngrams

from constants import STOP_WORDS


def _text_cleaner(text):
    # function that lower letters, clean punctuation and
    # strings that start with numbers, return a cleaned text
    return re.findall(r'\w+', re.sub(r"\s*\b(\d+\w*)", "", "".join(text).lower()))


def clean_text(text, ngrams_number: int = None):
    if ngrams_number is None:
        unique_word_list = set(_text_cleaner(text))
        filtered_unique_words_list = set(
            [i for i in unique_word_list if i not in STOP_WORDS]
        )
    else:
        filtered_words_list = set

        for word in text:
            cleaned_word = set(ngrams(_text_cleaner(word),2))
            filtered_words_list = filtered_words_list.union(cleaned_word)

        filtered_unique_words_list = [' '.join(i) for i in filtered_words_list]

    phrases_list = [' '.join(_text_cleaner(i)) for i in text]

    return phrases_list, sorted(filtered_unique_words_list)
