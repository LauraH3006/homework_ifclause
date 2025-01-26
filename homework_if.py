#If clauses homework
def calculate_net_salary():
 try:
    gross_salary= float(input("Enter the gross salary: "))
    num_children= int(input("Enter the number of children: "))

    #initialize variables
    tax_rate= 0.0
    tax_cut_per_child= 0.0


    if gross_salary < 1000:
        tax_rate= 0.10
    elif gross_salary < 2000:
        tax_rate = 0.12
    elif gross_salary < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    if gross_salary < 2000:
        tax_cut_per_child= 0.01
    else :
        tax_cut_per_child= 0.005

    total_tax_rate= tax_rate - (tax_cut_per_child * num_children)
    total_tax_rate= max(total_tax_rate,0)
    net_salary= gross_salary *(1-total_tax_rate)
    print(f"Net salary is :{net_salary:.2f}")

 except ValueError:
    print("Please enter valid numerical values for gross salary and number for children.")

calculate_net_salary()