file_name = 'beatles.txt'
with open(file_name, 'r') as txt_file:
    file_content = txt_file.read()

lowercase_content = file_content.lower()

import string
from collections import Counter

punctuation_symbols = ',.!?'
punctuation_stats = Counter(symbol for symbol in file_content if symbol in punctuation_symbols)

punctuation_sum = sum(punctuation_stats[symbol] for symbol in punctuation_symbols)

print(f'Количество знаков препинания (, . ! ?): {punctuation_sum}')

no_punctuation_content = lowercase_content.translate(str.maketrans('', '', string.punctuation))
word_list = no_punctuation_content.split()

distinct_words = set(word_list)
distinct_word_count = len(distinct_words)

word_frequency = Counter(word_list)

print(f'Количество уникальных слов: {distinct_word_count}')

top_word, top_word_count = word_frequency.most_common(1)[0]
words_used_once = sum(1 for count in word_frequency.values() if count == 1)

print(f'Слово, использованное наибольшее количество раз: "{top_word}" ({top_word_count} раз)')
print(f'Количество уникальных слов, используемых только один раз: {words_used_once}')

you_occurrences = word_frequency.get('you', 0)
i_occurrences = word_frequency.get('i', 0)

print(f'Количество слов "you": {you_occurrences}')
print(f'Количество слов "I": {i_occurrences}')