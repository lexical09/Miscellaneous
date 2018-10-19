'''
https://www.mtgprofessor.com/formulas.htm

P is your principal (amount borrowing).
r is your monthly interest rate, calculated by dividing your annual interest rate by 12.
n is your number of payments (the number of months you will be paying the loan)

M is your monthly payment.
M = P[i(1 + i)^n]/[(1 + i)^n - 1]

B is remaining loan balance of a fixed payment loan after p months
B = P[(1 + i)^n - (1 + i)^p]/[(1 + i)^n - 1]
'''

# Monthly payment
def monthly(house_price,down_percent,yearly_interest,year):
    down_payment = (down_percent/100)*house_price
    borrow_amount = house_price - down_payment
    monthly_interest = (yearly_interest/100)/12
    n = year*12
    monthly_payment = borrow_amount*(monthly_interest*(1+monthly_interest)**n)/(((1+monthly_interest)**n)-1)
    total_interest = monthly_payment*n-borrow_amount
    monthly_interest_paid = (borrow_amount-n)/monthly_payment
    total_amount_pay = total_interest + borrow_amount
    
    ############ Property Tax Info ##########
    city = 'MECHANICSBURG'
    total_mills = 0.01956030 #https://www.ccpa.net/DocumentCenter/View/8646/Tax-Rate--Millage-Rate-Sheet?bidId=
    yearly_tax = total_mills*house_price
    
    ################################
    print('House Price: ${}'.format(house_price))
    print('Percent Down: {}%'.format(down_percent))
    print('Yearly Interest Rate: {}%'.format(yearly_interest))
    print('Loan Term: %s years'%(year))
    print('-------------------------')
    print('')
    print('Down Payment: $%s'%(down_payment))
    print('Loan Amount: $%s'%(borrow_amount))
    print('-------------------------')
    print('Loan To Value Ratio: {}%'.format(total_interest/borrow_amount*100))
    print('Monthly Interest Amount: $%s'%(monthly_interest_paid))
    print('--------------------------------------------------')
    print('Monthly Payments: $%s'%(monthly_payment))
    print('--------------------------------------------------')
    print('')
    print('Total Interest Paid after {} Years: ${}'.format(year,total_interest))
    print('Total Amount Paid after %s Years: $%s'%(year,total_amount_pay))
    print('--------------------------------------------------')
    print('')
    print('****** Estimated Property Tax ******')
    print('City: ',city)
    print('Total Millages: ',total_mills)
    print('Estimated Yearly Property Tax: $%s'%(yearly_tax))
    
    
# Remaining loan balance of a fixed payment loan after p months    
def remain(house_price, down_percent, yearly_interest, year, p):
    down_payment = (down_percent/100)*house_price
    borrow_amount = house_price - down_payment
    monthly_interest = (yearly_interest/100)/12
    n = year*12
    monthly_payment = borrow_amount*(monthly_interest*(1+monthly_interest)**n)/(((1+monthly_interest)**n)-1)
    total_interest = monthly_payment*n-borrow_amount
    monthly_interest_paid = (borrow_amount-n)/monthly_payment
    #months is number of months already paid
    remaining_balance = borrow_amount*((1+monthly_interest)**n - (1 + monthly_interest)**p)/(((1+monthly_interest)**n)-1)
    print('house price: ${}'.format(house_price))
    print('percent down: {}%'.format(down_percent))
    print('yearly interest: {}%'.format(yearly_interest))
    print('Loan Term: ',year,'years')
    print('months paid: ',p,'months')
    print('-------------------------')
    print('')
    print('Down Payment: $%s'%(down_payment))
    print('Loan Amount: $%s'%(borrow_amount))
    print('--------------------------------------------------')
    print('')
    print('Remaining Loan Balance: $%s'%(remaining_balance))
    print('')
    print('--------------------------------------------------')
    print('')
    print('monthly interest amount: $%s'%(monthly_interest_paid))
    print('total interest after {} years is ${} (which is {}% of amount borrowed)'.format(year,total_interest,total_interest/borrow_amount*100))
    