from datetime import datetime

class Person:
    def __init__(self, first_name, gender, date_birth, surname=None, paternal_name=None, date_death=None):
        self.first_name = first_name
        self.gender = gender
        self.surname = surname
        self.paternal_name = paternal_name
        self.date_birth = self.change_date(date_birth)
        if self.date_birth is None:
            raise ValueError("Дата народження повинна бути вказана правильно.")
        self.date_death = self.change_date(date_death) if date_death else None

    def change_date(self, date_str):
        if isinstance(date_str, datetime):
            return date_str
        if not any(char.isdigit() for char in date_str):
            return None
        standard_date = date_str.replace(',', '.').replace(' ', '.').replace('-', '.').replace('/', '.')
        try:
            return datetime.strptime(standard_date, "%d.%m.%Y")
        except ValueError:
            return None

    def full_years(self):
        if self.date_birth is None:
            return None
        if self.date_death is None:
            age = datetime.now() - self.date_birth
        else:
            age = self.date_death - self.date_birth
        return age.days // 365 if age.days >= 0 else None

    def matches_query(self, query):
        query = query.lower()
        name_parts = self.first_name.lower()
        surname_parts = self.surname.lower() if self.surname else ''
        paternal_name_parts = self.paternal_name.lower() if self.paternal_name else ''

        if query in name_parts or query in surname_parts or query in paternal_name_parts:
            return True
        return False

    def __str__(self):
        age_string = f"{self.full_years()} років"
        if self.date_death:
            gender_string = "помер" if self.gender.lower() == 'm' else "померла"
            age_string = f"{age_string} ({gender_string})"
        full_name = f"{self.first_name} {self.surname or ''} {self.paternal_name or ''}"
        return f"{full_name.strip()} {age_string}."