define tv = Character('Телевизор', color="#aa66ff")
define legionnaire = Character('Легионер', color="#9a9a9a")

label ch3_3_firefight:
    $ c_show("worried")

    l "Как бы не превратиться в жаркое..."

    n "Леон пытается потушить шкаф..."
    n "Но быстро понимает, что это невозможно..."

    burai "Срррразись со мной, смерд..."

    n "Демон запускает еще один шар..."
    n "Леону едва удается увернуться..."

    l "Сперва бы разобраться с огнем..."
    l "Иначе школа сгорит дотла..."

    n "Пламя раздувается..."

    menu ch3_3_main_choice:
        "Использовать огнетушитель" if has_item('fire_extinguisher'):
            call ch3_3_extinguisher

        "Выбежать в коридор":
            call ch3_3_run

    return

label ch3_3_extinguisher:
    l "Огнетушитель!"
    l "[[Наконец-то пригодился!]"

    n "Леон достает Огнетушитель..."
    n "И начинает тушить пожар..."

    $ fire_extinguished = True
    return

label ch3_3_run:
    scene bg corridor
    with dissolve

    l "Нужно где-то найти воду..."
    l "На этаже должна быть подсобка уборщицы..."

    n "У Леона есть лишь несколько минут, прежде чем пламя выйдет из-под контроля..."
    n "Каждое действие отнимает драгоценное время..."

    $ fire_time = 0
    $ fire_limit = 300
    $ fire_extinguished = False
    $ _panel_done = False
    $ _v_women = False
    $ _v_men = False
    $ _v_cinema = False
    $ _v_stairs = False
    $ _v_janitor = False

    while not fire_extinguished and fire_time < fire_limit:
        scene bg corridor
        with dissolve

        $ _remaining = fire_limit - fire_time
        n "Пламя разрастается... У Леона осталось примерно [_remaining] секунд."

        menu ch3_3_explore_menu:
            "Посмотреть щиток" if not _panel_done:
                $ _panel_done = True
                call ch3_3_panel
                $ fire_time += 15

            "Женский туалет" if not _v_women:
                $ _v_women = True
                call ch3_3_women_toilet
                $ fire_time += 20

            "Мужской туалет" if not _v_men:
                $ _v_men = True
                call ch3_3_men_toilet

            "Комната киноклуба" if not _v_cinema:
                $ _v_cinema = True
                call ch3_3_cinema

            "Лестница B" if not _v_stairs:
                $ _v_stairs = True
                call ch3_3_stairs_b
                $ fire_time += 15

            "Подсобка уборщицы" if not _v_janitor:
                $ _v_janitor = True
                call ch3_3_janitor
                $ fire_time += 25

            "Осмотреть коридор":
                n "Леон медленно осматривается..."
                n "Драгоценное время уходит..."
                $ fire_time += 40

    if not fire_extinguished:
        call ch3_3_fire_fail

    return

label ch3_3_panel:
    l "Щиток..."
    l "Похоже, он подключен к датчику задымления в учительской..."

    if group_meets('intellect', 3):
        l "[[Похоже ничего сложного...]"

        n "Леон дергает штекер..."
        n "Из учительской раздается звук капающей воды..."
        n "Леон возвращается в Учительскую..."
        n "И видит, как пламя постепенно сходит на нет..."

        $ fire_extinguished = True
    else:
        l "Была бы Алиса здесь..."
        l "Лучше не рисковать и все же найти воду..."

    return

label ch3_3_women_toilet:
    scene bg women_toilet
    with dissolve

    l "Так..."
    l "Женский туалет..."
    l "Ни за что..."

    return

label ch3_3_men_toilet:
    scene bg men_toilet
    with dissolve

    n "Леон забегает в мужской туалет..."

    l "Так..."
    l "[[Вода есть...]"
    l "[[Но ведро...]"
    l "[[Думаю нужно отдышаться и прийти в себя...]"

    $ fire_time += 20

    n "Эмпатия Леона увеличена на 1."
    $ stat_add('leon','empathy',1)

    return

label ch3_3_cinema:
    n "Леон дергает ручку..."

    l "Открыто?"

    tv "Ахахаха..."
    tv "Наконец-то я смогу открыть врата!"

    l "Что?"
    l "Почему он работает?"
    l "Включался сам после перезагрузки?"

    menu ch3_3_cinema_choice:
        "Уйти":
            l "Нет на это времени..."
            l "Нужно торопиться..."
            $ fire_time += 10

        "Остаться посмотреть":
            l "[[Чтош, надеюсь недолго...]"
            $ fire_time += 60

            tv "Ну же братья мои..."
            tv "Явитесь в этот мир!"
            tv "Вместе мы поглотим этим бренные души..."

            n "Фигура из телевизора держит в одну руку какую-то книгу..."
            n "Другой рукой рисует непонятный силуэт в воздухе..."
            n "Вдруг ниоткуда появляется черная дыра..."

            tv "Вхахахах..."
            tv "Мы свободны..."
            tv "Ахаххаха..."

            n "Из дыры начинают вылетать какие-то темные сгустки..."
            n "Они постепенно принимают антропоморфные силуэты..."

            l "Жуть какая..."

            n "Мистика Леона увеличена на 1."
            $ stat_add('leon','mysticism',1)

    return

label ch3_3_stairs_b:
    n "Леон дергает ручку и открывает дверь..."

    l "Так..."
    l "Это лестница..."
    l "Еще рано покидать этаж..."

    return

label ch3_3_janitor:
    scene bg janitor
    with dissolve

    n "Леон аккуратно толкает дверь рукой..."

    l "Отлично!"
    l "Шваберная!"

    n "Леон включает кран и набирает воду в ведро..."
    n "..."

    l "Готово!"
    l "Осталось потушить пламя!"

    $ give_item('water')

    n "Леон возвращается в учительскую и начинает тушить пламя..."

    $ fire_extinguished = True
    return

label ch3_3_fire_fail:
    scene bg teachers_lounge
    with dissolve

    n "Пламя очень быстро распространяется..."
    n "И захватывает Леона в кольцо..."

    l "Я не успел..."
    l "Это конец?"
    l "Все пути отрезаны..."

    $ leon_take_wound()

    n "Но Леон чудом вырывается из огненного кольца..."
    n "Пламя удается сбить..."

    return

label ch3_3_scene2:
    scene bg teachers_lounge
    with dissolve

    $ c_show("worried")

    burai "Столько возни..."
    burai "Столько паники..."
    burai "И ради чего?.."
    burai "Потушить клочок земли?"
    burai "Зачем прилагать столько усилий, чтобы спасти это тленное место?"

    l "Может..."
    l "Потому что здесь мои друзья?"
    l "Они мне очень дороги..."
    l "Девушка..."
    l "Я не отступлю..."

    burai "Что ж..."
    burai "Давай я покажу тебе настоящих друзей..."
    burai "Преданных..."
    burai "Которые приходят на помощь!"

    n "Демон поднимает из сгоревшего пепла легионеров..."

    legionnaire "В боооооооооой!"

    return
