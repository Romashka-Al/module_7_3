class Wordsfinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        res = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as f1:
                a = []
                for line in f1:
                    line = line.lower().replace('\n', '')
                    for words in line.split():
                        a.append(words)
                res[name] = a
        return res

    def find(self, word):
        for keys, items in self.get_all_words().items():
            for i in range(len(items)):
                if items[i] == word.lower():
                    return {keys: i + 1}

    def count(self, word):
        mas = {}
        for keys, items in self.get_all_words().items():
            res = 0
            for i in range(len(items)):
                if items[i] == word.lower():
                    res += 1
            mas[keys] = res
        return mas


finder = Wordsfinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('TeXt'))
