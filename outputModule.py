from prettytable import PrettyTable

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
        strOr = ' или '
    return posit


 # вывод результатов в виде таблицы
def transmitData(outData):
    columnNames = ['Среднее кол-во отключаемых потребителей',
                   'Кол-во устанавливаемых КА',
                   'Места для установки']

    columns = len(columnNames)
    table = PrettyTable(columnNames)
    arrayOutData = []
    for nKA in sortByME(outData):
        arrayOutData.append(round(nKA[0], 2))
        arrayOutData.append(nKA[1])
        arrayOutData.append(viewPositions(nKA[2]))
        table.add_row(arrayOutData)
        arrayOutData.clear()
    print(table)