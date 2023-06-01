'''
Author - Debag101
Purpose - Lowest balance out of all account holders
Date - 1 06 2023
'''

# Gets the data in form of a 2D list
def get_data():
    datas = []
    try : 
        # Getting the count of users
        countof_data = int(input("Enter the number of account holder's you have : "))
        # Getting data for each user one by one
        for i in range(countof_data) :
            datas.append([input(f"Enter name of user {i+1} : "), input("Enter user code : "), int(input("Enter bank balance of user : "))])
           
    except ValueError:
        print("Only enter valid data !")
        exit()
    # Returning datas finally
    finally:
        return datas

# Finds out the lowest bal
def get_lowest_bal(acc_holders):
    # min_bal stores the lowest value 
    min_bal = acc_holders[0][2]
    min_index = 0
    for index, data_list in enumerate(acc_holders):
        if data_list[2] < min_bal:
            min_bal = data_list[2]
            min_index = index
    # Prints out the result
    print(f"Lowest balance is of {acc_holders[min_index][0]} = {min_bal}")

# executing methods
account_holders = get_data()
get_lowest_bal(account_holders)

