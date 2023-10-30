
# string = input("Введите строку: ")
#

# string = ''.join(ch for ch in string if ch.isalnum())
#
#
# string = string.lower()
#
#
# if string == string[::-1]:
#     print("Введенная строка является палиндромом.")
# else:
#     print("Введенная строка не является палиндромом.")


# text = input("Введите текст: ")
#
#
# reserved_words = input("Введите список зарезервированных слов (через запятую): ").split(',')
#
#
# for word in reserved_words:
#
#     occurrences = text.lower().count(word.lower())
#
#
#     text = text.replace(word, word.upper())
#
#
# print("Измененный текст:")
# print(text)



# text = input("Введите текст: ")
#
#
# sentences = text.split('. ')
#
#
# num_sentences = len(sentences)
#
#
# print(f"Количество предложений: {num_sentences}")