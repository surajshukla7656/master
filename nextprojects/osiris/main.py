

def operator_manager(command):
    prompt=""
    for char in command:
        if char==" ":
            prompt+="_"
        else:
            prompt+=char
    if "(" and ")" not in prompt:
        prompt+="()"
    
    command=prompt
    return command




