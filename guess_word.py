import random
import time

# Список слів
words = ["літо", "дощ", "школа", "робот", "панда", "пісня", "кава", "вікно", "кіт", "океан"]

# Вітання
print("Привіт! Це гра 'Вгадай слово' 🎮")
name = input("Як тебе звати? ")
print(f"Готова, {name}? Починаємо!")

time.sleep(1)  # невелика пауза

# Випадкове слово
word = random.choice(words)
guessed = ["_"] * len(word)
used_letters = []
tries = 6

print(f"\nЯ загадав слово з {len(word)} букв. У тебе є {tries} спроб.")

# Основний цикл гри
while tries > 0 and "_" in guessed:
    print("\nСлово:", " ".join(guessed))
    print("Використані літери:", ", ".join(used_letters) if used_letters else "немає")
    letter = input("Введи літеру: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Будь ласка, введи тільки одну українську літеру.")
        continue

    if letter in used_letters:
        print("Ти вже вводила цю літеру.")
        continue

    used_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("✅ Правильно!")
    else:
        tries -= 1
        print("❌ Неправильно. Спроб залишилось:", tries)

    time.sleep(0.5)  # маленька пауза після кожного ходу

# Після гри
print("\n📢 Результат гри:")

if "_" not in guessed:
    print("🎉 Ти виграла! Слово було:", word)
else:
    print("😢 Ти програла. Слово було:", word)

# Запропонувати повторити
play_again = input("\nХочеш зіграти ще раз? (так/ні): ").lower()
if play_again == "так":
    print("🔁 Просто запусти програму ще раз :)")
else:
    print(f"Дякую за гру, {name}! Гарного дня!")