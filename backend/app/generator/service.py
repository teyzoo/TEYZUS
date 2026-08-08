import random
import re
from app.generator.categories import CATEGORIES
# Telegram username:
# - 5–32 символа
# - латинские буквы
# - цифры
# - underscore
USERNAME_PATTERN = re.compile(
    r"^[A-Za-z0-9_]{5,32}$"
)
def is_valid_username(
    username: str
) -> bool:
    if not username:
        return False
    return bool(
        USERNAME_PATTERN.fullmatch(
            username
        )
    )
def generate_username(
    length: int,
    numbers: bool = False,
    category: str = None
):
    # Telegram не принимает username
    # короче 5 символов.
    if length < 5:
        length = 5
    # Максимальная длина Telegram username.
    if length > 32:
        length = 32
    words = []
    if category:
        words = CATEGORIES.get(
            category,
            []
        )
    if not words:
        for value in CATEGORIES.values():
            words.extend(
                value
            )
    if not words:
        return []
    results = set()
    attempts = 0
    # Не даём бесконечный while,
    # если подходящих слов мало.
    max_attempts = 5000
    while (
        len(results) < 20
        and attempts < max_attempts
    ):
        attempts += 1
        word = str(
            random.choice(
                words
            )
        ).strip()
        # Оставляем только символы,
        # разрешённые Telegram.
        word = re.sub(
            r"[^A-Za-z0-9_]",
            "",
            word
        )
        if not word:
            continue
        if numbers:
            number = str(
                random.randint(
                    1,
                    999
                )
            )
            candidate = (
                word + number
            )
        else:
            candidate = word
        # ВАЖНО:
        # больше не обрезаем username
        # через [:length].
        #
        # Сначала приводим к нужной длине.
        if len(candidate) > length:
            continue
        if len(candidate) < length:
            remaining = (
                length - len(candidate)
            )
            # Если нужны цифры —
            # дополняем цифрами.
            if numbers:
                candidate += "".join(
                    random.choice(
                        "0123456789"
                    )
                    for _ in range(
                        remaining
                    )
                )
            else:
                # Без numbers дополняем
                # допустимыми буквами.
                candidate += "".join(
                    random.choice(
                        "abcdefghijklmnopqrstuvwxyz"
                    )
                    for _ in range(
                        remaining
                    )
                )
        # Финальная проверка.
        if not is_valid_username(
            candidate
        ):
            continue
        results.add(
            candidate
        )
    return list(
        results
    )
