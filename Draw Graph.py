from matplotlib import pyplot

years =  [2013,2014,2015,2016,2017,2018,2019,2020]
companyA = [6, 5, 5, 7, 8,9 ,3,4]
companyB = [7, 8, 8, 9, 8,7 ,6,5]
companyC = [2, 3, 4, 5, 6, 4, 5,3]

pyplot.style.use('dark_background')
pyplot.plot(years,companyA,color='red',linestyle='-',marker='.')
pyplot.plot(years,companyB,color='green',linestyle='--',marker='.',markersize=10)
pyplot.bar(years,companyC,color='blue',)
#Tên cột Ox
pyplot.xlabel('Year')
#Tên cột Oy
pyplot.ylabel("Profit(USD)")
#Tạo chú thích
pyplot.legend(["companyA","companyB","companyC"])
pyplot.show()