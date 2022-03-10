from tqdm import tqdm
from deep_translator import GoogleTranslator


def list_to_string(some_list):
    long_string = ''
    for elem in some_list:
        if elem == '':
            elem = '_empty'
        long_string = long_string + elem + '\n'
    return long_string[:-1]


def string_to_list(some_string):
    some_list = some_string.strip('\n').split('\n')
    new_list = []
    for elem in some_list:
        if elem == '_empty':
            elem = ''
        new_list.append(elem)
    return new_list


def split_list_by_char_len(some_list, max_len=3500):
    result = list()
    buff = list()
    char_len = 0
    for elem in some_list:
        elem_len = len(elem)
        if (char_len + elem_len) > max_len:
          result.append(buff)
          char_len = 0
          buff = []
        char_len = char_len + elem_len
        buff.append(elem)
    result.append(buff)
    return result


def translate_list(source_lang, some_list):
    translated_list = []
    batches = split_list_by_char_len(some_list)
    for batch in tqdm(batches):
        long_string = list_to_string(batch)
        translated_string = GoogleTranslator(source=source_lang, target='en').translate(text=long_string)
        translated_batch = string_to_list(translated_string)

        for elem in translated_batch:
            translated_list.append(elem)

    return translated_list


def list_translator(source_lang, list_of_words):
    print('Start of the text translation.')
    print('Number of words:', len(list_of_words))
    print('Source language:', source_lang)
    result = translate_list(source_lang, list_of_words)
    assert len(list_of_words) == len(result)

    assert_text   = 'Текст был переведен.'
    assert_result = GoogleTranslator(source='ru', target='en').translate(text=assert_text)
    assert assert_text != assert_result, 'Translator does not work. Change your IP.'
    print(assert_result)

    return result


if __name__ == "__main__":
    filename = '../txt/local_name_list.txt'

    with open(filename, encoding="utf-8") as f:
        words = f.read().splitlines()

    translated_words = list_translator('ru', words)

    print(words[:10])
    print(translated_words[:10])