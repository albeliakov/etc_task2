from prettytable import PrettyTable
from tabulate import tabulate

 # сортировка по мат ожиданию (по возрастанию)
def sortByME(outData):
    return sorted(outData, key=lambda data: data[0])


 # извлечение позиций из массивов и представление в строков формате
def viewPositions(arrayPosit):
    strOr = ''
    posit = ''
    for arr1 in arrayPosit:
        posit += strOr
        for el in arr1:
            posit += str(el)+', '
        posit = posit[:len(posit)-2]
        strOr = '\nили\n'
    return posit


 # вывод результатов в виде таблицы
def transmitData(outData):
    columnNames = ['Среднее количество\nотключаемых потребителей',
                   'Количество\nустанавливаемых КА',
                   'Места для установки']

    arrayOutData = []
    for nKA in sortByME(outData):
        arrayOutData.append((round(nKA[0], 2), nKA[1], viewPositions(nKA[2])))

    print()
    print(tabulate(arrayOutData, headers=columnNames,tablefmt='grid',colalign=("center", "center", "center")))