import csv
import matplotlib.pyplot as plt

with open("data1.csv", encoding='windows-1251') as r_file:
    incl_col = [0, 3, 9]
    data1 = []
    file_reader = csv.reader(r_file, delimiter = ";")
    for row in file_reader:
       col = list(row[i] for i in incl_col)
       data1.append(col)

    time=[]
    PDZ = []
    YOZ = []
    count = 0
    for i in range(3774):
        if count == 0:
            count +=1
        else:
            time.append(float(data1[i][0]))
            PDZ.append(float(data1[i][1]))
            YOZ.append(float(data1[i][2]))

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,figsize=(8, 4))
    ax1.stackplot(time,  [YOZ, PDZ], labels=['Положение дроссельной заслонки (%)', 'Угол опережения зажигания (°ПКВ)'])
    ax1.set_title('График 1 задание 2')
    ax1.legend(loc='upper left')
    ax1.set_ylabel('Пдз(%) Уоз(°)')
    ax1.set_xlabel('Время (с)')
    ax1.set_ylim(ymax= 180)
    ax1.set_xlim(xmin=time[0], xmax=time[-1])
    fig.tight_layout()
    plt.scatter(PDZ, YOZ)
    ax2.scatter(x=PDZ, y= YOZ, marker='o', c='r', edgecolor='b')
    ax2.set_title('График корреляции')
    ax2.set_xlabel('$Положение дроссельной заслонки$')
    ax2.set_ylabel('$Угол опережения зажигания$')
    plt.show()



