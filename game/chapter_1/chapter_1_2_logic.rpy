label chapter_1_2:
    scene bg corridor
    with dissolve


    $ c_show("smile")
    $ c_say("Смотри сколько кабинетов...")
    $ c_say("Можем заглянем в них")

    l "Хорошо, думаю осмотреть несколько"
    l "Но предлагаю не терять много времени."

    n "По левую сторону коридора красуется кабинет биологии"
    n "Несколько дальше лаборантская и женский туалет"
    n "По правую сторону кабинет кружка робототехники, гардероб и мужской туалет"

    $ visited_rooms = 0
    $ visited_biology = False
    $ visited_laboratory = False
    $ visited_women_toilet = False
    $ visited_robotics = False
    $ visited_wardrobe = False
    $ visited_men_toilet = False

    if companion == "shinna":
        $ max_rooms = 4
    else:
        $ max_rooms = 3

    while visited_rooms < max_rooms:
        scene bg corridor
        $ c_show("smile")

        menu:
            "Какой кабинет осмотреть?"

            "Кабинет биологии" if not visited_biology:
                $ visited_biology = True
                $ visited_rooms += 1
                call ch1_2_biology

            "Лаборантская" if not visited_laboratory:
                $ visited_laboratory = True
                $ visited_rooms += 1
                call ch1_2_laboratory

            "Женский туалет" if not visited_women_toilet:
                $ visited_women_toilet = True
                $ visited_rooms += 1
                call ch1_2_women_toilet

            "Кружок робототехники" if not visited_robotics:
                $ visited_robotics = True
                $ visited_rooms += 1
                call ch1_2_robotics

            "Гардероб" if not visited_wardrobe:
                $ visited_wardrobe = True
                $ visited_rooms += 1
                call ch1_2_wardrobe

            "Мужской туалет" if not visited_men_toilet:
                $ visited_men_toilet = True
                $ visited_rooms += 1
                call ch1_2_men_toilet

    call ch1_2_after_explore
    return
