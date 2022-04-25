def user_input():
    print("hello")
    list = []
    for i in range(5):
        num = input("Type a number: ")
        list.append(int(num))
    print(list)
    return list

def cal_avg(avg):
    all = sum(avg)
    print(len(avg))
    average = all/len(avg)
    print("Average is ", average)
    print("Min is ", min(avg))
    print("Max is ", max(avg))


if __name__ == '__main__':
    num_given = user_input()
    cal_avg(num_given)
