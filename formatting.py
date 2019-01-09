import datetime

default_names = ["Lee", "Alex", "oreo"]
default_amounts = [213123, 89.22, 33]

unf_message = """Hi {name}

Thank you for your purchase on {date}/
We hope you enjoy it.

The purchase total was ${total}/

Have a great day!
- Madam Auring
"""


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today = today)
        for name in names:
            new_msg = unf_message.format(
                name = name,
                date = text,
                total = amounts[i]
            )
        i += 1 # loop going thru accordingly
        print(new_msg)

make_messages(default_names, default_amounts)
