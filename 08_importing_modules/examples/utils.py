def normalize_item(text: str) -> str:
    return text.strip().lower()


def is_valid_item(item: str) -> bool:
    return item in ("tea", "coffee")

