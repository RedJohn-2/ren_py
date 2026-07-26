image bg wide_panorama = Composite(
    (3840, 1080),
    (0, 0), Transform("images/bg/corridor.jpg", xsize=1920, ysize=1080, fit="fill"),
    (1920, 0), Transform("images/bg/gym.jpg", xsize=1920, ysize=1080, fit="fill"),
)


transform pan_hold(x=0):
    crop (x, 0, 1920, 1080)


transform pan_scan(x_from, x_to, duration=5.0):
    crop (x_from, 0, 1920, 1080)
    linear duration crop (x_to, 0, 1920, 1080)


screen panorama_explore():
    viewport:
        xsize 1920
        ysize 1080
        draggable True
        edgescroll (200, 600)
        add "bg wide_panorama"

    textbutton _("Продолжить"):
        xalign 0.5
        yalign 0.95
        action Return()


init python:
    import pygame

    def keyboard_pan_tick(adj, speed=20):
        pressed = pygame.key.get_pressed()
        dx = 0
        if pressed[pygame.K_a]:
            dx -= speed
        if pressed[pygame.K_d]:
            dx += speed
        if dx == 0:
            return
        rng = adj.range
        if not rng:
            return
        new_v = adj.value + dx
        if new_v < 0:
            new_v = 0
        elif new_v > rng:
            new_v = rng
        adj.change(new_v)


screen keyboard_panorama():
    default adj = ui.adjustment(range=1920, value=0, adjustable=True)

    viewport:
        xsize 1920
        ysize 1080
        xadjustment adj
        draggable True
        edgescroll (200, 600)
        add "bg wide_panorama"

    timer 0.02 repeat True action Function(keyboard_pan_tick, adj)

    text _("Зажмите Ф (A) — влево, В (D) — вправо"):
        xalign 0.5
        yalign 0.05
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]

    textbutton _("Продолжить"):
        xalign 0.5
        yalign 0.95
        action Return()


label demo_panorama:
    scene bg wide_panorama at pan_hold(0)
    with dissolve

    n "Это широкая панорама — два фона, склеенных в один холст 3840×1080."
    n "Сейчас видно только левую половину (коридор). Шов спрятан за правым краем экрана."

    show bg wide_panorama at pan_scan(0, 1920, 6.0)
    n "Запускаем функцию поворота — pan_scan плавно сдвигает окно просмотра вправо..."
    n "Мы пересекли шов между двумя изображениями."
    n "Теперь на экране правая половина (спортзал)."

    show bg wide_panorama at pan_hold(1920)
    n "Можно зафиксировать вид на любом участке через pan_hold(x)."

    show bg wide_panorama at pan_scan(1920, 0, 6.0)
    n "И так же вернуть камеру обратно — pan_scan с теми же координатами в обратную сторону."

    show bg wide_panorama at pan_hold(0)

    n "А теперь — интерактивный режим: перетаскивайте фон мышью или подведите курсор к краям."
    call screen panorama_explore

    n "Теперь управление с клавиатуры: зажмите Ф (A) для поворота влево и В (D) для поворота вправо."
    call screen keyboard_panorama

    scene black with dissolve
    n "Демонстрация панорамы завершена."
    return
