import pandas as pd
import os
import glob

class copExtract:
    allFile_list = []

    def __init__(self):
        root_input_file = r'D:\BitAcademy\프로젝트\주가예측_프로젝트\-_-\pyCharm\modelTestDB'
        self.allFile_list = glob.glob(os.path.join(root_input_file, '*'))

    def start_copExtract(self):
        for file in self.allFile_list:
            input_file = glob.glob(os.path.join(file, 'pretreatmented_merged.csv'))

            for csvFile in input_file:
                df = pd.read_csv(csvFile)
                df.columns = ['date', 'sid1', 'sid2', 'title', 'content', 'url']
                print(df.head())

                df = df.replace('\r', ' ', regex=True)

                # url기준으로 중복값 제거(url은 unique한 값)
                df = df.drop_duplicates(['url'])

                # content None값 제거
                df = df.dropna(axis=0)

                # date 컬럼을 purchase_date와 purchase_time 컬럼으로 나누기
                df['date'] = df['date'].str.replace('.', '')
                df['content'] = df['content'].str.replace('\t', '')
                df['content'] = df['content'].str.replace('\n', '')

                # title 컬럼으로 각 회사별 데이터만 추출
                LGchemical_title = df['title'].str.contains('LG화학')
                df_LGchemical_title = df[LGchemical_title]
                df_LGchemical_title.to_csv(str(file) + '\\LGchemical_title.csv', index=False, header=False)

                Ottugi_title = df['title'].str.contains('오뚜기')
                df_Ottugi_title = df[Ottugi_title]
                df_Ottugi_title.to_csv(str(file) + '\\Ottugi_title.csv', index=False, header=False)

                KIAcar_title = df['title'].str.contains('기아차')
                df_KIAcar_title = df[KIAcar_title]
                df_KIAcar_title.to_csv(str(file) + '\\KIAcar_title.csv', index=False, header=False)

                SAMSUNGelectronic_title = df['title'].str.contains('삼성전자')
                df_SAMSUNGelectronic_title = df[SAMSUNGelectronic_title]
                df_SAMSUNGelectronic_title.to_csv(str(file) + '\\SAMSUNGelectronic_title.csv', index=False, header=False)

                GSretail_title = df['title'].str.contains('GS리테일')
                df_GSretail_title = df[GSretail_title]
                df_GSretail_title.to_csv(str(file) + '\\GSretail_title.csv', index=False, header=False)

                HYUNDAIconstruct_title = df['title'].str.contains('현대건설')
                df_HYUNDAIconstruct_title = df[HYUNDAIconstruct_title]
                df_HYUNDAIconstruct_title.to_csv(str(file) + '\\HYUNDAIconstruct.csv', index=False, header=False)

                CJdaehantongun_title = df['title'].str.contains('CJ대한통운')
                df_CJdaehantongun_title = df[CJdaehantongun_title]
                df_CJdaehantongun_title.to_csv(str(file) + '\\CJdaehantongun.csv', index=False, header=False)

                KBfinace_title = df['title'].str.contains('KB금융')
                df_KBfinace_title = df[KBfinace_title]
                df_KBfinace_title.to_csv(str(file) + '\\KBfinace_title.csv', index=False, header=False)

                SAMSUNGlife_title = df['title'].str.contains('삼성생명')
                df_SAMSUNGlife_title = df[SAMSUNGlife_title]
                df_SAMSUNGlife_title.to_csv(str(file) + '\\SAMSUNGlife_title.csv', index=False, header=False)

                HANMImedicine_title = df['title'].str.contains('한미약품')
                df_HANMImedicine_title = df[HANMImedicine_title]
                df_HANMImedicine_title.to_csv(str(file) + '\\HANMImedicine_title.csv', index=False, header=False)