# Механика парирования: timed-choice меню, исчезает по таймеру.
# timeout = фикс. база + Сила Леона. Клик мимо кнопки = промах.

init python:
    def parry_timeout(base=2.5, per_strength=0.5):
        return base + char_stats['leon']['strength'] * per_strength


transform parry_bar_shrink(timeout):
    on show:
        xzoom 1.0
        linear timeout xzoom 0.0


screen parry_choice(items, prompt="", timeout=None, hint="ПАРИРОВАНИЕ"):
    if timeout is None:
        $ timeout = parry_timeout()

    timer timeout action Return("__miss__")

    button:
        xfill True
        yfill True
        background Solid("#00000099")
        action Return("__miss__")

    vbox:
        align (0.5, 0.72)
        spacing 14

        if hint:
            text hint:
                xalign 0.5
                size 28
                color "#ff5555"
                outlines [(2, "#000000", 0, 0)]

        if prompt:
            text prompt:
                xalign 0.5
                size 24
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]

        fixed:
            xalign 0.5
            xsize 460
            ysize 12
            fit_first True
            add Solid("#3a1010"):
                xsize 460
                ysize 12
            add Solid("#e23b3b"):
                xanchor 0.0
                xpos 0
                ysize 12
                xsize 460
                at parry_bar_shrink(timeout)

        hbox:
            xalign 0.5
            spacing 20
            for cap, val in items:
                textbutton cap:
                    text_size 26
                    action Return(val)


label parry(items, prompt="", timeout=0.0, hint="ПАРИРОВАНИЕ"):
    python:
        if timeout is None or timeout <= 0:
            timeout = parry_timeout()
        _parry = renpy.call_screen("parry_choice", items=items, prompt=prompt, timeout=timeout, hint=hint)
    return _parry
