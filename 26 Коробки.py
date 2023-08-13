f = open("26.3.txt")
n = int(f.readline())
boxes = []
for s in f:
    a = s.split()
    boxes.append([int(a[0]), a[1]])
boxes.sort(reverse=True)
blocks = []
while boxes:
    gift = [boxes[0]]
    for box in boxes[1:]:
        if gift[-1][0] - box[0] >= 6 and box[1] != gift[-1][1]:
            gift.append(box)
    blocks.append(gift)
    for box in gift:
        boxes.remove(box)
print(len(blocks), len(max(blocks, key=len)))
# даны коробки, если разница между большой/маленькой коробкой <=3 (2 символ это цвет) то они вкладываются друг в друга
# также складываем подарки по блокам
