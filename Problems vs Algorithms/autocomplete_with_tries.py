from collections import defaultdict

## Represents a single node in the Trie
class TrieNode(object):
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = defaultdict(TrieNode)
        self.word = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char]

    def _recurse_trie_node(self, start_node, word=""):
        word_list = list()
        while start_node.children:
            node_key = list(start_node.children.keys())[0]
            word += node_key
            start_node = start_node.children[node_key]
            if start_node.word:
                word_list.append(word)

        return word_list

    def suffixes(self, suffix=""):
        suffix_list = list()
        node = self
        for char in suffix:
            if char not in node.children:
                return "".join(suffix_list)
            for child_char, child in node.children.items():
                if char == child_char:
                    node = child
                    break
        if node.word or bool(node.children):
            if len(node.children) == 1:
                suffix_list += self._recurse_trie_node(node)
            elif len(node.children) > 1:
                for child_key, child_node in node.children.items():
                    suffix_list += self._recurse_trie_node(child_node, child_key)

        return suffix_list


## The Trie itself containing the root node and insert/find functions
class Trie(object):
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
        current_node.word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node


MyTrie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.root.suffixes("f"))
print(MyTrie.root.suffixes("ant"))
print(MyTrie.root.suffixes("trigo"))
