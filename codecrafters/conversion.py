import os
from django.conf import settings


def taking_content():
    global x, if_state, state_list  
    x = ""
    if_state = False
    state_list = []

    file_path = os.path.join(settings.BASE_DIR, "data_extract.txt")

    with open(file_path, 'r') as f:
        r = f.readlines()
    
    print(f"Reading from {file_path}: {r}")  

    for line in r:
        i = line.strip().split()
        
        if i and i[0] == 'if':
            var_other = " ".join(i[1:])  
            if_state = True
            state_list.append("if")
            x += f"{{% if {var_other} %}}\n"

        elif i and i[0] == 'for':
            var_other = " ".join(i[1:])  
            state_list.append("for")
            x += f"{{% for {var_other} %}}\n"

        elif i and i[0] == 'elif':
            var_other = " ".join(i[1:])  
            state_list.append("elif")
            x += f"{{% elif {var_other} %}}\n"

        elif i and i[0] == 'else':
            var_other = " ".join(i[1:])  
            state_list.append("else")
            x += f"{{% else {var_other} %}}\n"

        elif i and (i[0] != "if" and i[0] != "elif" and i[0] != "for" and i[0] != "else" and i[0] != "pass"):
            i_str = " ".join(map(str, i)) 

            if '(' in i_str and ')' in i_str:
                n = i_str.find("(")
                m = i_str.find(")")
            
                no = 0
                for t in range(n + 1, m):
                    tlist = list(range(n + 1, m))
                    num_values = len(tlist)
                
                    if num_values == 1:
                        x += f"{{{{{i_str[t]}}}}}\n"
                    elif num_values != 1:
                        no += 1
                        y2 = i_str[t:m]
                        if no == 1:
                            x += f"{{{{{y2}}}}}\n"

        elif i and i[0] == "pass":
            h = "# This is the 'else' block. You can add more HTML or logic here if needed. #"
            x += f"{{{{ {h} }}}} \n"  

    stack = []

    def empty_stk(a):
        return not a

    def push(stk, item):
        stk.append(item)

    def pop(stk):
        if empty_stk(stk):
            return '''Stack is Empty no element to Pop out'''
        else:
            return stk.pop()

    def peek(stk):
        if empty_stk(stk):
            return '''Stack is Empty no element to Peek'''
        else:
            return stk[-1]

    for v in state_list:
        push(stack, v)

    u = len(state_list)
    for _ in range(u):
        n = peek(stack)

        if n:
            if n == "if" or n == "for":
                x += f"{{% end{n} %}}\n"

        pop(stack)

    print(f"Processed content: {x}") 
    return x, state_list

def transfering_content(a):
    file_output_path = os.path.join(settings.BASE_DIR, "data_converted.txt")
    with open(file_output_path, 'w') as f:
        for line in a:  
            f.write(line) 
        print(f"Writing to {file_output_path}: {a}")    

x, _ = taking_content()
print(x)
transfering_content(x)
