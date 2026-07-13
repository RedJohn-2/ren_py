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

    return


label pro_4_search_first:
    while True:
        menu:
            "Осмотреть стол":
                call pro_4_search_desk

            "Осмотреть выдвижные ящики":
                call pro_4_search_drawers

            "Осмотреть подоконник":
                call pro_4_search_windowsill

        menu:
            "Продолжить поиски":
                pass

            "Хватит, ключа здесь нет":
                return


label pro_4_search_second:
    while True:
        menu:
            "Проверить плошки цветов":
                call pro_4_search_flowers

            "Осмотреть школьную доску":
                call pro_4_search_board

            "Заглянуть под коврик у входа":
                call pro_4_search_mat

        menu:
            "Продолжить поиски":
                pass

            "Здесь тоже ничего нет":
                return
