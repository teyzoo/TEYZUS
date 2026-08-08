from pathlib import Path
from aiogram import Router
from aiogram.types import (
    Message,
    CallbackQuery,
    FSInputFile
)
from aiogram.fsm.context import FSMContext
from app.search_menu.keyboards import (
    search_modes,
    number_mode
)
from app.search_menu.search_runner import (
    run_search
)
from app.search_menu.check_runner import (
    run_check
)
from app.result_card.builder import (
    build_result_card
)
router = Router()
SEARCH_IMAGE = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "assets"
    / "search.png"
)
@router.message(
    lambda message: message.text == "🔎 Поиск"
)
async def open_search(
    message: Message
):
    await message.answer(
        "🔎 TEYZUS Search\n\n"
        "Выберите режим:",
        reply_markup=search_modes()
    )
@router.callback_query(
    lambda callback: callback.data in {
        "search_5",
        "search_6"
    }
)
async def choose_length(
    callback: CallbackQuery,
    state: FSMContext
):
    length = 5
    if callback.data == "search_6":
        length = 6
    await state.update_data(
        length=length
    )
    await callback.message.answer(
        "Выберите тип username:",
        reply_markup=number_mode()
    )
    await callback.answer()
@router.callback_query(
    lambda callback: callback.data in {
        "letters_only",
        "with_numbers"
    }
)
async def start_generation(
    callback: CallbackQuery,
    state: FSMContext
):
    data = await state.get_data()
    length = data.get(
        "length",
        5
    )
    numbers = (
        callback.data == "with_numbers"
    )
    await callback.answer()
    # ---------------------------------------------------------
    # Генерируем username
    # ---------------------------------------------------------
    usernames = await run_search(
        length=length,
        numbers=numbers
    )
    if not usernames:
        await callback.message.answer(
            "❌ Username не найдены."
        )
        await state.clear()
        return
    # ---------------------------------------------------------
    # Картинка поиска
    # ---------------------------------------------------------
    if SEARCH_IMAGE.exists():
        loading = await callback.message.answer_photo(
            photo=FSInputFile(
                SEARCH_IMAGE
            ),
            caption=(
                "Проверяю: "
                f"@{usernames[0]}"
            )
        )
    else:
        loading = await callback.message.answer(
            "Проверяю: "
            f"@{usernames[0]}"
        )
    # ---------------------------------------------------------
    # Проверяем username
    # ---------------------------------------------------------
    checked = []
    for index in range(
        0,
        len(usernames),
        20
    ):
        batch = usernames[
            index:index + 20
        ]
        # Показываем конкретный username,
        # который сейчас проверяется.
        if batch:
            current = batch[0]
            try:
                await loading.edit_caption(
                    caption=(
                        "Проверяю: "
                        f"@{current}"
                    )
                )
            except Exception:
                try:
                    await loading.edit_text(
                        text=(
                            "Проверяю: "
                            f"@{current}"
                        )
                    )
                except Exception:
                    pass
        results = await run_check(
            batch
        )
        checked.extend(
            results
        )
        # Если нашли реально свободный —
        # дальше проверять остальные нет смысла.
        available = next(
            (
                item
                for item in results
                if item.get(
                    "available"
                ) is True
            ),
            None
        )
        if available:
            checked = [
                available
            ]
            break
    # ---------------------------------------------------------
    # Нет результата
    # ---------------------------------------------------------
    if not checked:
        try:
            await loading.delete()
        except Exception:
            pass
        await callback.message.answer(
            "❌ Свободный username не найден."
        )
        await state.clear()
        return
    # ---------------------------------------------------------
    # Берём реально доступный username
    # ---------------------------------------------------------
    available_item = next(
        (
            item
            for item in checked
            if item.get(
                "available"
            ) is True
        ),
        None
    )
    if available_item is None:
        available_item = checked[0]
    username = available_item.get(
        "username",
        "unknown"
    )
    available = (
        available_item.get(
            "available",
            False
        )
    )
    # ---------------------------------------------------------
    # Карточка результата
    # ---------------------------------------------------------
    card, keyboard = build_result_card(
        username=username,
        available=available,
        score=9.5,
        price="$500-$700"
    )
    # Если сообщение было фотографией,
    # удаляем его и отправляем карточку отдельно.
    try:
        await loading.delete()
    except Exception:
        pass
    await callback.message.answer(
        card,
        reply_markup=keyboard
    )
    await state.clear()
