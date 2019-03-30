

from numpy import logical_and, zeros, sum
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def main():

    print("running")

    data = pd.read_csv("bbc_pm.csv")
    
    parties = ["Con", "Lab", "LD", "Grn", "DUP", "SNP", "PC", "Ind"]
    seats = [314, 245, 11, 1, 10, 35, 4, 10]
    cols = ["b", "r", "y", "g", "purple", "y", "g", "grey"]
    
    times = zeros((2, len(parties)))
    times_norm = zeros((2, len(parties)))
    num = zeros((2, len(parties)))
    
    #axis_font = {'fontname':'Arial', 'size':'8'}
    
    for ii in (0, 1):
        count = 0
        for p in parties:
            times[ii, count] = data["Elapsed"][
                logical_and(data["Party"] == p, data["Senior"] == ii)
                ].sum()

            times_norm[ii, count] = data["Elapsed"][
                logical_and(data["Party"] == p, data["Senior"] == ii)
                ].sum() / seats[count] 
                
            num[ii, count] = sum(logical_and(data["Party"] == p, data["Senior"] == ii))

            count += 1
            
    plt.figure()
    plt.bar(parties, sum(times, axis = 0), color=cols)
    plt.ylabel("Time (minutes)")
    plt.xlabel("Party")
    plt.savefig("time.png", dpi=300)
    
    
    plt.figure()
    plt.bar(parties, sum(times_norm, axis = 0), color=cols)
    plt.ylabel("Time / No. Seats (minutes / seat)")
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
    plt.ylabel("Number of interviews")
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
    
        for ii in (1, 0):
        
            if ii == 0:
                pos = "backbencher"
            else:
                pos = "leadership"
        
        
            
            t = data["Elapsed"][
                logical_and(data["Party"] == p, data["Senior"] == ii)
                ].sum()
            
            if appending:
                x.append("{}\n{}".format(p, pos))
                y.append(t)
                c.append(cols[count])
            
        count += 1
            
        
    matplotlib.rcParams.update({'font.size': 6})
    
    plt.figure()
    plt.bar(x, y, color=c)
    plt.ylabel("Time (minutes)")
    plt.xlabel("Party")
    plt.savefig("time_split.png", dpi=300)
    
if __name__ == "__main__":

    main()