import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import requests, json, pandas, xlsxwriter,time
from datetime import datetime
#value = "AAVE_BTC"
value = str(input("Please enter what cryptocurrency you would like to monitor today: "))
style.use("fivethirtyeight")
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)



def animate(i):
    lsp = []
    ysp = []
    xsp = []
    dfp = pandas.read_excel(r"C:\Users\User\Desktop\prices.xlsx", engine='openpyxl')
    print("1")
    dfp = dfp.T
    for col in dfp.columns:
        col_lsp = dfp[col].tolist()
        lsp.append(col_lsp)
    print(lsp)
    for i in lsp:
        for name in i:
            if name == value:
                ysp = i
    for i in dfp.index:
        xsp.append(i)
    xsp.pop(0)
    cryptonameforgraph = ysp[0]
    ysp.pop(0)
    ax1.clear()
    ax1.plot(xsp, ysp, label = "Price of ")
    ax1.set_title("price "+cryptonameforgraph, fontsize=12)

    lsv = []
    ysv = []
    xsv = []
    dfv = pandas.read_excel(r"C:\Users\User\Desktop\volumes.xlsx",engine='openpyxl')
    dfv = dfv.T
    for col in dfv.columns:
        col_lsv = dfv[col].tolist()
        lsv.append(col_lsv)
    print(lsv)
    for i in lsv:
        for name in i:
            if name == value:
                ysv = i
    for i in dfv.index:
        xsv.append(i)
    xsv.pop(0)
    cryptonameforgraph = ysv[0]
    ysv.pop(0)
    ax2.clear()
    ax2.plot(xsv, ysv, label = "Volume of ")
    ax2.set_title("volume " + cryptonameforgraph, fontsize=12)

    lsm = []
    ysm = []
    xsm = []
    dfm = pandas.read_excel(r"C:\Users\User\Desktop\marketcap.xlsx",engine='openpyxl')
    dfm = dfm.T
    for col in dfm.columns:
        col_lsm = dfm[col].tolist()
        lsm.append(col_lsm)
    print(lsm)
    for i in lsm:
        for name in i:
            if name == value:
                ysm = i
    for i in dfm.index:
        xsm.append(i)
    xsm.pop(0)
    cryptonameforgraph = ysm[0]
    ysm.pop(0)
    ax3.clear()
    ax3.plot(xsm, ysm, label = "Volume of ")
    ax3.set_title("Market cap of " + cryptonameforgraph, fontsize=12)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.tight_layout()
plt.show()

