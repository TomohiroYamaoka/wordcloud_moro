from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()

sentenses = [
    "送料が安い",
    "これを使うと頭皮が痒くなる",
    "髪がサラサラになる"
]

for sentence in sentenses:
    print("=============================================")
    print(sentence)

    for token in tokenizer.tokenize(sentence):
        print("    " + str(token))
