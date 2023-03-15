import sys
import sqlite3

# указываем где находиться classes.py, чтобы успешно импортировать
sys.path.append(r"C:\Users\todor\OneDrive\Рабочий стол\Gamedev и программирование (1)\Github\Python\Python_text_rpg_game\TextRPG")

import classes

# создаем базу данных
db = sqlite3.connect("Python_text_rpg_game/TextRPG/db/rpg.db")
cursor = db.cursor()

# создаем таблицу оружик
cursor.execute("""
    CREATE TABLE IF NOT EXISTS weapon(
        id INT PRIMARY KEY,
        name TEXT,
        description TEXT,
        attack_power INT
    )
""")