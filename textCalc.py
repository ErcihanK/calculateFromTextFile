from operator import pow, truediv, mul, add, sub  
operators = {'+': add,'-': sub,'*': mul,'/': truediv,"^":pow}
def listToString(inFile):
    inF = open(inFile, 'r')
    for line in inF:
        line=line.split()
        problem = ""
        for nums in line:
            problem += nums
        if "=" in problem:
            problem= problem.replace("=", "")
            print(problem)
        return problem  
def calculate(problem):
        if problem.isdigit():
            return float(problem)
        for calculation in operators.keys():
            left, operator, right = problem.partition(calculation)
            if operator in operators:
                return operators[operator](calculate(left), calculate(right))
calc=str(listToString("math.txt"))
print(calc+"= " + str(round(calculate(calc), 4)))
