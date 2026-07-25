define DOC_BG = {
    'diary': 'doc_diary',
    'note': 'doc_note',
    'school_article': 'doc_school_article',
    'newspaper': 'doc_newspaper',
    'archive': 'doc_archive',
}

style doc_title_dark:
    color "#1a1a1a"
    size 34
    bold True
    xalign 0.5

style doc_title_light:
    color "#f2f6ff"
    size 34
    bold True
    xalign 0.5

style doc_body_dark:
    color "#222222"
    size 23
    line_leading 6
    line_spacing 6
    justify True

style doc_body_light:
    color "#e8edf7"
    size 23
    line_leading 6
    line_spacing 6
    justify True

style doc_close_button:
    background Frame("#3a3a5acc", 10, 10, 10, 10)
    hover_background Frame("#5a5a7acc", 10, 10, 10, 10)
    padding (18, 8, 18, 8)

style doc_close_button_text:
    color "#ffffff"
    size 22


screen document_reader(doc_bg, title, paragraphs, light_text=False):
    zorder 100
    modal True

    add Solid("#000000d8")

    fixed:
        align (0.5, 0.5)
        xsize 1500
        ysize 844
        add Transform(doc_bg, size=(1500, 844))

        viewport id "doc_vp":
            xsize 1280
            ysize 700
            align (0.5, 0.5)
            mousewheel True
            draggable True
            scrollbars "vertical"
            vbox:
                xsize 1200
                xalign 0.5
                if title:
                    if light_text:
                        text title style "doc_title_light"
                    else:
                        text title style "doc_title_dark"
                    null height 18
                for para in paragraphs:
                    if light_text:
                        text para style "doc_body_light"
                    else:
                        text para style "doc_body_dark"
                    null height 10

        textbutton "Закрыть":
            style "doc_close_button"
            align (0.985, 0.03)
            action Return()


label read_document(doc_type='note', title='', body=None, paragraphs=None):
    if paragraphs is None:
        if body is None:
            $ paragraphs = []
        else:
            $ paragraphs = [body]
    $ _doc_bg = DOC_BG.get(doc_type, 'doc_note')
    $ _doc_light = (doc_type == 'school_article')
    call screen document_reader(_doc_bg, title, paragraphs, _doc_light)
    return



