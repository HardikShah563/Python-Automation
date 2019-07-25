import csv


def read_csv():
    with open("studentdetails.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        for row in csv_reader:
            data.append(row)
    return data


def write_csv(data):
    with open("studentdetails.csv", 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for row in data:
            csv_writer.writerow(row)


def read_file():
    with open("sentmails.txt", 'r') as f:
        sent_mails = f.readlines()
    return sent_mails


def write_file(mail):
    with open("sentmails.txt", 'a') as f:
        f.write(mail + "\n")