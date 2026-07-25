label chapter_3_2:
    scene bg corridor
    with dissolve


    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ c_show("smile")

    call ch3_2_teachers_lounge

    return
