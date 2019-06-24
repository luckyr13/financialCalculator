# Financial Calculator
# By: Ricardo Guzman
# FIN-512 01 Money and Banking

def menu():
    option = -1
    print('FINANCIAL CALCULATOR\n')
    
    while True:
        print('\nChoose an option:')
        print('1. Simple Present Value')
        print('2. Yield to Maturity on a Simple Loan')
        print('3. Yearly Payment on a Fixed-Payment Loan')
        print('4. Yield to Maturity on a Fixed-Payment Loan')
        print('5. Bond Price (Present Value) for a Coupon Bond')
        print('6. Yield to Maturity for a Coupon Bond')
        print('0. Exit')

        try:
            option = int(input('Type an option: '))
        except:
            option = -1

        if option == 1:
            simplePresentValue()
        elif option == 2:
            yield2maturitySimpleLoan()
        elif option == 3:
            ypFixedPayment()
        elif option == 4:
            yield2maturityFixedPayment()
        elif option == 5:
            bondPriceCouponBond()
        elif option == 6:
            yield2maturityCouponBond()
        elif option == 0:
            break
        else:
            print('Wrong option!')
        


# Simple Present Value
def simplePresentValue():
    print('\n+ Simple Present Value')
    print('PV=Present Value (amount borrowed)')
    print('CF=Cash flow')
    print('i=annual interest rate')
    print('n=number of years')
    CF = float(input('CF= '))
    i = float(input('i= '))
    n = int(input('n= '))
    PV = 0.0

    PV = CF / (1 + i)**n
    print('PV = CF / (1+i)^n')
    print('PV = {0:.4f} / (1 + {1:.4f}) ^ {2:.1f} '.format(CF, i, n))
    print('PV = {0:.4f}'.format(PV))
    
# Yield to maturity on a Simple Loan
def yield2maturitySimpleLoan():
    print('\n+ Yield to maturity on a Simple Loan')
    print('PV=Present Value (amount borrowed)')
    print('CF= cash flow in one year')
    print('n=number of years')
    
    CF = float(input('CF= '))
    PV = float(input('PV= '))
    n = int(input('n= '))
    i = 0.0

    i = (CF / PV)**(1/n) - 1 
    print('CF = {0:.4f} PV = {1:.4f} n = {2:d} '.format(CF, PV, n))
    print('i = {0:.4f}'.format(i))

# Fixed-Payment Price on a Fixed-Payment Loan
def ypFixedPayment():
    print('\n+ Fixed-Payment Price on a Fixed-Payment Loan')
    print('FP=Fixed Payment')
    print('LV=Loan Value')
    print('i=annual interest rate')
    print('n=number of years')
    
    LV = float(input('LV= '))
    i = float(input('i= '))
    _n = int(input('n= '))
    zigma = 0.0
    FP = 0.0
    
    for n in range(1, _n + 1):
        zigma += (1 / (1 + i)**n)

    FP = LV / zigma
    print('LV = {0:.4f} i = {1:.4f} n = {2:d}'.format(LV, i, n))
    print('FP = {0:.4f}'.format(FP))

# Yield to Maturity on a Fixed-Payment Loan
def yield2maturityFixedPayment():
    print('\n+ Yield to Maturity on a Fixed-Payment Loan')
    print('FP=Fixed Payment')
    print('LV=Loan Value')
    print('i=annual interest rate')
    print('n=number of years')
    
    LV = float(input('LV= '))
    FP = float(input('FP= '))
    _n = int(input('n= '))
    i = 0.0
    epsilon = 0.01
    steps = 0.00001
    zigma = 0.000000001

    while abs(FP - (LV / zigma)) > epsilon and i <= 1:
        i += steps
        zigma = 0.0
        for n in range(1, _n + 1):
            zigma += (1 / (1 + i)**n)

    if abs(FP - (LV / zigma)) <= epsilon:
        print('LV = {0:.4f} FP = {1:.4f} n = {2:d}'.format(LV, FP, n))
        print('i = {0:.4f}'.format(i))
    else:
        print('i Not Found :(')

# Bond Price for a Coupon Bond
def bondPriceCouponBond():
    print('\n+ Bond Price for a Coupon Bond')
    print('P=price of coupon bond')
    print('C=yearly coupon payment')
    print('F=face value of the bond')
    print('n=years to madurity date')
    print('i=interest rate')
    
    C = float(input('C= '))
    F = float(input('F= '))
    i = float(input('i= '))
    _n = int(input('n= '))
    zigma = 0.0
    # Bond Face Price
    bfp = F / (1 + i)**_n
    
    
    for n in range(1, _n + 1):
        zigma += (1 / (1 + i)**n)

    P = (C * zigma) + bfp
    print('C = {0:.4f} i = {1:.4f} ' \
          'n = {2:d} F = {3:.4f} bfp {4:.4f}'.format(C, i, n, F, bfp))
    print('P = {0:.4f}'.format(P))
    
# Yield to Maturity on a Coupon Bond
def yield2maturityCouponBond():
    """
    """
    print('\n+ Yield to Maturity on a Coupon Bond')
    print('P=price of coupon bond')
    print('C=yearly coupon payment')
    print('F=face value of the bond')
    print('n=years to madurity date')
    print('i=interest rate')
    
    P = float(input('P= '))
    C = float(input('C= '))
    F = float(input('F= '))
    _n = int(input('n= '))
    i = 0.0
    epsilon = 0.01
    steps = 0.000001
    zigma = 0.000000001
    #Bond Face Price
    bfp = zigma

    while abs(P - ((C * zigma) + bfp)) > epsilon and i <= 1:
        i += steps
        zigma = 0.0
        bfp = F / (1 + i)**_n
        
        for n in range(1, _n + 1):
            zigma += (1 / (1 + i)**n)




    if abs(P - ((C * zigma) + bfp)) <= epsilon:
        print('P = {0:.4f} C = {1:.4f} n = {2:d}'.format(P, C, n))
        print('i = {0:.4f}'.format(i))
    else:
        print('i Not Found :(')


def run():
    menu()


if __name__ == "__main__":
    try:
        run()
    except Exception as err:
        print('Error: ', err)
