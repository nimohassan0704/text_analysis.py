import nltk

# Загружаем текст для анализа
text = "The quick brown fox jumps over the lazy dog."

# Токенизируем текст
tokens = nltk.word_tokenize(text)

# Лемматизируем токены
lemmatizer = nltk.WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token) for token in tokens]

# Определяем части речи для токенов
pos_tags = nltk.pos_tag(tokens)

# Выводим результаты
print("Original text: ", text)
print("Tokens: ", tokens)
print("Lemmas: ", lemmas)
print("Part-of-speech tags: ", pos_tags)
