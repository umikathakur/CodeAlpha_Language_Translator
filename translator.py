from deep_translator import GoogleTranslator

print("===== LANGUAGE TRANSLATOR =====")

text = input("Enter text to translate: ")

print("\nLanguage Codes:")
print("hi = Hindi")
print("fr = French")
print("es = Spanish")
print("de = German")
print("ja = Japanese")

target_language = input("\nEnter target language code: ")

translated = GoogleTranslator(
    source='auto',
    target=target_language
).translate(text)

print("\nTranslated Text:")
print(translated)