def using_control_once():
    if len("True") == 4:
        return "Success #1"

def using_control_again():
    if "True".lower() == "true":
        return "Success #2"

print using_control_once()
print using_control_again()
