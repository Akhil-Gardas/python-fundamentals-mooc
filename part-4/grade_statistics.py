# Write your solution here
def get_input():
    my_list=[]
    while True:
        user_input=input("Exam points and exercises completed: ")
        if user_input=="":
            break
        parts=user_input.split()
        exam_points=int(parts[0])
        exercise_points=int(parts[1])
        my_list.append([exam_points,exercise_points])
    return my_list

def calculate_excercise_points(amount):     
    return amount//10
def main():
    data=get_input()
    all_grades=[]
    all_points=[]

    for students in data:
        user_points=students[0]
        excercise=students[1]

        ex_points=calculate_excercise_points(excercise)
        total_points=user_points+ex_points  
        if user_points<10:
            grade=0 
        else:    
            if 0<=total_points<=14:
                grade=0
            elif 15<=total_points<=17:
                grade=1   
            elif 18<=total_points<=20:
                grade=2
            elif 21<=total_points<=23:
                grade=3   
            elif 24<=total_points<=27:
                grade=4 
            elif 28<=total_points<=30:
                grade=5
                                   
        all_grades.append(grade)
        all_points.append(total_points)

    print("Statistics:")
    if len(all_points)>0:
        avg=sum(all_points)/len(all_points)
        print(f"Points average: {avg:.1f}")   

        pass_count=0
        for g in all_grades:
            if g>0:
                pass_count+=1
        pass_pct=(pass_count/len(all_grades))*100
        print(f"Pass percentage: {pass_pct:.1f}")    
    else:
        print("Points average:0.0")
        print("Pass percentage:0.0")             

    print("Grade distribution:")
    for i in range(5,-1,-1):
        stars = "*" * all_grades.count(i)
        print(f"  {i}: {stars}")

main()        