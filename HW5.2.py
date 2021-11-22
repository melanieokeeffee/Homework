# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

# import sys
# with open('Lesson5/HW52.txt') as f:
#     text = f.readlines()
#     size = len(text)
# print(text)
# # количество строк
# print(size)

# with open('Lesson5/HW52.txt') as obj_file:



# with open("Lesson5/HW52.txt") as file_obj:
#     lines = 0
#     letters = 0
#     for line in file_obj:
#         lines += line.count("\n")
#         letters = len(line)-1
#         print(f"{letters} letters in line")
#     print(f"String count is {lines}")



# print(content)

def calculations(file_path):

    result = dict()
    line_number = 0
    try:
        with open(file_path, 'r') as f:
            for line_number, fl in enumerate(f, 1):
                result[line_number] = len(fl.split())
    except Exception as err:
        print(err)
    return line_number, result


if __name__ == '__main__':
    num, counts = calculations('Lesson5/HW52.txt')
    print(f'Found {num} line(s)')
    for k, v in counts.items():
        print(f'Line {k}: {v} word(s)')




