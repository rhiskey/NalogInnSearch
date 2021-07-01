import logging
import os
from sys import exit


def get_inn_list_from_file(filename):
    content = []
    path = os.path.realpath(filename)
    try:
        f = open(path, 'rt')
        content = f.readlines()
    except Exception as e:
        logging.exception("Input file exception")
        exit(3)
    except FileNotFoundError:
        logging.exception('File not found: %s', filename)
        exit(4)
    finally:
        f.close()

    # remove elem if only '\n'
    l1 = [s for s in content if s != '\n']

    # remove last \n in each content element: '1234567\n'
    l2 = []
    for elem in l1:
        elem = elem.replace("\n", "")
        if elem != '000000000000' and elem != '0000000000':
            l2.append(elem)

    content = l2
    return content


# # Debug
# if __name__ == '__main__':
#    get_inn_list_from_file('C:\\naloginn\\innall.txt')
