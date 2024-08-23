def delta_between_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    

    diff1 = list(set1 - set2)
    
    diff2 = list(set2 - set1)
    
    delta_list = diff1 + diff2
    
    return delta_list

def input_lists_together():
    print("double enter to give second input")
    list1 = []
    while True:
        try:
            input_block = input()
            if not input_block.strip():
                break
            list1 = input_block.splitlines()
        except EOFError:
            break
    
    print("doubke enter to give delta lists")
    list2 = []
    while True:
        try:
            input_block = input()
            if not input_block.strip():
                break
            list2 = input_block.splitlines()
        except EOFError:
            break

    return list1, list2

if __name__ == "__main__":
    list1, list2 = input_lists_together()
    delta = delta_between_lists(list1, list2)
    print("Delta list:")
    for item in delta:
        print(item)
