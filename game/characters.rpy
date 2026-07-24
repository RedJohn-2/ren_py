define s = Character('Шинна Кудо', color="#ff6b9d")
define a = Character('Алиса Тогаши', color="#6bc5ff")
define m = Character('Мари Аясэ', color="#ffb86b")
define l = Character('Леон Грей', color="#b8b8ff")
define n = Character(None, color="#ffffff")
define seller = Character('Продавец', color="#aaaaaa")

define h = Character('Хелена Куросава', color="#ff8c00")
define sy = Character('Сильвия Киба', color="#50c878")
define mk = Character('Микки', color="#da70d6")
define pred = Character('Предводитель', color="#ff0000")

define zombie = Character('Зомби', color="#556b2f")
define skeleton = Character('Скелет', color="#d4c5a9")
define genro = Character('Демон Генро', color="#ffd700")
define guard = Character('Охранник', color="#8b7355")
define girl_narrator = Character('???', color="#ffffff")

default girl_alive = True
default dodges_left = 0
default mask_broken = False

init python:
    companion_chars = {
        "shinna": s,
        "alice": a,
        "mari": m,
        "helena": h,
        "sylvia": sy,
    }

    def c_say(text):
        char = companion_chars.get(companion, n)
        char(text)
