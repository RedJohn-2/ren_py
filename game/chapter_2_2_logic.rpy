# Chapter 2.2: Exploration logic
# Основан на файле "Диалоги/Глава 2.2.md"

init python:
    companion_chars = {
        "mari": m,
        "alice": a,
        "shinna": s,
        "sylvia": sy,
        "helena": h,
    }

label chapter_2_2:
    scene bg corridor
    with dissolve

    n "Локация: Коридор"

    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ companion = "mari"
        $ companion_char = m

    show expression companion + " smile"

    companion_char "Леон, давай осмотрим эти кабинеты!"
    companion_char "Они нам по пути..."

    l "Хорошо"
    l "Только предлагаю лишний раз не шуметь."
    l "Демоны могут быть где-то поблизости..."

    n "В рекреации герои замечают кабинеты литературы,"
    n "музыки и черчения."
    n "Также неподалеку находится шваберная и мастерская."

    $ rooms_visited = 0
    $ max_visits = 2
    if has_map:
        $ max_visits = 3

    label ch2_2_explore_loop:
        if rooms_visited >= max_visits:
            n "Вы осмотрели все, что могли в этот заход."
            jump ch2_2_continue

        menu:
            "Кабинет литературы":
                call ch2_2_literature
                $ rooms_visited += 1
                jump ch2_2_explore_loop

            "Кабинет музыки":
                call ch2_2_music
                $ rooms_visited += 1
                jump ch2_2_explore_loop

            "Кабинет черчения":
                call ch2_2_drafting
                $ rooms_visited += 1
                jump ch2_2_explore_loop

            "Шваберная":
                call ch2_2_janitor
                $ rooms_visited += 1
                jump ch2_2_explore_loop

            "Мастерская":
                call ch2_2_workshop
                $ rooms_visited += 1
                jump ch2_2_explore_loop

            "Продолжить путь":
                jump ch2_2_continue
