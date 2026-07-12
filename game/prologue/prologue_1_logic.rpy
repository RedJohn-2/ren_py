# Пролог 1: Логика выбора
# Основан на файле "Диалоги/Пролог 1 Кабинет Школьного совета.md"

label prologue_1:
    call pro_1_meeting
    call pro_1_go_for_food
    call pro_1_assign_tasks
    call pro_1_article_choice
    call pro_1_finish_work

    jump prologue_2


label pro_1_article_choice:
    menu:
        "Выберите статью для проверки:"

        "«Спорт калечит — физкультура лечит» — важность безопасного спорта и анализ здоровья своего организма.":
            call pro_1_article_sport
            jump pro_1_article_after

        "«Дебют Гроба» — сильнейшее начало на шахматном турнире.":
            call pro_1_article_chess
            jump pro_1_article_after

        "«Легенда о бубновом валете» — призрак, вызываемый через экран монитора?":
            call pro_1_article_joker
            jump pro_1_article_after

        "«Второй мозг» — Как организовать хранение большого объема информации?":
            call pro_1_article_notes
            jump pro_1_article_after

        "«На одной волне» — Как музыка помогает человеку разобраться в себе?":
            call pro_1_article_music
            jump pro_1_article_after


label pro_1_article_after:
    menu:
        "Продолжить"

        "Выбрать другую статью":
            jump pro_1_article_choice

        "Вернуться к работе":
            return
