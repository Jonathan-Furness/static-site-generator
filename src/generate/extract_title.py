import re


def extract_title(markdown: str) -> str:
    title_pattern = r"(^#{1}\W*.*)"
    raw_title: list[str] = re.findall(title_pattern, markdown)

    if not raw_title:
        raise ValueError("Title is missing")

    substitute_pattern = r"(^#{1}\W*)"
    return re.sub(substitute_pattern, "", raw_title[0].strip())
