class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            #print(self.get_balance()
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, description="Transfer to " + category.name)
            category.deposit(amount, description="Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False


    def __str__(self):
        s = self.name.center(30, '*')
        for i in self.ledger:
            s += '\n'
            s += i['description'][:23].ljust(23)
            amount = str(round(i['amount'], 2))
            if '.' not in str(i['amount']):
                amount += '.00'    
            s += amount.rjust(7)
        total = str(round(self.get_balance(), 2))
        s += '\nTotal: ' + total
        return s


def create_spend_chart(categories):
    rows = ['Percentage spent by category']

    # Getting Percentages

    total_spent = 0
    spent_list = []

    for category in categories:
        spent = 0
        for i in category.ledger:
            if i['amount'] < 0:
                spent -= i['amount']

        spent_list.append(spent)
        total_spent += spent


    raw_precentages = [(x / total_spent) for x in spent_list]
    percentages = [round((x / total_spent), 1) * 100 for x in spent_list]
    # Example percentages: [70, 20, 10]

    print('========DEBUG========')
    print('spent_list:', spent_list)
    print('percentages:', percentages)
    print('raw_precentages:', raw_precentages)
    print('total_spent:', total_spent)
    print('=====================')

    # Formatting Percentages

    for i in range(11):
        percent_level = 100 - i * 10
        s = (str(percent_level) + '|').rjust(4)

        for i in range(len(percentages)):

            if percentages[i] >= percent_level:
                s += ' o '
            else:
                s += '   '       

        rows.append(s)

    
    # Formatting names
    names = []
    for c in categories:
        names.append(c.name)

    names = [x.ljust(len(max(names, key=len))) for x in names]

    rows.append(' ' * 4 + '-' * (len(categories) * 3 + 1))

    for i in zip(*names):
       rows.append(' '*5 + '  '.join(i))
    
    result=''
    for row in rows:
        result += row + '\n'
    
    return result   #.rstrip('\n')


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
