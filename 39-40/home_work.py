def conversion_of_rub_to_dollars(amount, dollar_to_rub):
    res = round(amount / dollar_to_rub, 2)

    return f"{res}$"


def check_age(age):
    return age > 17


# print(conversion_of_rub_to_dollars(100, 85))
# print(check_age(2))