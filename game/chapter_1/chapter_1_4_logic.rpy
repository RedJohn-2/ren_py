# Глава 1.4: Основной поток битвы с демоном Генро
# Основан на файле "StoreRoomEvil/Диалоги/Глава 1.4.md"

label chapter_1_4:
    call ch1_4_scene1_gen_room
    call ch1_4_scene2_archive_with_genro

    if has_lamp:
        menu:
            "Кинуть лампу в левый силуэт":
                call ch1_4_throw_lamp_at_correct
            "Кинуть лампу в правый силуэт":
                call ch1_4_throw_lamp_at_wrong
                call ch1_4_no_lamp_fight_sequence
            "Кинуть лампу в центральный силуэт":
                call ch1_4_throw_lamp_at_wrong
                call ch1_4_no_lamp_fight_sequence
            "Кинуть лампу в задний силуэт":
                call ch1_4_throw_lamp_at_wrong
                call ch1_4_no_lamp_fight_sequence
    else:
        call ch1_4_no_lamp_fight_sequence

    call ch1_4_after_boss

    if girl_alive:
        call ch1_4_medbay
    else:
        n "Леон покидает подвал и отправляется на поиски девочек..."

    return


label ch1_4_no_lamp_fight_sequence:
    $ dodges_left = 2
    call ch1_4_no_lamp_choice_a
    call ch1_4_no_lamp_choice_b
    call ch1_4_mask_not_removed
    return
