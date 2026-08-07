import re


USERNAME_PATTERN = re.compile(
    r"^[a-zA-Z0-9_]+$"
)


def normalize_username(value: str) -> str:
    value = value.strip()

    if value.startswith("@"):
        value = value[1:]

    return value.lower()


def validate_username(value: str) -> bool:
    if not 3 <= len(value) <= 32:
        return False

    return bool(USERNAME_PATTERN.fullmatch(value))


def generate_candidates(query: str) -> list[str]:
    query = normalize_username(query)

    candidates = [
        query,
        f"{query}ai",
        f"{query}hub",
        f"my{query}",
        f"{query}x"
    ]

    unique_candidates = []

    for candidate in candidates:
        if (
            validate_username(candidate)
            and candidate not in unique_candidates
        ):
            unique_candidates.append(candidate)

    return unique_candidates
