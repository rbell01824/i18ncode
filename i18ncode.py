
'''
Playing around with i18n problem.

NOTE: there are several unexplored boundry conditions. This code is NOT bug free!!!

'''

# some test words
test_words = ['a', 'i', 'an', 'at', 'fiern', 'fierx', 'fiarn', 'fuern', 'blue', 'elephant']


class Code_i18n:

    def __init__(self):
        self.word_codes = {}
        self.conflicts = 0

    def code_a_word(self, word, n=1):
        wl = len(word)
        word = word.strip()
        if wl < 1 or not word.isalnum():
            # print(' not a word:<' + word + '>')
            return
        if wl <= 2:
            self.word_codes[word] = word
            # print('short word:', word)
            return word
        code = word[:n] + str(wl - n - 1) + word[-1]
        if code not in self.word_codes:
            self.word_codes[code] = word
            return code
        conflict_word = self.word_codes[code]
        if word == conflict_word:
            print('duplicate word: ', word)
            return code
        if conflict_word != '-':
            self.conflicts += 1
            # print('conflict code ', code, word, ':', conflict_word)
        return self.code_a_word(word, n + 1)

    def key_lengths(self):
        n = max(len(w) for w in self.word_codes.keys())     # tricky bit since we are Python 3
        print('max key length:', n)
        lengths = [0] * (n+1)
        for key in self.word_codes.keys():
            lengths[len(key)] += 1
        print('distribution of key lengths', lengths)
        return

    def word_lengths(self):
        n = max(len(w) for w in self.word_codes.values()) + 1
        print('max word length:', n)
        lengths = [0] * (n + 1)
        for key in self.word_codes.keys():
            lengths[len(self.word_codes[key])] += 1
        print('distribution of word lengths', lengths)
        return

    def report(self, nkeys=0):
        print('conflicts:', self.conflicts)
        self.key_lengths()
        self.word_lengths()
        if nkeys == 0:
            print(self.word_codes)
        else:
            keys = list(self.word_codes.keys())[:nkeys]
            print([(key, self.word_codes[key]) for key in keys])
        return


def doit():
    global test_words

    # print( test_words)
    print('test words')
    print(test_words)

    print('----------')
    codes = Code_i18n()

    for word in test_words:
        codes.code_a_word(word)
        # print( 'unique code for ', code, unique_i18n_code(word))
    codes.report()

    # now lets try some real words
    print('---------------')
    codes = Code_i18n()
    words = 0
    with open('words') as fp:
        for line in fp:
            words += 1
            codes.code_a_word(line)
    print('words ', words)
    codes.report(20)

    # # how many words differ by only the last character
    # cnt = 0
    # for key in word_codes.keys():
    #     if key == word_codes[key]:
    #         cnt += 1
    # print('words that can not be uniquely coded: ', cnt)
    # print('a:', word_codes['a0'])

if __name__ == "__main__":
    doit()
