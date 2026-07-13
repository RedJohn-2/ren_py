# Глава 1.3: Основной поток
# Основан на файле "StoreRoomEvil/Диалоги/Глава 1.3.md"

label chapter_1_3:
    call ch1_3_guard_post

    call ch1_3_archive_pre

    if leon_strength >= 2:
        call ch1_3_book_fall_strong
    else:
        call ch1_3_book_fall_weak

    menu:
        "Давай я помогу тебе встать":
            call ch1_3_help_up
        "Давай я понесу тебя":
            call ch1_3_carry

    call ch1_3_archive_post

    call ch1_3_generator_room

    return
