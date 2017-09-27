# 2017, Daniel "The Doon" Stotts
from sys import argv
from os.path import basename

# Print   h e l p f u l   message if no sentence is given
if len(argv) == 1:
    print("Usage: python {} <your> <message> <here>".format(basename(__file__)))
    exit()

# Concatenate all given parameters
meme = " ".join(argv[1:])

# Do the thing
mid = int((len(meme) - 1) / 2)

# a b c d e f g
print(" ".join(meme))

# b           f
# c           e
for i in range(mid - 1):
    print(meme[i + 1], end="")
    print(" " * (i * 2 + 1), end="")
    print("\\", end="")
    print(" " * ((len(meme) - 2) * 2 - (i * 2) - 1), end="")
    print(meme[-2 - i], end="")
    print(" " * (i * 2 + 1), end="")
    print("\\")

# d     a b c d e f g
print(meme[mid], end="")
print(" " * (mid * 2 - 1), end="")
print(" ".join(meme))

# e     b     c     f
# f     c     b     e
for i in range(len(meme) - mid - 2):
    print(meme[i + mid + 1], end="")
    print(" " * (mid * 2 - 1), end="")
    print(meme[i + 1], end="")
    print(" " * (((len(meme) - 2) - mid) * 2 + 1), end="")
    print(meme[-i - mid - 2], end="")
    print(" " * (mid * 2 - 1), end="")
    print(meme[-2 - i])

# g f e d c b a     d
print(" ".join(meme[::-1]), end="")
print(" " * (mid * 2 - 1), end="")
print(meme[mid])

#       e           c
#       f           b
for i in range(mid - 1):
    print(" " * (i * 2 + 2), end="")
    print("\\", end="")
    print(" " * ((mid - i) * 2 - 3), end="")
    print(meme[-mid + i], end="")
    print(" " * (((len(meme) - 2) - mid + i) * 2 + 3), end="")
    print("\\", end="")
    print(" " * ((mid - i) * 2 - 3), end="")
    print(meme[mid - i - 1])

# g f e d c b a
print(" " * (mid * 2), end="")
print(" ".join(meme[::-1]))
