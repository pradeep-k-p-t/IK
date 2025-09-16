def division(a,b):
    try: 
        rt = a/b 
    except Exception as e: 
        print(e)
    finally: 
        print("handled exception")

def write_file():
    lines = ["line1", "line2"]
    with open("my_file.txt", "w") as file:
        file.write(lines)
       


write_file()

