def format_score(value):

    if value is None:
        return "—"

    return f"{value}/10"



def format_price(
    minimum,
    maximum
):

    if minimum is None or maximum is None:
        return "Не рассчитано"

    return (
        f"${minimum:.0f}"
        f" - "
        f"${maximum:.0f}"
    )
