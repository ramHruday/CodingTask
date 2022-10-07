import csv


def write_to_csv(iced, hot, filename='data_file.csv'):
    data_file = open(filename, 'w', newline='', encoding='utf-8')
    header = ["id", "title", "description", "ingredients", "image"]
    csv_writer = csv.DictWriter(data_file, fieldnames=header)
    csv_writer.writeheader()

    for cold_c in iced:
        csv_writer.writerow(cold_c)

    for hot_c in hot:
        csv_writer.writerow(hot_c)

    data_file.close()
