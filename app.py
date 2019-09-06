import json

from flask import Flask
from flask import request, jsonify
from flask.views import MethodView

from utils import clean_text

app = Flask(__name__)


class WordListView(MethodView):
    def post(self):
        text_data_dict = json.loads(request.data)
        ngrams_args = request.args.get("ngrams", None)
        texts = text_data_dict.get("texts", None)

        if texts is None:
            return (
                jsonify({"error": 'Key value error. Ensure that the key is "texts"'}),
                400,
            )

        if not isinstance(texts, list):
            return (
                jsonify(
                    {"error": "Input value not supported. Only lists are supported."}
                ),
                400,
            )

        if len(texts) == 0:
            return (jsonify({"error": "Provide a valid list. Empty list found."}), 400)

        if not isinstance(texts[0], str):
            return (
                jsonify(
                    {
                        "error": "Provide a valid value inside the list. Type found not string."
                    }
                ),
                400,
            )

        phrases_list, unique_word_list = clean_text(
            text_data_dict["texts"], ngrams_args
        )
        word_counter = {}
        for index, phrase in enumerate(phrases_list):
            word_counter[index] = [phrase.count(word) for word in unique_word_list]

        json_data = {"unique_words": unique_word_list, "word_count": word_counter}
        return jsonify(json_data)


word_list_view = WordListView.as_view("word_list_view")
app.add_url_rule("/", view_func=word_list_view, methods=["POST"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)