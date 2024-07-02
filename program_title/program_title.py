def program_title(title):
    title_text = f"Welcome to {title}!"
    title_len = len(title_text) + 14
    space_before = "" if title_len > 45 else "      "
    print(f"\t{space_before}{"*" * title_len}")
    print(f"\t{space_before}*{" " * 6}{title_text}{" " * 6}*")
    print(f"\t{space_before}{"*" * title_len}", end="\n\n")

