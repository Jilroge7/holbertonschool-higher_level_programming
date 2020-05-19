#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    newList = []
    ind1 = 0
    ind2 = 0

    for ind1, ind2 in zip(my_list_1, my_list_2):
        try:
            result = ind1 / float(ind2)
            newList.append(result)
        except ZeroDivisionError:
            print("division by 0")
            newList.append(0)
        except ValueError:
            print("wrong type")
            newList.append(0)
        except IndexError:
            print("out of range")
            newList.append(0)
        finally:
            pass
    return(newList)
