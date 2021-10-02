from __future__ import annotations


ALPHABET = {
    "a": 0,
    "b": 1,
    "c": 2,
    "ç": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "ğ": 8,
    "h": 9,
    "ı": 10,
    "i": 11,
    "j": 12,
    "k": 13,
    "l": 14,
    "m": 15,
    "n": 16,
    "o": 17,
    "ö": 18,
    "p": 19,
    "r": 20,
    "s": 21,
    "ş": 22,
    "t": 23,
    "u": 24,
    "ü": 25,
    "v": 26,
    "y": 27,
    "z": 28,
}


class Node:
    """Character node that is used in the trie."""

    character: str
    children: List[Node]
    is_word: bool

    def __init__(self, character: str = ""):
        self.character = character
        self.children = [None] * len(ALPHABET)
        self.is_word = False

    def __str__(self):
        return f'{self.character}, {self.is_word}, {self.children}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.character}, {self.is_word}, {self.children})'


class Trie:
    """Instantiates a new trie object."""

    root: Node

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """Inserts a new word into the trie."""

        curr = self.root
        for character in word:
            position = ALPHABET.get(character)
            if position is None:
                return None

            if curr.children[position] is None:
                node = Node(character)
                curr.children[position] = node
            curr = curr.children[position]
        curr.is_word = True
        return None

    def search(self, word: str) -> bool:
        """Checks if a given word exists in the trie."""

        node = self.get_node(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        """Checks if there are any nodes in the trie with the given prefix."""

        if not prefix:
            return False

        return self.get_node(prefix) is not None

    def get_node(self, word: str) -> Node:
        """Returns the last node of the given word/prefix if it exists."""

        curr = self.root
        for character in word:
            position = ALPHABET.get(character)
            if position is None:
                return None

            if curr.children[position] is None:
                return None
            curr = curr.children[position]
        return curr

    def suggest_words(self, prefix: str = None) -> List[str]:
        """Returns words that starts with the given prefix, using DFS."""

        if not prefix:
            return []

        prefix_node = self.get_node(prefix)
        if prefix_node is None:
            return []

        suggestions: List[str] = []

        stack = [(prefix, prefix_node)]
        while stack:
            prfx, node = stack.pop()

            if node.is_word:
                suggestions.append(prfx)

            for child in node.children:
                if not child:
                    continue
                stack.append((prfx + child.character, child))

        return suggestions

    def __str__(self):
        return f'{self.root}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.root.character})'
