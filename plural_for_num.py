def plural_for_num(num, word_forms):
    """
    Function returns a correct plural form of a word for a num.

    Based on https://habr.com/post/105428/.
    Tested only with russian language.

    Args:
        num (int): A number that precedes a word
        word_forms (list): A list that contains 3 plural forms of a word

    Returns:
        string: a correct form on a word for the num

    Example:
        records_count = 21
        record_forms = ['сообщение', 'сообщения', 'сообщений']
        new_forms = ['новое', 'новых', 'новых']
        print('У вас {} {} {}'.format(
            records_count, 
            plural_for_num(records_count, new_forms), 
            plural_for_num(records_count, record_forms))
        )
    """
    num = num % 100
    if 11 <= num <= 19:
        result = word_forms[2]
    else:
        num = num % 10
        endings = {
            1: word_forms[0],
            2: word_forms[1],
            3: word_forms[1],
            4: word_forms[1],
        }
        result = endings.get(num)
        if result is None:
            result = word_forms[2]
    return result
