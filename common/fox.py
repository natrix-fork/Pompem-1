
def format_to_json():
    with open("out.txt", "r", encoding="utf-8") as FILE:
        list_pompem = FILE.readlines()

    list_pompem = list(set(list_pompem))

    # def validate(qb: list):
    #     for i in range(len(qb)):
    #
    #         for x in range(1, len(qb)):
    #             if i == x:
    #                 del qb[x]
    #
    #
    # validate(list_pompem)
    for i in range(len(list_pompem)):
        if i + 1 < len(list_pompem):
            list_pompem[i] = list_pompem[i][:-1] + ',\n'

    with open("out.txt", "w", encoding="utf-8") as FILE:
        FILE.write('{\n')
        for i in list_pompem:
            FILE.write(i)
        FILE.write('}')
