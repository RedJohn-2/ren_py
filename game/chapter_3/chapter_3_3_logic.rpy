label chapter_3_3:
    scene bg teachers_lounge
    with dissolve


    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ c_show("smile")

    call ch3_3_firefight

    call ch3_3_scene2
    return
