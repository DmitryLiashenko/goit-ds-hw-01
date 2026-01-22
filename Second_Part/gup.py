from datetime import timedelta as td
from datetime import datetime as dtdt
import datetime as dt

def get_upcoming_birthdays(book):
    """Get upcoming birthdays data."""
    congratulation_data = []
    today = dtdt.today().date()
    future_day = today + td(days=7)
    for record in book.values():
        if record.birthday:
            birthday = record.birthday.value
            birthday_date = dt.date(today.year, birthday.month, birthday.day)
            if (today < birthday_date) and (birthday_date <= future_day):
                if birthday_date.weekday() == 5:
                    birthday_date = birthday_date + td(days=2)
                    congratulation_data.append({'name': record.name.value,
                                                'congratulation_date': birthday_date.strftime("%Y-%m-%d")})
                elif birthday_date.weekday() == 6:
                    birthday_date = birthday_date + td(days=1)
                    congratulation_data.append({'name': record.name.value,
                                                'congratulation_date': birthday_date.strftime("%Y-%m-%d")})
                else:
                    congratulation_data.append({'name': record.name.value,
                                                'congratulation_date': birthday_date.strftime("%Y-%m-%d")})
    return congratulation_data