def fake_data(rows: int = 10) -> None:
    values_str = ''
    for i in range(rows):
        first_name_nonbinary = fake.first_name_nonbinary()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80)
        values_str += f'"{first_name_nonbinary}": "{date_of_birth}"'
        if (i + 1) < rows:
            values_str += ', '
    print(values_str)
def task_1() -> None:
    my_dict = {"Илья": "31-05-2001", "Ксения": "24-04-2003", "Славик": "08-12-1997", "Александр": "20.04.2000",
    "Мирон": "23-03-2003", "Миша": "12-12-2002",}
    print(f'Dict: {my_dict}')
    print(f'Existing value: {my_dict["Мирон"]}')
    print(f'Not existing value: {my_dict.get("Александр")}')
    my_dict.update({"Алина": "19-03-1999", "Валерий": "12-07-1998"})
    print(f'Modified dictionary: {my_dict}')
    get_person = my_dict.pop('Славик')
    print(f'Deleted value: {get_person}')
    print(f'Final change: {my_dict}')


def task_2() -> None:
    my_set = {1, 'Яблоко' , 42.314,}
    print(f'Set: {my_set}')
    my_set.discard(1)
    my_set.add ('Яблоко')
    my_set.add(13)
    my_set.add("(5, 6, 1.6)")
    print(f'Modified set: {my_set}')
if __name__ == "__main__":
    task_1()
    print('\n' * 2 + '=' * 30 + '\n' * 2)
    task_2()