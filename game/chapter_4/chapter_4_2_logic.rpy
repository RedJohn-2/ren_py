label chapter_4_2:
    scene bg cafeteria
    with dissolve

    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ c_show("smile")

    if companion == "helena":
        call ch4_2_intro_helena
    else:
        call ch4_2_intro_girl
        call ch4_2_girl_hug

    call ch4_2_chef_taunt
    call ch4_2_mystic_insight
    call ch4_2_chef_rage

    if companion == "helena":
        call ch4_2_helena_potion
    else:
        n "Повар хватает тесак и бросается на героев..."
        n "От злости он хаотично размахивает тесаком, скидывая кастрюли и столовые приборы..."

    menu:
        "Что делать?"

        "Парировать":
            call ch4_2_fight_parry

        "Плеснуть зелье в лицо" if companion == "helena":
            call ch4_2_fight_potion

        "Бежать":
            call ch4_2_fight_flee

    call ch4_2_kara_reveal
    call ch4_2_kara_fight

    return
