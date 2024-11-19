from pprint import pprint

def custom_write(file_name, strings):
     file_name = 'test.txt'
     file = open(file_name, 'w', encoding= 'utf-8')
     strings_positions = {}
     str_num = 0
     str_start_byte = file.seek(0)
     for string_ in  strings:
         file.write(string_ + '\n')
         str_num +=1
         key = (str_num, str_start_byte)
         strings_positions[key]= string_
         str_start_byte = file.tell()
     file.close()
     return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


