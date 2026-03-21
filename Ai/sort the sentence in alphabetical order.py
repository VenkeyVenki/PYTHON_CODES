#Write a python program to sort the sentence in alphabetical order


def sort_sentence(sentence):
  words = sentence.split()
  sorted_words = sorted(words)
  return " ".join(sorted_words)
sentence = "This is a sentence to be sorted."
sentence=sentence.lower()
sorted_sentence = sort_sentence(sentence)
print(sorted_sentence)
