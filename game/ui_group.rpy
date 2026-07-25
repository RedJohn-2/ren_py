style group_panel_frame:
    background Frame("#1a1a2ecc", 12, 12, 12, 12)
    padding (12, 8, 12, 8)

style group_stat_icon:
    xalign 0.5

style group_stat_num:
    xalign 0.5
    color "#ffffff"
    outlines [(2, "#000000cc", 0, 0)]
    size 26

style group_stat_num_max:
    xalign 0.5
    color "#ffe066"
    outlines [(2, "#000000cc", 0, 0)]
    size 26
    bold True

style group_member_name:
    color "#ffffff"
    outlines [(1, "#000000cc", 0, 0)]
    size 18

style group_member_num:
    xalign 0.5
    color "#c8c8d0"
    outlines [(1, "#000000cc", 0, 0)]
    size 20

style group_member_num_max:
    xalign 0.5
    color "#ffe066"
    outlines [(1, "#000000cc", 0, 0)]
    size 20
    bold True

style group_avatar_text:
    color "#ffffff"
    outlines [(2, "#000000cc", 0, 0)]
    size 24
    xalign 0.5
    yalign 0.5

style wounds_text:
    color "#ff5555"
    outlines [(2, "#000000cc", 0, 0)]
    size 22
    bold True


screen group_panel():
    zorder 50
    style_prefix "group"

    frame:
        id "group_panel"
        area (1340, 20, 560, 300)
        background None

        vbox:
            spacing 4

            frame:
                style "group_panel_frame"
                vbox:
                    spacing 6
                    hbox:
                        spacing 6
                        vbox:
                            xsize 96
                            if len(party) >= 2:
                                button:
                                    action ToggleVariable("_group_table_expanded", True, False)
                                    background Frame("#2a2a4acc", 8, 8, 8, 8)
                                    xsize 96
                                    ysize 64
                                    text "Группа" style "group_avatar_text"
                            else:
                                frame:
                                    background Frame("#2a2a4acc", 8, 8, 8, 8)
                                    xsize 96
                                    ysize 64
                                    text party_initials() style "group_avatar_text"

                        for stat in STAT_ORDER:
                            vbox:
                                xsize 84
                                add STAT_ICONS[stat] xzoom 0.075 yzoom 0.075 xalign 0.5
                                text str(group_stat(stat)) style "group_stat_num"

                    if _group_table_expanded and len(party) >= 2:
                        null height 4
                        for member in party:
                            hbox:
                                spacing 6
                                vbox:
                                    xsize 96
                                    text member_label(member) style "group_member_name"
                                for stat in STAT_ORDER:
                                    $ val = stat_get(member, stat)
                                    $ is_max = stat_get(member, stat) == group_stat(stat) and val > 0
                                    if is_max:
                                        text str(val) style "group_member_num_max"
                                    else:
                                        text str(val) style "group_member_num"

            frame:
                style "group_panel_frame"
                hbox:
                    spacing 8
                    text "Раны Леона:" style "wounds_text"
                    if leon_wound_limit() <= 0:
                        text "[leon_wounds] / 0  (штраф за рану)" style "wounds_text"
                    else:
                        text "[leon_wounds] / [leon_wound_limit()]" style "wounds_text"


init python:
    def party_initials():
        return "".join(_initial_of(m) for m in party[:4])

    def _initial_of(member):
        names = {
            'leon': 'Л', 'alice': 'А', 'mari': 'М',
            'shinna': 'Ш', 'helena': 'Х', 'sylvia': 'С',
        }
        return names.get(member, '?')

    def member_label(member):
        names = {
            'leon': 'Леон', 'alice': 'Алиса', 'mari': 'Мари',
            'shinna': 'Шинна', 'helena': 'Хелена', 'sylvia': 'Сильвия',
        }
        return names.get(member, member)
