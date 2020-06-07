import spacy
nlp = spacy.load('en_core_web_sm')
from cltk.corpus.utils.importer import CorpusImporter

corpus_importer = CorpusImporter('old_english')
corpus_importer.list_corpora
corpus_importer.import_corpus('old_english_models_cltk')

import cltk.lemmatize.old_english.lemma as oe_l
lemmatizer = oe_l.OldEnglishDictionaryLemmatizer()

from cltk.tag.pos import POSTag
tagger = POSTag('old_english')

%%writefile #ENTER-YOUR-FILE-NAME.txt
TEXT TOKENIZED

#TOKENIZATION
doc = nlp(#ENTER YOUR STRING HERE)
with open('#ENTER-YOUR-FILE-NAME.txt', 'a+') as f:
    for token in doc:
        tokens = print(token.text, file = f) 

%%writefile -a #ENTER-YOUR-FILE-NAME.txt

TEXT LEMMATIZED:

#LEMMATIZER 

doc = (#ENTER YOUR STRING HERE)

lemma = lemmatizer.lemmatize(doc, best_guess=False)

with open(#ENTER-YOUR-FILE-NAME.txt, 'a+') as f:
    print(lemma, file = f)
    
%%writefile -a #ENTER-YOUR-FILE-NAME.txt
 
TEXT TAGGED:

#POS TAGGER

POS = tagger.tag_crf(doc)

with open('#ENTER-YOUR-FILE-NAME.txt', 'a+') as f:
    print(POS, file = f)
