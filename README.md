# Turkish Auto-Completion

<p align="center">
  <img src="https://media.giphy.com/media/KArsmHDUvE2AqW7cx4/giphy.gif" alt="turkish auto-completion" />
</p>

## Auto-completion using tries

A simple app that implements an auto-completion feature using Trie data structure.

The corpus is made of up most popular 100K keywords in Turkish language.

At most 10 suggestions are returned, and these are selected based on the Levenshtein distance of the suggested words to the prefix. 
Words with minimum edit distance are shown.

# Front-end

[/app](app/) folder contains a simple React app that serves the UI for this project.

# Suggestion Service

[Suggestion API](suggestions/) uses Python & Flask.
