 # curly = re.search(r"\{(.*?)\}", args[len(args) - 1])
    # print(args)
    # if curly is None:
    #     my_arg = args[1].split(", ")
    #     args = args[0]
    #     id = ""
    #     attr = ""
    #     value = ""
    #     new_list = [id, attr, value]
    #     i = 0
    #     while i < len(my_arg):
    #         if my_arg[i]:
    #             new_list[i] = my_arg[i].replace("\"", "")
    #         else:
    #             break
    #         i += 1
    #     result = {args: new_list}
    #     return result
    # my_arg = args[1].split(", ")
    # i = 2
    # while i < len(my_arg):
    #     my_arg[1] += ", " + my_arg[i]
    #     i += 1
    # my_arg = [my_arg[0].replace("\"", ""), my_arg[1]]
    # args = args[0]
    # result = {args: my_arg}
    # return resul