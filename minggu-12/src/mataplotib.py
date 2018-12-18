#mengimport library Matplotlib Python  
from matplotlib import pyplot as plt
#same as import matplotlib.pyplot as plt
 
#menghasilkan nilai untuk x-axis 
x = [2, 4, 6, 8, 10]
 
#menghasilkan nilai untuk y-axis 
y = [10, 11, 6, 7, 4]
 
#memanggil function untuk plotting the bar chart
plt.bar(x,y)
 
#menampilkan the plot
plt.show()