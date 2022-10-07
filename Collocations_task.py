#importing important libraires' 
from nltk import FreqDist
import re
from nltk.corpus import wordnet as wn

#main part of program
synset = set()
synset_say = wn.synsets("say")
all_say =[]

for i in synset_say:
    if i.pos() in "v":
        all_say.append(i.lemma_names())
all_say = [j for i in all_say for j in i]

say_synset = set(all_say)

#open file with write permission 
with open(r"C:\PyCharmGrammarly\Grammarly\say_synset.txt", "w") as file:
    for j in say_synset:
        file.write(j)
        file.write("\n")

import spacy
nlp = spacy.load("en_core_web_md", disable=['textcat', 'ner'])
example = nlp('Enounce me about the issue immediately.')

def nlp_def(with_ly):
    adv_dict = {}
    for sent in with_ly:
        nlp_sent = nlp(sent)
        for tok in nlp_sent:
            if tok.lemma_ in say_synset:
                if tok.lemma_ not in adv_dict.keys():
                    adv_dict[tok.lemma_] = []
                children = list(tok.children)
                for c in children:
                    if c.text.endswith('ly') and c.pos_ in "ADV":
                        adv_dict[tok.lemma_].append(c.text)
                        grand_children = list(c.children)
                        for g in grand_children:
                            if g.text.endswith('ly') and g.pos_ in "ADV":
                                adv_dict[tok.lemma_].append(g.text)
    for verb, adverb in adv_dict.items():
        print("{} : {} .".format(verb, FreqDist(adverb).most_common()))

with open(r"C:\git_project\summer-school-2019\classes\5_syntax\task-collocations\blog2008.txt", "r", encoding="utf-8") as text:
    with_ly = []
    sent_text = text.readlines()
    reg = re.compile(r"\w+ly\b")
    for t in sent_text:
        if re.findall(reg, t):
            with_ly.append(t)
    nlp_def(with_ly)




#end of the code


