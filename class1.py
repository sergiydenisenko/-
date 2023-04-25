import os

while True:
    # �������� ����������� ��� ���� �� �����
    filepath = input("Enter the file path: ")

    # ���������� �� ���� ����
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Try again...".format(filepath))
        continue

    # ³�������� ���� � ������ ���� �����
    with open(filepath) as file:
        lines = file.readlines()

    # ���������� ���������
    total_lines = len(lines)
    empty_lines = 0
    lines_with_z = 0
    z_count = 0
    lines_with_and = 0

    # ���������� ����������
    for line in lines:
        if line.strip() == "":
            empty_lines += 1
        if "z" in line:
            lines_with_z += 1
            z_count += line.count("z")
        if "and" in line:
            lines_with_and += 1

    # �������� ����������
    print("File: {}".format(filepath))
    print(" total lines: {}".format(total_lines))
    print(" empty lines: {}".format(empty_lines))
    print(" lines with \"z\": {}".format(lines_with_z))
    print(" \"z\" count: {}".format(z_count))
    print(" lines with \"and\": {}".format(lines_with_and))

    # ������ ����������� �� ���� �� ������������
    choice = input("Do you want to analyze another file? (y/n): ")
    if choice.lower() != "y":
        break




