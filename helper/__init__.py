from typing import Tuple, NoReturn

import pandas as pd
import csv


def get_words(filename: str) -> list:
    data = pd.read_csv(filename)
    return list(data.bad_words.to_list())


def validate_word(filename: str, current_word: str) -> Tuple[bool, str]:
    words, file_words = current_word.split(' '), get_words(filename)

    if [v for v in file_words if v in current_word]:
        return True, 'Você digitou uma palavra proibida nesse canal!.'

    for word in words:
        if word in file_words:
            return True, 'O texto que você digitou contém uma palavra proibida nesse canal!.'

    return False, ''


def insert_word(filename: str, header: str, word: str) -> NoReturn:
    all_words = get_words(filename)

    if str(word) not in all_words:
        all_words.append(str(word))
        new_df = pd.DataFrame({header: all_words})
        new_df.to_csv(filename)
