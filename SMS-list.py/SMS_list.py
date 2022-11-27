from db import student_list,student_table_format

categary=['fname','lname','roll_no','std','age','intrest']

def display_student():
    student_table_format()
    for i in range(len(student_list)):

        print(f'\n{i+1}\t{student_list[i][1]:<7.10} \t\t{student_list[i][3]:<7.10} \t{student_list[i][5]}\t\t{student_list[i][7]}\t\t{student_list[i][9]}\t\t{student_list[i][11]}')
        print(f"{'-'*125}")
    print()


def student_admission():
    sub_list=[]
    student_list.append(sub_list)


    fname=(input('Enter first name of student: ').lower())
    sub_list.append('fname')
    sub_list.append(fname)
    lname=(input('Enter last name of student: ').lower())
    sub_list.append('lname')
    sub_list.append(lname)
    roll_no=eval(input('Enter roll no of student: '))
    sub_list.append('roll_no')
    sub_list.append(roll_no)
    age=eval(input('Enter age of student: '))
    sub_list.append('age')
    sub_list.append(age)
    std=eval(input('Enter std of student: '))
    sub_list.append('std')
    sub_list.append(std)
    intrest=(input('Enter intrest of student: ').lower())
    sub_list.append('intrest')
    sub_list.append(intrest)

    


def update_student_data():
    roll_no=int(input('Enter Sr no of student to update data: '))
    update_option=int(input('choose the categary to update:[1=fname, 3=lname, 5=roll_no, 7=std, 9=age, 11=intrest]: '))
    update_value=(input('enter value to update:[fname,lname,roll_no,std,age,intrest]: '))

    student_list[int(roll_no-1)][update_option]=update_value
    
    



def delete_student_data():
    delete_option=int(input('choose Sr no to delete data: '))
    
    del student_list[delete_option-1]
    display_student()




def sort_by_std():
    sort_option=int(input('choose std to sort data: '))
    student_table_format()
    for i in range(len(student_list)):
        while True:
            if student_list[i][7]==sort_option:
                l=student_list[i]
        
                print(f'\n{i+1}\t{l[1]:<7.10} \t\t{l[3]:<7.10} \t{l[5]}\t\t{l[7]}\t\t{l[9]}\t\t{l[11]}')
                print(f"{'-'*125}")
            break

          
def sort_by_age():
    sort_option=int(input('choose age to sort data: '))
    student_table_format()
    for i in range(len(student_list)):
        while True:
            if student_list[i][9]==sort_option:
                l=student_list[i]
        
                print(f'\n{i+1}\t{l[1]:<7.10} \t\t{l[3]:<7.10} \t{l[5]}\t\t{l[7]}\t\t{l[9]}\t\t{l[11]}')
                print(f"{'-'*125}")
            break

def sort_by_intrest():
    sort_option=(input('choose intrest to sort data: '))
    student_table_format()
    for i in range(len(student_list)):
        while True:
            if student_list[i][11]==sort_option:
                l=student_list[i]
        
                print(f'\n{i+1}\t{l[1]:<7.10} \t\t{l[3]:<7.10} \t{l[5]}\t\t{l[7]}\t\t{l[9]}\t\t{l[11]}')
                print(f"{'-'*125}")
            break





while True:
    option=eval(input('Select one: [1:Read/Display, 2:Add, 3:Update 4:Delete 5:age sort 6:age sort 7:intrest sort]: '))

    if option==1:
       display_student()

    elif option==2:
         student_admission()
         
    elif option==3:  
         update_student_data()
        
    elif option==4:
        delete_student_data()

    elif option==5:
        sort_by_std()

    elif option==6:
        sort_by_age()

    elif option==7:
        sort_by_intrest()

    else:
        print('invilide input')

    choice=input('do you want to continue [y/n]: ')
    if choice !='y':
        print('Thank you')
        break


    