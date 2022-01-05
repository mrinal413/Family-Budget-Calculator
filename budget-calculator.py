class Calculator:
    
    def __init__(self, F, C, E, MD, Edu, T, S, OB):
        self.Food = F
        self.Clothing = C
        self.Entertainment = E
        self.Materialistic_Desires = MD 
        self.Education = Edu
        self.Total = T
        self.Savings = S
        self.overBudget = OB

    def withdraw(self, category, amount):
        if category=="F":
            if self.Food-amount>=0:
                self.Food -= amount
            else:
                return 1
        
        elif category=="C":
            if self.Clothing-amount>=0:
                self.Clothing -= amount
            else:
                return 1
        
        elif category=="E":
            if self.Entertainment-amount>=0:
                self.Entertainment -= amount
            else:
                return 1
        
        elif category=="MD":
            if self.Materialistic_Desires-amount>=0:
                self.Materialistic_Desires -= amount
            else:
                return 1
        
        elif category=="Ed":
            if self.Education-amount>=0:
                self.Education -= amount
            else:
                return 1
        self.Total -= amount
        print("Withdrawal Successful!!\n")
        return 0

    def transfer(self, category):
        A = input("You don't have enough funds in this category :( Do you want to transfer funds from any other category? [Y/N] ")
        if A=='Y':
            cgy, amt = input("Enter category and amount to be transferred: ").split()
            amt = int(amt)

            if category=="F":
                if cgy=="C":
                    self.Clothing -= amt
                    self.Food += amt
                elif cgy=="E":
                    self.Entertainment -= amt
                    self.Food += amt
                elif cgy=="Ed":
                    self.Education -= amt
                    self.Food += amt
                elif cgy=="MD":
                    self.Materialistic_Desires -= amt
                    self.Food += amt
                (self.overBudget).append('F')

            elif category=="C":
                if cgy=="F":
                    self.Food -= amt
                    self.Clothing += amt
                elif cgy=="E":
                    self.Entertainment -= amt
                    self.Clothing += amt
                elif cgy=="Ed":
                    self.Education -= amt
                    self.Clothing += amt
                elif cgy=="MD":
                    self.Materialistic_Desires -= amt
                    self.Clothing += amt
                (self.overBudget).append('C')

            elif category=="E":
                if cgy=="C":
                    self.Clothing -= amt
                    self.Entertainment += amt
                elif cgy=="F":
                    self.Food -= amt
                    self.Entertainment += amt
                elif cgy=="Ed":
                    self.Education -= amt
                    self.Entertainment += amt
                elif cgy=="MD":
                    self.Materialistic_Desires -= amt
                    self.Entertainment += amt
                (self.overBudget).append('E')

            elif category=="Ed":
                if cgy=="C":
                    self.Clothing -= amt
                    self.Education += amt
                elif cgy=="F":
                    self.Food -= amt
                    self.Education += amt
                elif cgy=="E":
                    self.Entertainment -= amt
                    self.Education += amt
                elif cgy=="MD":
                    self.Materialistic_Desires -= amt
                    self.Education += amt  
                (self.overBudget).append('Ed')

            elif category=="MD":
                if cgy=="C":
                    self.Clothing -= amt
                    self.Materialistic_Desires += amt
                elif cgy=="F":
                    self.Food -= amt
                    self.Materialistic_Desires += amt 
                elif cgy=="Ed":
                    self.Education -= amt
                    self.Materialistic_Desires += amt
                elif cgy=="E":
                    self.Entertainment -= amt
                    self.Materialistic_Desires += amt
                (self.overBudget).append('MD')
            print("Transfer Complete!!\n")  
        else:
            print("Sorry the transaction cannot be processed for this category.\n")

    def get_balance(self):
        print("\nDisplaying Current Balance")
        print(f"FOOD: \t\t {self.Food} \nCLOTHING: \t {self.Clothing} \nEntertainment \t {self.Entertainment} \nMaterialistic_Desires: \t {self.Materialistic_Desires} \nEducation: \t {self.Education}\nTotal: \t {self.Total}\n")

    def savings(self, initial_amount):
        for i in self.overBudget:
            if i=='F': print("You spent more money on Food than intended!")
            elif i=='C': print("You spent more money on Clothing than intended!")
            elif i=='E': print("You spent more money on Entertainment than intended!")
            elif i=='MD': print("You spent more money on Materialistic Desires than intended!")
            elif i=='Ed': print("You spent more money on Education than intended!")
        per = (self.Total/initial_amount)*100
        print(f"You saved {per:.2f}% from your budget this month.\n ")
        if per>=self.Savings:
            print("Saving goal reached, Congratulations!!!")
        else:
            print("Saving goal not reached ☹ You should try saving more.")



print("❀❀ Greetings Amigo! ❀❀")

Total = float(input("Please enter your total amount for budgeting: "))
print("\nDivide your budget for each category(in %): ")
Food = ((float(input("1. FOOD(F): ")))/100)*Total
Clothing = ((float(input("2. CLOTHING(C): ")))/100)*Total
Entertainment = ((float(input("3. ENTERTAINMENT(E): ")))/100)*Total
Materialistic_Desires = ((float(input("4. MATERIALISTIC_DESIRES(MD): ")))/100)*Total
Education = ((float(input("5. EDUCATION(Ed): ")))/100)*Total
save = input("Enter savings goal(in %): ")
save = float(save)
overBudget = []

budget = Calculator(Food, Clothing, Entertainment, Materialistic_Desires, Education, Total, save, overBudget)

print("\nTo withdraw money enter 1\nTo check current balance enter 2\nTo show month-end analysis enter 3\n")
k = 0

while(k!=3):

    k = int(input())

    if k==1:
        print("For Food use 'F'\nFor Clothing use 'C'\nFor Entertainment use 'E'\nFor Materialistic Desires use 'MD'\nFor Educatiion use 'Ed\n")
        category, amount = input("Enter category and amount: ").split()
        r = budget.withdraw(category, int(amount))
        if r==1:
            budget.get_balance()
            budget.transfer(category)
    elif k==2:
        budget.get_balance()
    elif k==3:
        budget.get_balance()
        budget.savings(Total)

print("\n❅ ❅ ❅ This Budget Calculator was presented to you by Nikhil, Mrinalini, Irhaam & Garvit. ❅ ❅ ❅")

Rating = int(input("\nHow would you rate our app? "))
for i in range(Rating):
    print('✮',end='')

print()