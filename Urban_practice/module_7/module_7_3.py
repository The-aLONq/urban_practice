class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        punctuation = (',', '.', '=', '!', '?', ';', ':', ' - ')

        for file_name in self.file_name:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for p in punctuation:
                        line = line.replace(p , '')
                    if line:
                        words.extend(line.split())
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        results = []

        for file_name in self.file_name:
            words = self.get_all_words().get(file_name, [])
            if word in words:
                position = words.index(word)
                results.append((file_name,position + 1))

        return results

    def count(self, word):
        word = word.lower()
        total_count = 0

        for file_name in self.file_name:
            words = self.get_all_words().get(file_name, [])
            total_count += words.count(word)

        return total_count

finder2 = WordsFinder('sample.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего