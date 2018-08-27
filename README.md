Function returns a correct plural form of a word for a num.

Based on https://habr.com/post/105428/.
Tested only with russian language.

Example:
```
records_count = 21
record_forms = ['сообщение', 'сообщения', 'сообщений']
new_forms = ['новое', 'новых', 'новых']
print('У вас {} {} {}'.format(
    records_count, 
    plural_for_num(records_count, new_forms), 
    plural_for_num(records_count, record_forms))
)
```
