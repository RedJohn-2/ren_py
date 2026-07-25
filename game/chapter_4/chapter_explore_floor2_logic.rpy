label chapter_explore_floor2:
    scene bg corridor
    with dissolve

    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ c_show("smile")

    n "Леон выходит в длинный коридор второго этажа..."
    n "Ровный гул ламп под потолком. Вокруг ни души."

    $ _e_director = False
    $ _e_reception = False
    $ _e_psychologist = False
    $ _e_physics = False
    $ _e_women_toilet = False
    $ _e_men_toilet = False
    $ _e_chemistry = False
    $ _e_library = False
    $ _e_reading_room = False
    $ _e_lab_assistant = False
    $ _e_geography = False
    $ _e_journalism = False
    $ _e_informatics = False
    $ _e_rest_room = False
    $ _e_social_studies = False
    $ _e_janitor = False
    $ _e_history = False

    while True:
        scene bg corridor
        with dissolve
        $ c_show("smile")

        menu:
            "Куда направимся?"

            "Кабинет директора":
                call exp2_director

            "Приемная":
                call exp2_reception

            "Кабинет психолога":
                call exp2_psychologist

            "Кабинет физики":
                call exp2_physics

            "Женский туалет":
                call exp2_women_toilet

            "Мужской туалет":
                call exp2_men_toilet

            "Кабинет химии":
                call exp2_chemistry

            "Библиотека":
                call exp2_library

            "Читательский зал":
                call exp2_reading_room

            "Лаборантская":
                call exp2_lab_assistant

            "Кабинет географии":
                call exp2_geography

            "Кружок журналистики":
                call exp2_journalism

            "Кабинет информатики":
                call exp2_informatics

            "Комната отдыха":
                call exp2_rest_room

            "Кабинет обществознания":
                call exp2_social_studies

            "Подсобка уборщицы":
                call exp2_janitor

            "Кабинет истории":
                call exp2_history

            "→ Идти в столовую (продолжить)":
                n "Леон направляется к столовой..."
                return
