import random
import webbrowser

print("Привіт! Це програма з кількома функціями.")

# Введення даних користувача
name = input("Введіть своє ім'я: ")
age = int(input("Введіть свій вік: "))

# --- ГРА: Вгадай число ---
print("\n🎯 Гра: Вгадай число (від 1 до 10)")
secret = random.randint(1, 10)
success = False

for attempt in range(1, 4):
    guess = int(input(f"Спроба {attempt}: "))
    if guess == secret:
        print("✅ Ви вгадали число!")
        success = True
        break
    else:
        print("❌ Невірно.")

if not success:
    print(f"Правильна відповідь була: {secret}")

# --- МАТЕМАТИЧНИЙ ТРЕНАЖЕР ---
print("\n🧠 Математичний тренажер")
score = 0

for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        correct = a + b
    elif op == "-":
        correct = a - b
    else:
        correct = a * b

    answer = int(input(f"{a} {op} {b} = "))
    if answer == correct:
        print("✅ Правильно!")
        score += 1
    else:
        print(f"❌ Неправильно. Правильна відповідь: {correct}")

print(f"Ваш результат: {score} з 5")

# --- HTML-ПРОФІЛЬ ---
print("\n📄 Створення HTML-профілю")
bio = input("Коротко опишіть себе: ")
color = input("Укажіть колір фону (наприклад: lightblue, pink, lightgreen): ")

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Профіль {name}</title>
    <style>
        body {{
            background-color: {color};
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }}
        h1 {{
            color: #333;
        }}
        p {{
            font-size: 20px;
        }}
        .box {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
            display: inline-block;
        }}
    </style>
</head>
<body>
    <div class="box">
        <h1>{name}</h1>
        <p>Вік: {age}</p>
        <p>Ваш бал у тренажері: {score} з 5</p>
        <p>{bio}</p>
    </div>
</body>
</html>
"""

with open("profile.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("\n✅ HTML-файл створено. Відкриваємо в браузері...")
webbrowser.open("profile.html")
