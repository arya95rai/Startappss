# Write a generator that yields words from a sentence one by one.
def gen(sen):
    for i in sen.split():
        yield i
sentence=input("Enter any sentence: ")
for i in gen(sentence):
    print(i)