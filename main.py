from lib.Castom_Classes import FlatIterator, FlatIterItems

def flat_generator(input_list):
    flat_list = FlatIterItems(input_list).list
    start = -1
    cursor = start
    end = len(flat_list)

    while cursor != end:
        yield flat_list[cursor]
        cursor += 1


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c',[233,22]],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print('\n', flat_list, '\n\n')

    for item in flat_generator(nested_list):
        print(item)
    