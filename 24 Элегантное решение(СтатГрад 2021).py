print(len([i for i in open("24.1.txt").readline().split("UM")[1:-1] if len(i) >= 14 and "A" not in i]))
# Определить кол-во групп из идущих подряд 18 символов нач и конч на UM и без А
# У первого и второго элемента НЕ БЫЛО UM, поэтому [1:-1]