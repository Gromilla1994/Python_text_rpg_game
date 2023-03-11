import classes

def validateAnswer(variants_of_answer, variants_are_colored=False) -> str:
    formating_action_variants = []

    if variants_are_colored:
        formating_action_variants = addColorToStrings(variants_of_answer)
    else:
        formating_action_variants = variants_of_answer

    answer = input("\nТвой выбор:\n").lower()

    while(answer not in variants_of_answer):
        print("\nТы ввёл что-то, что мне непонятно, преключенец.")

        # по логике если is_colored = true, то мы передаем dict, а если false то list, отсюда и такой страшный оператор
        result_after_condition = formating_action_variants if variants_are_colored else formating_action_variants.keys()
        
        formating_result = ' : '.join(result_after_condition) + classes.bcolors.ENDC
        print(f"ты можешь:\n{formating_result}\n")
        answer = input("твой выбор:" + "\n").lower()

    return answer

def addColorToStrings(dict_of_text_and_color: dict):
    formating_dict = []

    for key in dict_of_text_and_color:
        formating_dict.append(dict_of_text_and_color[key] + key)
    
    return formating_dict 

# decorator for a console output
def pretify_separation(func):
    separation = "------------------------------"
    def wrapper(*args):
        print("\n" + separation)
        func(*args)
        print(separation + "\n")
    
    return wrapper