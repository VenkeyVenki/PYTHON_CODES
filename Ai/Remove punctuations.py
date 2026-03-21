#Write a python program to remove punctuations from the given string.


def remove_punctuation(text):
  no_punct = ""
  for char in text:

    if char.isalnum() or char.isspace():
      no_punct += char
  return no_punct
text = "This is a string! With some punctuation?"
text_without_punct = remove_punctuation(text)
print(text_without_punct)
