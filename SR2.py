new_words = set()

def add_word(word):
    new_words.add(word.lower())

def search_by_prefix(prefix):
    return [w for w in new_words if w.startswith(prefix.lower())]

def frequency_report():
    print(f"Загальна кількість унікальних слів: {len(new_words)}")

add_word("мемчик")
add_word("трушний")
add_word("діджиталізація")
add_word("бандерштат")
add_word("мемчик")

print("Слова на 'м':", search_by_prefix("м"))
frequency_report()
