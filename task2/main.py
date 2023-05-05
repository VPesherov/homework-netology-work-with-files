import os


def get_directory_with_text_files(folder):
    return os.path.join(os.getcwd(), folder)


def get_count_line_in_file(file_name):
    with open(file_name[0], 'rt', encoding='UTF-8') as file:
        count = 0
        for line in file:
            count += 1

    return count


def files_by_line_length(file_names):
    count_line_dict = {}
    for file_name in file_names:
        line_in_file = get_count_line_in_file(file_name)
        count_line_dict[line_in_file] = file_name
    count_line_dict = dict(sorted(count_line_dict.items()))

    # count_line_list = []
    #
    # for value in count_line_dict.values():
    #     count_line_list.append(value)

    return count_line_dict


def main():
    folder = 'text-files'
    path = get_directory_with_text_files(folder)
    txt_files = []
    for file_name in os.listdir(path):  #
        if file_name.endswith('.txt'):
            relative_path = os.path.join(folder, file_name)
            txt_files.append((relative_path, file_name))
            # with open(os.path.join(folder, file_name), 'rt', encoding='UTF-8') as file:
            #     print(file.read())

    count_line_dict = files_by_line_length(txt_files)

    if os.path.exists(os.path.join(os.getcwd(), 'result_file.txt')):
        create_file = open('result_file.txt', 'wt')
        create_file.close()

    count_of_files = 0

    for key, value in count_line_dict.items():
        count_of_files += 1
        with open('result_file.txt', 'at', encoding='UTF-8') as file_output, open(value[0], 'rt', encoding='UTF-8') as file_input:
            file_output.write(value[1] + '\n')
            file_output.write(str(key) + '\n')
            number_line = 0
            for line in file_input:
                number_line += 1
                res_string = f'Строка номер {number_line} файла номер {count_of_files}'
                file_output.write(res_string + '\n')
                file_output.write(line)
            #file_output.write(value[1])
            file_output.write('\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
