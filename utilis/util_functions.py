def save_to_file(name: str) -> None:
    with open('names.txt', 'a') as f:
        f.write(name + '\n')