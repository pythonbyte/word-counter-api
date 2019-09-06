import json

from flask import Flask
from flask import request, jsonify
from flask.views import MethodView

from utils import STOP_WORDS

app = Flask(__name__)


def clean_text(text):
    unique_word_list = set(re.sub(r'\s*\b(\d+\w*)', '', ''.join(text).lower()).translate(str.maketrans('', '', string.punctuation)).split())
    filtered_unique_words_list = set([i for i in unique_word_list if i not in STOP_WORDS])
    phrases_list = [re.sub(r'\s*\b(\d+\w*)['+string.punctuation+ ']', ' ', ''.join(i).lower()).split() for i in text]

    return phrases_list, sorted(filtered_unique_words_list)


class WordListView(MethodView):

    def post(self):
        text_data_dict = json.loads(request.data)
        phrases_list, unique_word_list = clean_text(text_data_dict['texts'])
        word_counter = {}

        for index, phrase in enumerate(phrases_list):
            word_counter[index] = ([phrase.count(word) for word in unique_word_list])


        json_data = {
            "unique_words": unique_word_list,
            "word_count": word_counter
        }
        return jsonify(json_data)



word_list_view =  WordListView.as_view('word_list_view')
app.add_url_rule(
    '/', view_func=word_list_view, methods=['POST']
)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)