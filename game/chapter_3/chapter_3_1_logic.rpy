label chapter_3_1:
    scene bg corridor
    with dissolve

    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ c_show("smile")

    l "[[Ну чтож...]"
    l "[[Похоже первый этаж почти полностью исследован...]"
    l "[[Кроме кабинета математики...]"
    n "..."
    l "[[А может не стоит терять время здесь...]"
    l "[[И продолжить поиски уже на втором этаже...]"
    l "[[Например в учительской!]"

    menu:
        "Отправиться в кабинет математики":
            call ch3_1_math

        "Отправиться на второй этаж":
            call ch3_1_teachers_lounge

    return
