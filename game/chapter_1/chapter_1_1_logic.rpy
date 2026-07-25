# Глава 1.1: Логика выбора
# Основана на файле "Диалоги/Глава 1.1.md"

label chapter_1_1:
    scene bg storage_room
    with dissolve


    n "В полной темноте Леон лишь слышит визги девушек."
    n "С некоторыми из них он сталкивается плечами."
    n "Леон не понимал, кому помочь первым."

    l "Постой!"
    l "Шинна!"
    l "Алиса..."

    n "Тишина..."

    menu:
        "Выбежать в коридор, попытаться остановить девочек":
            $ set_companion(renpy.random.choice(['alice', 'mari', 'shinna']))
            call ch1_1_run_to_corridor

        "Не паниковать, остаться в подсобке":
            $ set_companion('sylvia')
            call ch1_1_stay_in_storage

    call ch1_1_unite

    return
