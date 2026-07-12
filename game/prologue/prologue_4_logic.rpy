# Пролог 4: Логика
# Основан на файле "Диалоги/Пролог 4 Актовый зал.md"

label prologue_4:
    call pro_4_assembly_setup
    call pro_4_theater_intro

    call pro_4_search_first

    n "Шинна молча посмотрела на Леона."
    n "Очень молча."
    n "Леон решил проверить менее очевидные места."

    call pro_4_search_second
    call pro_4_theater_outro
    call pro_4_assembly_lockpick
    call pro_4_storage_room

    jump chapter_1_1


label pro_4_search_first:
    menu:
        "Осмотреть стол":
            call pro_4_search_desk
            jump pro_4_search_first_check

        "Осмотреть выдвижные ящики":
            call pro_4_search_drawers
            jump pro_4_search_first_check

        "Осмотреть подоконник":
            call pro_4_search_windowsill
            jump pro_4_search_first_check


label pro_4_search_first_check:
    menu:
        "Продолжить поиски":
            jump pro_4_search_first

        "Хватит, ключа здесь нет":
            return


label pro_4_search_second:
    menu:
        "Проверить плошки цветов":
            call pro_4_search_flowers
            jump pro_4_search_second_check

        "Осмотреть школьную доску":
            call pro_4_search_board
            jump pro_4_search_second_check

        "Заглянуть под коврик у входа":
            call pro_4_search_mat
            jump pro_4_search_second_check


label pro_4_search_second_check:
    menu:
        "Продолжить поиски":
            jump pro_4_search_second

        "Здесь тоже ничего нет":
            return
