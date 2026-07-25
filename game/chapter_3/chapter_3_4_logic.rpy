label chapter_3_4:
    scene bg teachers_lounge
    with dissolve

    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ set_possessed(companion, 'burai')

    if companion in ('alice', 'mari', 'shinna'):
        $ show_companion_mask('burai')

    call ch3_4_legionnaire_spear
    call ch3_4_legionnaire_sword
    call ch3_4_legionnaire_mace
    call ch3_4_legionnaire_shield

    burai "Вра..."

    n "Девушка падает на колени..."

    l "[[Похоже, призыв воинов забирает у нее силы...]"
    l "[[Есть время поискать информацию в Дневнике...]"

    $ _diary_read = False
    $ _curtain_failed = False
    $ _fight_resolved = False

    while not _fight_resolved:
        menu:
            "Прочитать дневник" if has_item('occult_diary') and not _diary_read:
                call ch3_4_read_diary
                $ _diary_read = True

            "Включить кофемашину" if _diary_read:
                call ch3_4_coffee_machine

            "Вылить ведро воды" if has_item('water_bucket'):
                call ch3_4_water_bucket

            "Бросить бутылку спирта" if has_item('alcohol_bottle'):
                call ch3_4_alcohol_bottle

            "Накинуть занавеску" if not _diary_read and not _curtain_failed:
                call ch3_4_curtain

            "Напасть с битой":
                call ch3_4_attack_bat

    call ch3_4_continuation

    if girl_alive:
        call ch3_4_medbay

    $ clear_possessed()
    return
