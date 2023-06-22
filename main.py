def main():
    
    ##################################################

    x = int(input("Number of Males: "))
    y = int(input("Number of Females: "))
    t = x + y
    percentage_males = t/x
    percentage_females = t/y
    print("The total number of students: ", t)
    print(f"The number of males and females: {x}, {y} ")
    print(f"The percentage of males and females: {percentage_males}, {percentage_females} ")
        ########################################
    # Do not delete the return statement
    ########################################
    
    return percentage_males, percentage_females


if __name__ == '__main__':
    main()
