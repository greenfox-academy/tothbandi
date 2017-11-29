# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

l = quote.split(" ")
l.insert(3, "always takes longer than")
quote = " ".join(l)

print(quote)