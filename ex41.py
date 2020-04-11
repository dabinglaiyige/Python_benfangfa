import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/word.txt"
WORDS = []

PHRASES = {
"class %%%(%%%):":
"Make a class named %%% that is-a %%%.",
"class %%%(object):\ntdef __init__(self, ***)":
"class %%% has-a __init__ that takes self and *** params.",
"class %%%(object):\n\tdef ***(self, @@@)":
"class %%% has-a function *** that takes self and @@@ params.",
"*** = %%%()":
"Set *** to an instance of class %%%.",
"***.***(@@@)":
"From *** get the *** function, call with params self, @@@",
"***.*** = '***'":
"From *** get the *** attribute and sit to '***'"
}

# do they want to drill pharaes first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHARSE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))


def convert(snippet, phrase):
    class_name = [for w in random.sample(WORDS, snippet.count("%%%"))
            w.capitalize()]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

        for sentence in snippet, phrase:
            result = sentecce[:]

