def arithmetic_arranger(problems, result=False):
    data = len(problems)
    if len(problems) > 5 or len(problems) < 1:
        return "Error: Too many problems."
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for i,problems in enumerate(problems):
        num1, op, num2 = problems.split()
        
# Boundary and the limits
        if not op in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if op == "+":
            solution = int(num1) + int(num2)
        else :
            solution = int(num1) - int(num2)
        num_lenght = len(max([num1,num2], key=len))

        line1 += num1.rjust(num_lenght+2)
        line2 += op + num2.rjust(num_lenght+1)
        line3 += "-" * (num_lenght+2)
        line4 += str(solution).rjust(num_lenght+2)

        if i < data-1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            line4 += "    "
        
    if result : 
        vertical_problems = line1 +"\n"+ line2+"\n"+ line3 +"\n"+ line4
    else :
        vertical_problems = line1 +"\n"+ line2+"\n"+ line3
    
    return vertical_problems
