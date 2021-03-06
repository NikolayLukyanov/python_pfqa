from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, fax=None, main_email=None, email_2=None, email_3=None,
                 homepage=None, birth_day=None, birth_month=None, birth_year=None, ann_day=None, ann_month=None, ann_year=None,
                 group_number=None, address2=None, phone2=None, notes=None, id=None, all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.main_email = main_email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.ann_day = ann_day
        self.ann_month = ann_month
        self.ann_year = ann_year
        self.group_number = group_number
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return ("%s:%s:%s") % (self.firstname, self.lastname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize