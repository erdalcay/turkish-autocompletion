# Suggestion Service

<p>Flask API with a single route that returns the Turkish words from the corpus, made up of most popular 100K words, that are starting with the input prefix.</p>

`/suggestions` accepts `POST` requests and returns an array of words.

Example:

```javascript
curl --location --request POST 'http://127.0.0.1:3000/suggestions' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prefix": "amaç"
}'
```

Response:

```json
HTTP 200
application/json
[
    "amaçlı",
    "amaçsız",
    "amaçlama",
    "amaçsızca",
    "amaçlılık",
    "amaçlanma",
    "amaçlanan",
    "amaçlamak",
    "amaçsızlık",
    "amaçlanmak"
]
```

## Request body

There is only a single accepted body parameter.

<table style="width: 100%;">
<tr><th>Name</th><th>Description</th><th>Required</th></tr>
<tr><th>prefix</th><th>Prefix to suggest words upon</th><th>True</th></tr>
</table>

```json
Raw JSON
{
  "prefix": "test"
}
```

## Response

Returned words are in ascending sorted order of their edit distance from the input prefix using Levenshthein distance.

## Development

To run the app locally, do:

```
make development
```
