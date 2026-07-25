# Глава 2.4: Разрешение боя с Демоном Докуто
# Основан на файле "Диалоги/Глава 2.4.md"

label chapter_2_4:
    scene bg locker_room
    with dissolve

    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    if not possessed_girl:
        $ set_possessed(companion, 'dokuto')

    $ _ch2_4_toxins = []
    $ _ch2_4_balls_destroyed = False
    $ _ch2_4_net_failed = False
    $ _ch2_4_fight_resolved = False
    $ girl_alive = True
    $ mask_broken = False

    if companion in ('alice', 'mari', 'shinna'):
        $ show_companion_mask('dokuto')
    else:
        n "Леон оборачивается на девушку..."
        n "Лицо ее искажено зловещей маской Докуто..."

    call ch2_4_lizard_fight

    call ch2_4_claw_chase

    while not _ch2_4_fight_resolved:
        call ch2_4_mask_assault

    call ch2_4_after_victory

    if girl_alive:
        call ch2_4_medbay

    $ clear_possessed()
    return
