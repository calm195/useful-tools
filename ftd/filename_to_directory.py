import os
import shutil


def get_filenames_to_list_without_postfix_from(the_dir):
    return remove_postfix_from_filenames_list(get_filenames_to_list_from(the_dir))


def get_filenames_to_list_from(the_dir):
    filenames = os.listdir(the_dir)
    temp_list = []
    for filename in filenames:
        if os.path.isfile(os.path.join(the_dir, filename)):
            temp_list.append(filename)
    return temp_list


def remove_postfix_from_filenames_list(filenames):
    temp_list = []
    for filename in filenames:
        temp_list.append(remove_postfix_from_filename(filename))
    return temp_list


def remove_postfix_from_filename(filename):
    return filename[:filename.rfind('.')]


def get_directory_from_filename_list(filenames):
    target_dict = {}
    for filename in filename_list:
        split_list = filename.split('_')
        if split_list[1] == 'kit':
            temp = split_list[0]
            split_list[0] = split_list[1]
            split_list[1] = temp
        if split_list[0] not in target_dict:
            target_dict[split_list[0]] = []
        target_dict[split_list[0]].append(split_list[1])
    return target_dict


def split_filenames_to_directories(the_dir, filename_dict):
    for key in filename_dict.keys():
        if not os.path.exists(os.path.join(the_dir, key)):
            os.mkdir(os.path.join(the_dir, key))
        for value in filename_dict[key]:
            if key == 'kit':
                shutil.copyfile(os.path.join(
                    the_dir, value + '_' + key + '.md'),
                    os.path.join(the_dir, key + '/' + value + '.md'))
            else:
                shutil.copytree()
                shutil.copyfile(os.path.join(
                    the_dir, key + '_' + value + '.md'),
                    os.path.join(the_dir, key + '/' + value + '.md'))


test_dir = "D:\\Downloads\\learning-docs"
print(get_filenames_to_list_from(test_dir))
filename_list = get_filenames_to_list_without_postfix_from(test_dir)
filenames_dict = get_directory_from_filename_list(filename_list)
split_filenames_to_directories(test_dir, filenames_dict)
