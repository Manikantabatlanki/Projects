pin = 123
balance = 1000
cust_pin = int(input('Enter your PIN: '))

if pin == cust_pin:
    while True:
        print('\n--- ATM Menu ---')
        print('1. Withdraw')
        print('2. Deposit')
        print('3. Balance Check')
        print('4. Exit')
        ch = int(input('Choose one option: '))

        if ch == 1:
            mny = int(input('How much money do you want to withdraw: '))
            if mny % 100 == 0:
                if mny <= balance:
                    balance =balance- mny
                    print('Please collect your cash.')
                else:
                    print('Insufficient funds.')
            else:
                print('Enter amount in multiples of 100.')

        elif ch == 2:
            mny = int(input('How much money do you want to deposit: '))
            if mny % 100 == 0:
                balance += mny
                print('Deposited successfully.')
            else:
                print('Wrong denomination. Enter amount in multiples of 100.')

        elif ch == 3:
            print('The available balance is:', balance)

        elif ch == 4:
            print('Exiting... Thank you for using the ATM.')
            break

        else:
            print('Invalid choice. Please try again.')

else:
    print('Incorrect PIN. Access denied.')

