from deep_translator import GoogleTranslator
import time

def calculate_time(start_time):
  seconds = time.time() - start_time
  print(f'{seconds} seconds')
  print(f'{(seconds / 60)} minutes')

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

def batches(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def translate_list(some_list, size):
    translated_list = []
    for batch in batches(some_list, size):
        long_string = list_to_string(batch)
        translated_string = GoogleTranslator(source='auto', target='en').translate(text=long_string)
        translated_batch = string_to_list(translated_string)

        for elem in translated_batch:
            translated_list.append(elem)
        
        time.sleep(2)

    return translated_list

def list_translator(list_of_words, size=200):
    print('Batch size ', size)
    print('Time for translation:')
    start_time = time.time()
    result = translate_list(list_of_words, size)
    calculate_time(start_time)

    assert_list   = ['Текст был переведен.']
    assert_result = translate_list(assert_list)
    assert assert_list != assert_result, 'Translator does not work. Change your IP.'
    print(assert_result[0])

    return result


if __name__ == "__main__":

    filename = 'words.txt'

    words = []
    with open(filename, encoding="utf-8") as f:
        words = f.read().splitlines()

    translated_words = list_translator(words)
    print(translated_words)