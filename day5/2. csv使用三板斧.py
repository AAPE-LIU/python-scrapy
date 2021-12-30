import csv
f = open('test.csv',mode='w')
csvwritter = csv.writer(f)
csvwritter.writerow([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
f.close()

# csv写入数据的时候会自动使用  ','  将列表中的内容分隔开
