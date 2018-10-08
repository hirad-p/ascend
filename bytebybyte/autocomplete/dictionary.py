
class Node:
  def __init__(self, prefix):
    self.prefix = prefix
    self.children = dict()

class Autocomplete:
  def __init__(self, words):
    self.trie = Node("")
    for w in words:

  def insert(word):
    current = self.trie
    for ch in word:
      if ch