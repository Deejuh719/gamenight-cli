def convert_to_snake_case(pascal_or_camel_cased_string):
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         converted_character = '_' + char.lower()
    #         snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    ask_for_input = input('Please Enter Your Own camelCased or PascalCased String: ')
    user_input = str(ask_for_input)
    print(f'User Input: {user_input} \nConverted: ',convert_to_snake_case(user_input))

if __name__ == '__main__':
    print('****convert_to_snake_case****')
    example = 'aLongAndComplexString'
    example_2 = 'APascalCasedString'
    print(f'Example Conversion: {example} \nConverted: ',convert_to_snake_case(example))
    print(f'Example Conversion: {example_2} \nConverted: ',convert_to_snake_case(example_2))
    main()