import random
import re

from app.generator.categories import CATEGORIES


USERNAME_PATTERN = re.compile(
    r"^[A-Za-z][A-Za-z0-9_]{4,31}$"
)

READABLE_SUFFIXES = [
    "ai",
    "app",
    "hub",
    "lab",
    "go",
    "pro",
    "x",
]

READABLE_PREFIXES = [
    "my",
    "go",
    "get",
    "use",
    "the",
]


def is_valid_username(username: str) -> bool:
    if not username:
        return False

    return bool(
        USERNAME_PATTERN.fullmatch(username)
    )


def _clean_word(value: str) -> str:
    return re.sub(
        r"[^A-Za-z0-9]",
        "",
        str(value).strip()
    )


def _build_candidates(
    word: str,
    length: int,
    numbers: bool
) -> list[str]:

    candidates = []

    word = _clean_word(word)

    if not word:
        return candidates

    # Само слово
    if len(word) == length:
        candidates.append(word)

    # Слово + осмысленный суффикс
    for suffix in READABLE_SUFFIXES:
        candidate = word + suffix

        if len(candidate) == length:
            candidates.append(candidate)

    # Осмысленный префикс + слово
    for prefix in READABLE_PREFIXES:
        candidate = prefix + word

        if len(candidate) == length:
            candidates.append(candidate)

    # Только если пользователь разрешил цифры:
    # добавляем цифры в конец, но НЕ случайные буквы.
    if numbers and len(word) < length:
        remaining = length - len(word)

        if remaining <= 3:
            for _ in range(5):
                digits = "".join(
                    random.choice("0123456789")
                    for _ in range(remaining)
                )

                candidates.append(
                    word + digits
                )

    return candidates


def generate_username(
    length: int,
    numbers: bool = False,
    category: str | None = None
):
    if length < 5:
        length = 5

    if length > 32:
        length = 32

    words = []

    if category:
        words.extend(
            CATEGORIES.get(category, [])
        )

    if not words:
        for values in CATEGORIES.values():
            words.extend(values)

    if not words:
        return []

    results = set()

    # Берём достаточно много попыток,
    # но никогда не дописываем случайные буквы.
    for _ in range(10000):

        word = random.choice(words)

        candidates = _build_candidates(
            word=word,
            length=length,
            numbers=numbers
        )

        for candidate in candidates:

            if not is_valid_username(candidate):
                continue

            if len(candidate) != length:
                continue

            results.add(candidate)

            if len(results) >= 20:
                break

        if len(results) >= 20:
            break

    return list(results)
