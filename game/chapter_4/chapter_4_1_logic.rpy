label chapter_4_1:
    scene bg corridor
    with dissolve

    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ c_show("smile")

    l "[[Пора продолжить поиски...]"

    call ch4_1_noise

    l "Какого черта?..."
    n "Похоже, это из столовой..."

    return
