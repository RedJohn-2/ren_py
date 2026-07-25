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
    $ _s1_desk = False
    $ _s1_drawers = False
    $ _s1_win = False
    while not (_s1_desk and _s1_drawers and _s1_win):
        menu:
            "Осмотреть стол" if not _s1_desk:
                $ _s1_desk = True
                call pro_4_search_desk

            "Осмотреть выдвижные ящики" if not _s1_drawers:
                $ _s1_drawers = True
                call pro_4_search_drawers

            "Осмотреть подоконник" if not _s1_win:
                $ _s1_win = True
                call pro_4_search_windowsill
    return


label pro_4_search_second:
    $ _s2_flowers = False
    $ _s2_board = False
    $ _s2_mat = False
    while not (_s2_flowers and _s2_board and _s2_mat):
        menu:
            "Проверить плошки цветов" if not _s2_flowers:
                $ _s2_flowers = True
                call pro_4_search_flowers

            "Осмотреть школьную доску" if not _s2_board:
                $ _s2_board = True
                call pro_4_search_board

            "Заглянуть под коврик у входа" if not _s2_mat:
                $ _s2_mat = True
                call pro_4_search_mat
    return
