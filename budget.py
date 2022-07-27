from math import floor, ceil


class Category:
    def __init__(self, category):
        self.ledger = []
        self.amount = 0
        self.category = category
        self.withdraws = 0

    def deposit(self, amount, description=''):
        self.amount += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({"amount": -amount, "description": description})
            self.withdraws += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.amount >= amount:
            return True
        else:
            return False

    def __str__(self):
        name_len = len(self.category)
        result = ceil((30 - name_len) / 2) * '*' + self.category + floor(
            (30 - name_len) / 2) * '*'

        for i in self.ledger:
            amount = format(float(i['amount']), '.2f')
            description = i['description']
            if len(description) > 23:
                description = description[:23]
                amount = format(float(amount), '.2f')
            if len(str(amount)) > 7:
                amount = amount[:7]
            result += '\n' + description + str(amount).rjust(30 -
                                                             len(description))

        result += '\nTotal: ' + format(float(self.amount), '.2f')
        return result


def create_spend_chart(categories):

    cat_list = []
    spent_list = []
    full_sum = 0
    len_list = len(categories)
    percents = range(100, -10, -10)
    max_cat = 0

    for name in categories:
        cat_list.append(name.category)
        spent_list.append(name.withdraws)
        full_sum += name.withdraws
        if max_cat < len(name.category):
            max_cat = len(name.category)

    for spent in range(len(spent_list)):
        spent_list[spent] = floor(10 * round(spent_list[spent] / full_sum, 2))
        spent_list[spent] = ' ' * (10 - spent_list[spent]) + 'o' * (
            spent_list[spent] + 1)
        cat_list[spent] += ' ' * (max_cat - len(cat_list[spent]))

    result = 'Percentage spent by category'

    for i in range(11):
        result += '\n' + ' ' * (3 - len(str(percents[i]))) + str(
            percents[i]) + '|'

        for j in range(len_list):
            result += ' ' + spent_list[j][i] + ' '
        result += ' '
    result += '\n' + ' ' * 4 + '-' * (3 * len_list + 1)

    for i in range(max_cat):
        result += ('\n' + ' ' * 5 + cat_list[0][i] + '  ' + cat_list[1][i] +
                   '  ' + cat_list[2][i] + '  ')

    return result
