import re
import string

from constants import STOP_WORDS


def _text_cleaner(text):
    # function that lower letters, clean punctuation and
    # strings that start with numbers, return a cleaned text
    return re.sub(r"\s*\b(\d+\w*)", "", "".join(text).lower()).translate(
        str.maketrans("", "", string.punctuation)
    )


def clean_text(text):
    unique_word_list = set(_text_cleaner(text).split())
    filtered_unique_words_list = set(
        [i for i in unique_word_list if i not in STOP_WORDS]
    )
    phrases_list = [_text_cleaner(i).split() for i in text]

    return phrases_list, sorted(filtered_unique_words_list)
