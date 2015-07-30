import csv
import sys

def usage():
    print('Usage:')
    print('python {} input_file output_file'.format(sys.argv[0]))

def main():

    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    input_file  = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, newline='') as fp:
        input_reader = csv.reader(fp)
        header = next(input_reader)

        with open(output_file, 'w', newline='') as fp:
            output_writer = csv.writer(fp)
            output_writer.writerow(['PassengerId', 'Survived'])

            for row in input_reader:
                if row[3] == 'female':
                    output_writer.writerow([row[0], '1'])
                else:
                    output_writer.writerow([row[0], '0'])


if __name__ == "__main__":
    main()
