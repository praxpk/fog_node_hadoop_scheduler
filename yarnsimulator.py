import pandas as pd
import matplotlib.pyplot as plt
import json
file = "realtimetrack_capacity.json"



def return_list_keys():
    with open(file) as jf:
        data = json.load(jf)
        a_list=["jvm.free.memory","jvm.max.memory","jvm.total.memory","running.applications","scheduler.handle.timecost",
                "scheduler.handle-NODE_ADDED.timecost",
                "scheduler.handle-NODE_UPDATE.timecost","scheduler.handle-NODE_LABELS_UPDATE.timecost"]
        list_keys = []
        for i in data:
            for key, value in i.items():
                if (key not in list_keys and key in a_list):
                    list_keys.append(key)

        return list_keys


def header_vs_time(header):
    with open(file) as jf:
        data = json.load(jf)
        time = []
        h_list = []
        for i in data:
            for key, value in i.items():
                if key == "time":
                    time.append(value)
                elif key == header:
                    h_list.append(value)
        return [time, h_list]


def plot_dataframe(df, index):
    ax = plt.gca()

    df.plot(kind='line', x='time', y=index, color='red', ax=ax)

    plt.show()


def plot_vs_time():
    list_keys = return_list_keys()
    result_list=[]
    for i in list_keys:
        if i != "time":
            print(" ", " ", "time", " ", i)
            header_time = header_vs_time(i)
            list1 = header_time[0]
            list2 = header_time[1]
            df1 = pd.DataFrame({"time": list1})
            df2 = pd.DataFrame({i: list2})
            df3 = pd.concat([df1, df2], axis=1, join='inner')
            plot_dataframe(df3, i)
            result_list.append(df3)
    return result_list


def plot_comparison(df1,df2):

    ax1 = plt.gca()
    ax2= plt.gca()
    for (i,j) in df1.iteritems():
        if(i!="time"):
            df1.plot(kind='line', x='time', y=i, color='red', ax=ax1)
    for (i,j) in df2.iteritems():
        if(i!="time"):
            df2.plot(kind='line', x='time', y=i, color='blue', ax=ax2)

    plt.show()




def main():
    result_list = plot_vs_time()
    for i in result_list:
        for j in result_list:
            plot_comparison(i,j)


if __name__ == '__main__':
    main()
