from faker import Factory

import phonenumbers


def phone_generate():
    fake = Factory.create('uk_UA')
    while True:
        phone = fake.phone_number()
        if phone[0] == '+':
            x = phonenumbers.parse(phone)
            return phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
