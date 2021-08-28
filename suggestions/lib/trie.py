from __future__ import annotations


class Node:
    """Character node that is used in the trie."""
    
    ALPHABET = "abcçdefgğhıijklmnoöprsştuüvyz"
    character: str
    children: List[Node]
    is_word: bool
    
    def __init__(self, character: str = ""):
        self.character = character
        self.children = [None] * len(Node.ALPHABET)
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
            try:
                position = Node.ALPHABET.index(character)
            except ValueError:
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
        """Checks if a word with the given prefix exists."""

        if not prefix:
            return False

        return self.get_node(prefix) is not None

    def get_node(self, word: str) -> Node:
        """Returns the last node of the given word if it exists."""

        curr = self.root
        for character in word:
            try:
                position = Node.ALPHABET.index(character)
            except ValueError:
                return None

            if curr.children[position] is None:
                return None
            curr = curr.children[position]

        return curr

    def suggest_words(self, prefix: str = None) -> List[str]:
        """Returns words that starts with the given prefix, using DFS."""

        if not prefix:
            return []

        suggestions: List[str] = []
        stack: List[Tuple(str, int, Node)] = []
        stack.append((self.root.character, 0, self.root))

        while stack:
            parent, level, node = stack.pop()

            if node.is_word and parent.startswith(prefix) and parent != prefix:
                suggestions.append(parent)

            for child in node.children:
                if not child:
                    continue

                if level < len(prefix):
                    if prefix[level] == child.character:
                        stack.append(
                            (parent + child.character, level + 1, child))
                else:
                    stack.append((parent + child.character, level + 1, child))

        return suggestions

    def __str__(self):
        return f'{self.root}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.root.character})'
