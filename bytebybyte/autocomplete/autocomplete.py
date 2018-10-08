import sys

words = ["abc", "acd", "bcd", "def", "a", "aba"]

def autocomplete(prefix):
  return [x for x in words if x.startswith(prefix)]

if __name__ == "__main__":
  suggestions = autocomplete(sys.argv[1])
  print(suggestions)
