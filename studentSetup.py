from setup import technopop


def studentinitialize():
    print("Student")
    technopop("Files/students.csv", overwrite_original=False)


def main():
    studentinitialize()


if __name__ == "__main__":
    main()
