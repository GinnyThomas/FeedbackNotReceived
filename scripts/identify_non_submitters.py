import os
import pandas as pd

def identify_non_submitters(spreadsheet_name, email_list, cohort):
    # Read the spreadsheet
    spreadsheet_path = os.path.expanduser(f'~/Downloads/{spreadsheet_name}.xlsx')
    df = pd.read_excel(spreadsheet_path)

    # Assuming the spreadsheet has a column named 'Email'
    df = df[df['Which Cohort is this feedback for?'] == cohort]
    submitted_emails = set(df['Email'].dropna().str.lower())

    # Convert the email list to a set of lowercase emails
    email_set = set(email.lower() for email in email_list)

    # Identify non-submitters
    non_submitters = email_set - submitted_emails

    return non_submitters
