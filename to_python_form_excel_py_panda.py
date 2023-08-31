

from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.colors as clm
data=pd.read_excel(r'D:\Desktop\data processing\12 Pomiary REMAG 11_05_2023\RejestratorCisnien11_05_23_10_53_39   ax20.xlsx',usecols='A,C,E,H,K,N,Q')
#print(data.head)
files_lst=
""" x_values=data[0]
y_values=data[1]
plt.plot_date(x_values,y_values) """

#import pandas as pd
#import matplotlib.pyplot as mp

# take data
#data = pd.read_csv("Bestsellers.csv")

# form dataframe
#data = data.head()

# df = pd.DataFrame(data, columns=["Data", "E_IL_percent", "F_II_percent"])

# plot the dataframe
# df.plot(x="Data", y=["E_IL_percent", "F_II_percent"], kind="line", figsize=(15, 13))

# plotowanie
x = data["Data"]
y_IL = data["E_IL_percent"]
y_II = data["F_II_percent"]
y_gsig=data["G-sig"]
y_hsig=data["H-sig"]
y_isig=data["I-sig"]
y_jsig=data["J-sig"]

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(x,y_gsig, label="sruba bok", color="tab:pink")
ax.plot(x,y_hsig, label="sruba gora", color="b")
ax.plot(x,y_isig, label="żebro", color="b")
ax.plot(x,y_jsig, label="tłoczysko siłownika", color="b")

plt.title('Przebieg zarejestrowanych sygnałów')
plt.ylim(bottom=-30, top=50)
plt.xlabel('czas (s)')
plt.xticks(rotation=90)
ax.set_ylabel('Naprężenia [MPa]', color='k')
plt.grid(True)

ax2=ax.twinx()
ax2.plot(x, y_IL, label="E_IL_percent", linestyle="--", color="k")
ax2.plot(x, y_II, label="F_II_percent", linestyle="--", color="g")

ax2.set_ylabel('Wysunięcie siłownika [%]', color='r')
ax2.tick_params(axis='y', labelcolor='r')
ax2.set_ylim(0, 100)

# informacje opisowe


# ustawienia wyświetlania
#plt.xticks(fontsize=8)
#ax.xaxis.set_major_locator(mdates.SecondLocator(bysecond=range(5)))
#plt.gcf().autofmt_xdate()
#ax.set_xticks(np.arange(min(x),max(x),1))
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

