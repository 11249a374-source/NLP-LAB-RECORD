import nltk


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


sentence = input("Enter a sentence: ")


tokens = nltk.word_tokenize(sentence)


tagged = nltk.pos_tag(tokens)


grammar = r"""
    NP: {<DT>?<JJ>*<NN>}
"""


chunker = nltk.RegexpParser(grammar)


result = chunker.parse(tagged)


print(result)


result.draw()
