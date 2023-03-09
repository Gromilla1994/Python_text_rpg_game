import classes

def validateAnswer(variants_of_answer, variants_are_colored=False) -> str:
    formating_action_variants = []

    if variants_are_colored:
        for key in variants_of_answer:
            formating_action_variants.append(variants_of_answer[key] + key)
    else:
        formating_action_variants = variants_of_answer

    answer = input("\nТвой выбор:\n").lower()

    while(answer not in variants_of_answer):
        print("\nТы ввёл что-то, что мне непонятно, преключенец.")

        # по логике если is_colored = true, то мы передаем dict, а если false то list, отсюда и такой страшный оператор
        result_after_condition = formating_action_variants if is_colored else formating_action_variants.keys()
        print("ты можешь:")
        answer = input(" : ".join(result_after_condition) + classes.bcolors.ENDC + "\n" + "твой выбор:" + "\n")

    return answer

# decorator for a console output
def pretify_separation(func):
    separation = "------------------------------"
    def wrapper(*args):
        print("\n" + separation)
        func(*args)
        print(separation + "\n")
    
    return wrapper