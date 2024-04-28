from setup import condor, format_csv_value, technopop, marathon, jongara, strip_unique_isbns


def studentinitialize():
    print("Student")
    technopop("Files/students.csv", overwrite_original=False)
