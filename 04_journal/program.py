
def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------')
    print('      JOURNAL APP')
    print('------------------------')


def run_event_loop():
    print('What would you like to do with your Journal?')
    cmd = None
    journal_data = list()

    while cmd != 'x':
        cmd = input('(L)ist entries, (A)dd entries or E(x)it? ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            print_listing(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, I do not understand '{}'.".format(cmd))

    print("Goodbye!!!")


def print_listing(data):
    print(data)


def add_entry(data):
    text = input('Type your entry, hit <enter> to exit. ')
    data.append(text)


main()
