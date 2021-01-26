# Description

Flask API that filters texts into word vectors filtered by the occurrence of unique words inside the text. The program will clean the input text, removing punctuation, strings that begin with number and remove stop words. The app is alphabetically ordered.


<b>POST</b> is the only method allowed.

# Endpoint
This endpoint works at the /.  Receives a object({}) with key as 'texts' and an array as value.

<b>Post</b>: '/'
```
{
	"texts": ["Falar é fácil. Mostre-me o código."]
}
```
<b>Response</b>
```
{
    "unique_words": [
        "código",
        "falar",
        "fácil",
        "mostre"
    ],
    "word_count": {
        "0": [
            1,
            1,
            1,
            1
        ]
    }
}
```

# Parameter
This endpoint receive a <b>ngrams</b> parameter, that will separate the input text into the number passed as parameter

<b>Post</b>: '/?ngrams=2'
```
{
	"texts": ["Falar é fácil. Mostre-me o código."]
}
```
<b>Response</b>
```
{
    "unique_words": [
        "falar é",
        "fácil mostre",
        "me o",
        "mostre me",
        "o código",
        "é fácil"
    ],
    "word_count": {
        "0": [
            1,
            1,
            1,
            1,
            1,
            1
        ]
    }
}

```
<b>Post</b>: '/?ngrams=3'
```
{
	"texts": ["Falar é fácil. Mostre-me o código."]
}
```
<b>Response</b>
```
{
    "unique_words": [
        "falar é fácil",
        "fácil mostre me",
        "me o código",
        "mostre me o",
        "é fácil mostre"
    ],
    "word_count": {
        "0": [
            1,
            1,
            1,
            1,
            1
        ]
    }
}
```
