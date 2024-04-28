from setup import condor, format_csv_value, technopop, marathon, jongara, strip_unique_isbns


def studentinitialize():
    all_Students = "Files/students.csv"
    technopop(all_Students, overwrite_original=True)

