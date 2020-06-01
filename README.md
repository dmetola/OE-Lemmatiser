# OE-LEMMATISER

A simple lemmatiser in charge of tokenising, lemmatising and tagging Parts of Speech (POS) in any Old English input.

The main aim of this little project is to cover a gap exiting in the field of study of Old English. 
There are some tools that help the study of Old English from a linguistic point of view, but they lack a tool that creates
comprehensive information, which can be the starting point to any piece of research.

This tool is not one in charge of lemmatising, tokenising or tagging full texts or sentences, it can also work with lists 
of adjectives, verbs, etc. so that you can focus in any of the grammatical categories of Old English.

At first sight, the code may seem to be repetitive. One of the reasons for that is that I had to solve the issue of 
tokenisation. The CNLTK corpus does not support tokenisation in Old English, so I had to use the 'en_core_web_sm' corpus
from Spacy. 

The program can be run as a whole, exporting all the information in a single .txt file. One of the drawbacks I have found, and
which I am trying to solve, is that of presenting all the information in columns. Some functions from Spacy cannot be applied
when working with CNLTK (or at least I cannot apply them), so the information can be presented in chunks, but separately.
The user can also run the module of the code that fits the purpose of his/her research. If the intention of the user is to tag 
Parts of Speech of some text, for example, this user can only run the import modules, the line in charge of creating a .txt 
file, and then just the POS_tagger code lines.

This is a preliminary version, but a fully-working one. Apart from the much-needed correction of how the output is presented,
it also needs to be improved so that it can cope with larger sets of texts, or even full corpora, but that first issue has 
to be fixed before moving on more complex issues.

Another thing I need to point out is that, at the moment, this program was implemented in a Jupyter notebook, I am not sure
if how it will work in an IDE. This is something that will also be improved in future versions of the project.

To wrap up, this is my first project in NLP and Python. Although I have experience in manual lemmatisation, manual tagging
and tokenisation in Old English, I have wanted for some time to create a program that may allow students, researchers and
scholars to process the data before moving on to more specific aspects of the study of the Old English language. I sincerely
hope that this program can help them achieve their results in a faster and easier way.

Thank you very much for your attention.

PS. Any comments/suggestions about my project will be gladly received.
