"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных."""

# Пока не обрабатывает цифры в строке


def encode_rle(wip_text):
    str_code = ''
    prev_char = ''
    count = 1
    for char in wip_text:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            print(char.isdigit())
            prev_char = char
        else:
            print(char.isdigit())
            count += 1
    str_code += str(count) + prev_char
    with open('Task_Three_encoded', 'w') as data:
        data.write(str_code)
    return str_code


str_code = encode_rle("abbahuBbabuubaBabaBoooOoye1337")
print(str_code)

with open('Task_Three_encoded', 'r') as data:
    my_text2 = data.read()


def decoding_rle(wip_text: str):
    count = ''
    str_decode = ''
    for char in wip_text:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text2)
print(str_decode)