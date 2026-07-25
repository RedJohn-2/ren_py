# Глава 2.3: Спортзал — логика
# Основан на файле "Диалоги/Глава 2.3.md"

label chapter_2_3:
    scene bg gym
    with dissolve


    if companion in companion_chars:
        $ companion_char = companion_chars[companion]
    else:
        $ set_companion("mari")
        $ companion_char = m

    $ c_show("smile")

    companion_char "Так..."
    companion_char "Я найду выключатель..."

    l "Погоди..."
    l "Может не будем торопиться?"
    l "Демоны могут быть где-то здесь..."

    companion_char "..."
    companion_char "Да, пожалуй ты прав..."
    companion_char "Хмм..."
    companion_char "Спортивный инвентарь должен быть где-то в кладовке..."
    companion_char "Также физрук любит что-то держать в своем кабинете!"
    companion_char "Может стоит заглянуть и туда..."

    call ch2_3_physed_office

    call ch2_3_storage_closet

    call ch2_3_women_locker

    return
