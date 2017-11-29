
# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

words.remove("do")
words.remove("cannot")
words.insert(2, "cannot")
words.insert(5, "do")

print(" ".join(words))