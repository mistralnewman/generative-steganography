import random

def is_zero(letter):
    return letter in "aeiouy0"

def word_to_bin(string):
    string = string.lower()
    binary = ""
    for letter in string:
        if is_zero(letter):
            binary += "0"
        elif letter == " ":
            binary += ""
        else:
            binary += "1"
    return binary

def make_bin_dict(words):
    result = dict()
    for word in words:
        bword = word_to_bin(word)
        if bword in result:
            result[bword].append(word)
        else:
            result[bword] = [word]
    return result

with open("adjectives.txt","r") as adj_file:
    adjectives = make_bin_dict(adj_file.read().split("\n"))

with open("nouns.txt","r") as noun_file:
    nouns = make_bin_dict(noun_file.read().split("\n"))

with open("intrans.txt", "r") as vtr_file:
    verbs_tr = make_bin_dict(vtr_file.read().split("\n"))

with open("trans.txt", "r") as vitr_file:
    verbs_itr = make_bin_dict(vitr_file.read().split("\n"))

with open("determiners.txt", "r") as det_file:
    determiners = make_bin_dict(det_file.read().split("\n"))

with open("prepositions.txt", "r") as prep_file:
    prepositions = make_bin_dict(prep_file.read().split("\n"))

def v_tr(btext):
    if btext in verbs_tr:
        return verbs_tr[btext][random.randint(0,len(verbs_tr[btext])-1)]
    else:
        return False
def v_itr(btext):
    if btext in verbs_itr:
        return verbs_itr[btext][random.randint(0,len(verbs_itr[btext])-1)]
    else:
        return False
def n(btext):
    if btext in nouns:
        return nouns[btext][random.randint(0,len(nouns[btext])-1)]
    else:
        return False
def adj(btext):
    if btext in adjectives:
        return adjectives[btext][random.randint(0,len(adjectives[btext])-1)]
    else:
        return False
def det(btext):
    if btext in determiners:
        d = determiners[btext][random.randint(0,len(determiners[btext])-1)]
        return d
    else:
        return False
def prep(btext):
    if btext in prepositions:
        d = prepositions[btext][random.randint(0,len(prepositions[btext])-1)]
        return d
    else:
        return False


def decode(msg):
    q = ""
    for l in msg:
        if is_zero(l):
            q += "0"
        elif l == " ":
            q += ""
        else:
            q += "1"
    z = ""
    for x in range(0, len(q) - 7, 8):
        z += chr(int(q[x:x + 8], 2))
    return z

def ascii_to_bin(msg):
    return ''.join([bin(ord(x))[2:].zfill(8) for x in msg])

def sentenceify(s):
    return s[0].upper() + s[1:] + "."
