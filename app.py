import json

from flask import Flask
from flask import request, jsonify
from flask.views import MethodView

from utils import clean_text

app = Flask(__name__)


class WordListView(MethodView):
    def post(self):
        text_data_dict = json.loads(request.data)
        phrases_list, unique_word_list = clean_text(text_data_dict["texts"])
        word_counter = {}

        for index, phrase in enumerate(phrases_list):
            word_counter[index] = [phrase.count(word) for word in unique_word_list]

        json_data = {"unique_words": unique_word_list, "word_count": word_counter}
        return jsonify(json_data)


word_list_view = WordListView.as_view("word_list_view")
app.add_url_rule("/", view_func=word_list_view, methods=["POST"])
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
