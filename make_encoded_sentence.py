import words
import random
import functools
# Mistral Newman
# <hnewman@oberlin.edu>
# this is a prototype version of generative steganography code!
# it ... works, but isn't pretty (TODO: make it better)

# make_phrase takes two word-returning functions and a text
# and returns either a valid splitpoint for the text with words from each function
# or False
def make_phrase(btext,f1,f2):
    length = len(btext)
    # test random index splits
    # return the first one that works
    indexes = [x for x in range(length)]
    random.shuffle(indexes)
    for idx in indexes:
        w1 = f1(btext[:idx])
        w2 = f2(btext[idx:])
        # f1 and f2 return either a valid word or False
        if w1 and w2:
            # if neither is False, we've found one that works
            return f1(btext[:idx]) + " " + f2(btext[idx:])
    return False

# will always & only make a sentence of the form
# det adj n v_tr det adj n
# however, you can play with these functions to make new grammars
# making the code itself decide between grammars is a WIP!
# (also, making this less hacky and terrible is a WIP!)
# (functools.partial is probably not the best way to curry things)
detadj = functools.partial(make_phrase, f1 = words.det, f2 = words.adj)
np = functools.partial(make_phrase, f1 = detadj, f2 = words.n)
vp = functools.partial(make_phrase, f1 = words.v_tr, f2 = np)
pp = functools.partial(make_phrase, f1 = words.prep, f2 = np)
s = functools.partial(make_phrase, f1 = np, f2 = vp)

print("Please enter a word you would like to encode!")
msg = words.ascii_to_bin(input(">"))
for _ in range(10):
    r = s(msg)
    print(words.sentenceify(r) if r else r)