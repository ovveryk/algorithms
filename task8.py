arr=[5,1,4,2,8]

def bubble(mas):
    n = len(mas)
    for i in range(n):
        for j in range(0, n-i-1):
            if mas[j] > mas[j+1]:
                mas[j], mas[j+1] = mas[j+1], mas[j]
                print("Після обміну:", mas)

bubble(arr)
print("Відсортований масив:", arr)
