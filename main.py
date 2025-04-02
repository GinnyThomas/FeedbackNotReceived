from scripts.identify_non_submitters import identify_non_submitters


def main():
    # List of emails to check against the spreadsheet - learners
    # if you copy in your email list from the agenda sheet, wrap it in a single quote, select the full list and ask
    # Github co-pilot to format it into separate emails
    e1 = []

    # List of emails to check against the spreadsheet - mentors

    e2 = []

    # change the spreadsheet name to the one you want to check in your downloads folder
    # change e1 to e2 to check the mentors
    # change the cohort to the one you want to check (e.g. 'Q1 2025')
    non_submitters = identify_non_submitters('spreadsheet_name', e1, 'Q1 2025')
    print("Non-submitters: \n", non_submitters)

if __name__ == "__main__":
    main()
