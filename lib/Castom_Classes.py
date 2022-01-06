class FlatIterItems:
    def __init__(self, input_list):
        self.list = self._merge_list(input_list)

    # метод для создания плоского списка через рекурсию
    def _merge_list(self, inp_list):
        result = []
        for elem in inp_list:
            result += self._merge_list(elem) if isinstance(elem, list) else [elem]
        return result


class FlatIterator:
    def __init__(self, input_list):
        self.list = FlatIterItems(input_list).list

    def __iter__(self):
        self.cursor = -1
        return self
    
    def __next__(self):
        if self.cursor == len(self.list) - 1:
            raise StopIteration
        self.cursor += 1
        return self.list[self.cursor]
