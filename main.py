from scripts.identify_non_submitters import identify_non_submitters


def main():
    # List of emails to check against the spreadsheet - learners
    # if you copy in your email list from the agenda sheet, wrap it in a single quote, select the full list and ask
    # Github co-pilot to format it into separate emails
    e1 = ['muhammad.a.ahmad@capgemini.com', 'milo.brookes@capgemini.com', 'johannes.bull@capgemini.com',
                  'nick.cooke@capgemini.com', 'stephen.heath@capgemini.com', 'nadin.jandali@capgemini.com',
                  'al.miliunas@capgemini.com', 'ahmadzeya.naeem@capgemini.com', 'ellie.newell@capgemini.com',
                  'william.pattle@capgemini.com', 'gary.tate@capgemini.com', 'russell.thorn@capgemini.com',
                  'andrew.adey@capgemini.com']

    # List of emails to check against the spreadsheet - mentors

    e2 = ['martin.armstrong@capgemini.com', 'jake.barnes@capgemini.com', 'steve.mallen@capgemini.com',
        'richard.melvin@capgemini.com', 'joey.moore@capgemini.com', 'ian.ralphs@capgemini.com',
        'ben.ryan@capgemini.com', 'james.whiteley@capgemini.com', 'richard.woollett@capgemini.com',
        'virginia-elizabeth.thomas@capgemini.com', 'valentin.lukovski@capgemini.com']

    # change the spreadsheet name to the one you want to check in your downloads folder
    # change e1 to e2 to check the mentors
    # change the cohort to the one you want to check (e.g. 'Q1 2025')
    non_submitters = identify_non_submitters('Scala Academy Block 4 Diary Study(1-5)', e1, 'Q1 2025')
    print("Non-submitters: \n", non_submitters)

if __name__ == "__main__":
    main()