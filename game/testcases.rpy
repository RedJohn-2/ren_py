## Happy-path smoke tests for Storeroom Evil.
## Run with:  renpy.sh <project> test <suite::testcase>
## e.g.       renpy.sh . test smoke::start_to_menu


testsuite global:
    before testsuite:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    teardown:
        exit


testsuite smoke:

    setup:
        $ _test.timeout = 90.0
        $ _cb = renpy.test.testexecution.add_reached_label
        $ if _cb not in renpy.config.label_callbacks: renpy.config.label_callbacks.append(_cb)

    testcase start_to_menu:
        description "Start → dialogue → first menu → document reader"
        click "Начать" raw until screen "say"
        advance until screen "choice"
        click "Дебют Гроба" raw until screen "document_reader"
        assert screen "document_reader"


testsuite integrity:
    description "Static integrity checks (labels, items, routing)"

    setup:
        $ _test.timeout = 15.0

    testcase routing_labels_exist:
        description "All chapter labels wired in script.rpy are defined"
        $ expected = [
            "prologue_1", "prologue_2", "prologue_3", "prologue_4",
            "chapter_1_1", "chapter_1_2", "chapter_1_3", "chapter_1_4",
            "chapter_2_1", "chapter_2_2", "chapter_2_3", "chapter_2_4",
            "chapter_3_1", "chapter_3_2", "chapter_3_3", "chapter_3_4",
            "chapter_4_1", "chapter_explore_floor2", "chapter_4_2", "chapter_4_3",
            "demo_end",
        ]
        $ missing = [l for l in expected if not renpy.has_label(l)]
        assert eval "not missing"

    testcase sublabels_exist:
        description "Key event/logic sublabels referenced via call exist"
        $ subs = [
            "ch2_4_mask_assault", "ch2_4_rip_mask", "ch2_4_save_dialog", "ch2_4_death_dialog",
            "parry", "acquire_item",
        ]
        $ missing = [l for l in subs if not renpy.has_label(l)]
        assert eval "not missing"

    testcase items_registry_valid:
        description "Every ITEMS entry has the required name/img keys"
        $ bad = [k for k, v in ITEMS.items() if "name" not in v or "img" not in v]
        assert eval "not bad"

    testcase companions_and_masks_defined:
        description "Companions and core state helpers are defined in store"
        $ ok = bool(companion_chars) and callable(stat_add) and callable(set_companion) and callable(break_mask) and callable(leon_take_wound)
        assert eval "ok"
