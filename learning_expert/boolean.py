# bool data type

value=str()

bool(value) # it returns false only for empty values 

# bool return false in these input
print(f'''
{bool(False)}
{bool(None)}
{bool(0)}
{bool("")}
{bool(())}
{bool([])}
{bool({})}''')
