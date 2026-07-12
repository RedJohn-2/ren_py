define s = Character('Шинна Кудо', color="#ff6b9d")
define a = Character('Алиса Тогаши', color="#6bc5ff")
define m = Character('Мари Аясэ', color="#ffb86b")
define l = Character('Леон Грей', color="#b8b8ff")
define n = Character(None, color="#ffffff")
define seller = Character('Продавец', color="#aaaaaa")

default leon_strength = 0
default leon_intellect = 0
default leon_mystic = 0
default leon_organization = 0
default leon_empathy = 0

define h = Character('Хелена Куросава', color="#ff8c00")
define sy = Character('Сильвия Киба', color="#50c878")
define mk = Character('Микки', color="#da70d6")
define pred = Character('Предводитель', color="#ff0000")

define zombie = Character('Зомби', color="#556b2f")
define skeleton = Character('Скелет', color="#d4c5a9")
define genro = Character('Демон Генро', color="#ffd700")
define guard = Character('Охранник', color="#8b7355")
define girl_narrator = Character('???', color="#ffffff")

default companion = None
default has_lamp = False
default has_diary = False
default has_map = False
default has_medkit = False
default has_fire_extinguisher = False
default has_key = False
default girl_alive = True
default leon_injured = False
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

    companion_sprites = {
        "shinna": {
            "smile": "shinna smile",
            "frown": "shinna frown",
            "closed_smile": "shinna closed smile",
            "closed_frown": "shinna closed frown",
        },
        "alice": {
            "smile": "alice smile",
            "frown": "alice frown",
            "closed_smile": "alice closed smile",
            "closed_frown": "alice closed frown",
        },
        "mari": {
            "smile": "mari smile",
            "frown": "mari frown",
            "closed_smile": "mari smile eyesclosed",
            "closed_frown": "mari frown eyesclosed",
        },
        "helena": {
            "smile": "helena smile",
            "frown": "helena frown",
            "closed_smile": "helena smile closedeyes",
            "closed_frown": "helena frown closedeyes",
        },
        "sylvia": {
            "smile": "sylvia smile",
            "frown": "sylvia frown",
            "closed_smile": "sylvia closed smile",
            "closed_frown": "sylvia closed frown",
        },
    }

    def c_show(emotion="smile"):
        if not companion:
            return
        emap = companion_sprites.get(companion)
        if not emap:
            return
        img = emap.get(emotion)
        if img:
            renpy.show(img)
