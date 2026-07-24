# Chapter 2.2: Exploration logic
# Основан на файле "Диалоги/Глава 2.2.md"

label chapter_2_2:
    scene bg corridor
    with dissolve


    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ c_show("smile")

    companion_char "Леон, давай осмотрим эти кабинеты!"
    companion_char "Они нам по пути..."

    l "Хорошо"
    l "Только предлагаю лишний раз не шуметь."
    l "Демоны могут быть где-то поблизости..."

    n "В рекреации герои замечают кабинеты литературы,"
    n "музыки и черчения."
    n "Также неподалеку находится шваберная и мастерская."

    $ rooms_visited = 0
    $ _v_lit = False
    $ _v_mus = False
    $ _v_dra = False
    $ _v_jan = False
    $ _v_wor = False
    $ max_visits = 2
    if has_item('map_floor_1'):
        $ max_visits = 3

    while rooms_visited < max_visits:
        scene bg corridor
        $ c_show("smile")

        menu:
            "Кабинет литературы" if not _v_lit:
                $ _v_lit = True
                call ch2_2_literature
                $ rooms_visited += 1

            "Кабинет музыки" if not _v_mus:
                $ _v_mus = True
                call ch2_2_music
                $ rooms_visited += 1

            "Кабинет черчения" if not _v_dra:
                $ _v_dra = True
                call ch2_2_drafting
                $ rooms_visited += 1

            "Шваберная" if not _v_jan:
                $ _v_jan = True
                call ch2_2_janitor
                $ rooms_visited += 1

            "Мастерская" if not _v_wor:
                $ _v_wor = True
                call ch2_2_workshop
                $ rooms_visited += 1

    call ch2_2_continue
    return
