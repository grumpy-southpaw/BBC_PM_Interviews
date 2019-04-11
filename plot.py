

from numpy import logical_and, zeros, sum, min, max
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

def main():

    print("running")
    
    data = pd.read_csv("bbc_pm.csv")
    
    n_days = (dt.datetime.strptime(data["Date"][len(data["Date"])-1], '%d/%m/%Y') - dt.datetime.strptime(data["Date"][0], '%d/%m/%Y')).days

    # TODO(jim): this will not work in general and needs correcting
    # it DOES work with the current data though.
    half_progs = (n_days - 5)/7 + 1
    hour_progs = n_days - half_progs 
    total_time = hour_progs + half_progs / 2

    
    parties = ["Con", "Lab", "LD", "Grn", "DUP", "SNP", "PC", "Ind"]
    seats = [314, 245, 11, 1, 10, 35, 4, 10]
    cols = ["b", "r", "y", "g", "purple", "y", "g", "grey"]
    
    times = zeros((2, len(parties)))
    times_norm = zeros((2, len(parties)))
    num = zeros((2, len(parties)))
    
    
    for ii in (0, 1):
        count = 0
        for p in parties:
            times[ii, count] = data["Elapsed"][
                logical_and(data["Party"] == p, data["Senior"] == ii)
                ].sum() / total_time

            times_norm[ii, count] = data["Elapsed"][
                logical_and(data["Party"] == p, data["Senior"] == ii)
                ].sum() / (total_time * seats[count])
                
            num[ii, count] = sum(logical_and(data["Party"] == p, data["Senior"] == ii)) / total_time

            count += 1
            
    plt.figure()
    plt.bar(parties, sum(times, axis = 0), color=cols)
    plt.ylabel("Interview Time / hour (minutes)")
    plt.xlabel("Party")
    plt.savefig("time.png", dpi=300)
    
    
    plt.figure()
    plt.bar(parties, sum(times_norm, axis = 0), color=cols)
    plt.ylabel("Interview Time / No. Seats (minutes / seat)")
    plt.xlabel("Party")
    plt.savefig("time_norm.png", dpi=300)

    parties_num = []
    count_num = []
    cols_num = []

    count = 0
    for p in parties:
        if sum(num[:, count]) > 0:
            parties_num.append(p)
            count_num.append(sum(num[:, count]))
            cols_num.append(cols[count])
        count += 1


    plt.figure()
    plt.bar(parties_num, count_num, color=cols_num)
    plt.ylabel("Number of interviews / hour")
    plt.xlabel("Party")
    plt.savefig("num.png", dpi=300)
    
    x = []
    y = []
    c = []
    
    
    count = 0
    for p in parties:
        
        appending = False
        if any(data["Elapsed"][data["Party"] == p] > 0):
            appending = True
    
        if p == "Ind":
            loop = [0]
        else:
            loop = [1, 0]
        
        for ii in loop:
        
            if ii == 0:
                pos = "backbencher"
            else:
                pos = "leadership"
        
        
            
            t = data["Elapsed"][
                logical_and(data["Party"] == p, data["Senior"] == ii)
                ].sum() / total_time
            
            if appending:
                x.append("{}\n{}".format(p, pos))
                y.append(t)
                c.append(cols[count])
            
        count += 1
            
        
    matplotlib.rcParams.update({'font.size': 5})
    
    plt.figure()
    plt.bar(x, y, color=c)
    plt.ylabel("Time (minutes)")
    plt.xlabel("Party")
    plt.savefig("time_split.png", dpi=600)
    
if __name__ == "__main__":

    main()