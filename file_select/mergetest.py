from Merge_resource import merge_resorce


class mergetest(merge_resorce):
    def __init__(self, merge1):
        super().__init__(merge1)


if __name__ == "__main__":
    mg = mergetest("csv_file/dummy.csv")