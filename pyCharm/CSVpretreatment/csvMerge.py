"""
# Raw News Data Merging Code
"""
import pandas as pd
import glob
import os
import gc

"""
# 멀티 자동화 코드 
# pandas.errors.ParserError: Error tokenizing data. C error: out of memory 해결
# 미리 만들어진 pretreated_merge 파일 제외하고 읽어오는 코드 필요
"""

class csvMerge:
    root_input_file = r'D:\BitAcademy\프로젝트\주가예측_프로젝트\-_-\pyCharm\modelTestDB'
    allFile_list = []

    def __init__(self):
        self.allFile_list = glob.glob(os.path.join(self.root_input_file, '*'))

    def start_csvMerge(self):
        for file in self.allFile_list:
            print(file)
            allData = []
            input_file = glob.glob(os.path.join(file, '*'))
            print(input_file)

            for csvFile in input_file:
                print(csvFile)
                df = pd.read_csv(csvFile)
                df.columns = ['date', 'sid1', 'sid2', 'title', 'content', 'url']

                # url기준으로 중복값 제거(url은 unique한 값)
                df = df.drop_duplicates(['url'])

                # content None값 제거
                df = df.dropna(axis=0)

                # date 컬럼을 purchase_date와 purchase_time 컬럼으로 나누기
                df['date'] = df['date'].str.replace('.', '')
                df['content'] = df['content'].str.replace('\t', '')
                df['content'] = df['content'].str.replace('\n', '')

                print(df)
                allData.append(df)

            ouput_path_dir = os.path.join(str(file), 'pretreatmented_merged.csv')
            dataCombine = pd.concat(allData, axis=0, ignore_index=True)
            dataCombine.to_csv(ouput_path_dir, header=False, index=False)

            del allData, input_file, csvFile, df, ouput_path_dir
            gc.collect()

