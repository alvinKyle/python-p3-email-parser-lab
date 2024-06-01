import re

class EmailAddressParser:
    email_regex = re.compile(r'([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')

    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        email = re.split(r",|\s", self.emails)

        parsed_emails = set()
        for string in email:
            if self.email_regex.fullmatch(string.strip()):  
                parsed_emails.add(string.strip())

        return sorted(parsed_emails)


