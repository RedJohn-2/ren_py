define ITEMS = {
    'kerosene_lamp':    {'name': 'Керосиновая лампа',       'img': 'item_kerosene_lamp'},
    'occult_diary':     {'name': 'Дневник о масках и демонах', 'img': 'item_occult_diary'},
    'map_floor_1':      {'name': 'Карта первого этажа',     'img': 'item_map_floor_1'},
    'map_floor_2':      {'name': 'Карта второго этажа',     'img': 'item_map_floor_2'},
    'mari_hairclip':    {'name': 'Заколка Мари',            'img': 'item_mari_hairclip'},
    'golf_club':        {'name': 'Клюшка для гольфа',       'img': 'item_golf_club'},
    'screwdriver':      {'name': 'Отвёртка',                'img': 'item_screwdriver'},
    'tesla_coil':       {'name': 'Катушка Теслы',           'img': 'item_tesla_coil'},
    'exorcism_potion':  {'name': 'Изгоняющее зелье',        'img': 'item_exorcism_potion'},
    'white_phosphorus': {'name': 'Белый фосфор',            'img': 'item_white_phosphorus'},
    'mercury':          {'name': 'Ртуть',                   'img': 'item_mercury'},
    'medkit':           {'name': 'Аптечка первой помощи',   'img': None},
    'fire_extinguisher':{'name': 'Огнетушитель',            'img': None},
    'lighter':          {'name': 'Зажигалка',               'img': None},
    'bat':              {'name': 'Бита',                    'img': None},
}

image item_kerosene_lamp    = "images/ui/items/kerosene_lamp.png"
image item_occult_diary     = "images/ui/items/occult_diary.png"
image item_map_floor_1      = "images/ui/items/map_floor_1.png"
image item_map_floor_2      = "images/ui/items/map_floor_2.png"
image item_mari_hairclip    = "images/ui/items/mari_hairclip.png"
image item_golf_club        = "images/ui/items/golf_club.png"
image item_screwdriver      = "images/ui/items/screwdriver.png"
image item_tesla_coil       = "images/ui/items/tesla_coil.png"
image item_exorcism_potion  = "images/ui/items/exorcism_potion.png"
image item_white_phosphorus = "images/ui/items/white_phosphorus.png"
image item_mercury          = "images/ui/items/mercury.png"


style item_notify_card:
    background Frame("#1a1a2ee8", 18, 18, 18, 18)
    padding (50, 36, 50, 36)

style item_notify_caption:
    color "#a8a8f0"
    size 22
    xalign 0.5

style item_notify_name:
    color "#ffffff"
    size 30
    bold True
    xalign 0.5


screen item_notification(item_id, item_name, item_img):
    zorder 90
    modal True

    button:
        xfill True
        yfill True
        action Return()
        background None

        vbox:
            align (0.5, 0.5)
            frame:
                style "item_notify_card"
                vbox:
                    xalign 0.5
                    if item_img:
                        add Transform(item_img, maxsize=(320, 320)) xalign 0.5
                        null height 16
                    text "Получен предмет" style "item_notify_caption"
                    null height 6
                    text item_name style "item_notify_name"

    timer 3.5 action Return()


label acquire_item(item_id, count=1):
    $ _was = inventory.get(item_id, 0)
    $ give_item(item_id, count)
    if _was <= 0:
        $ _info = ITEMS.get(item_id, {'name': item_id, 'img': None})
        $ _img = _info.get('img')
        call screen item_notification(item_id, _info['name'], _img)
    return
