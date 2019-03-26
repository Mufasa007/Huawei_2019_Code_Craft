import pandas as pd
import os


def read_txt(txt_path):
    os.chdir(os.getcwd())  # 设置相对路径
    df = pd.read_csv(txt_path,',')
    return df


if __name__ == "__main__":
    txt_path = 'car.txt'
    data = read_txt(txt_path)
    # for i in data:
    #     print(data)
    print(data)
