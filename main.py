from writeHTML import openHTML, delfiles
from calculate import mean, variance1, SD 
from createStatistic import createStatic
import pandas as pd

if __name__ == '__main__':
    
    #파일 불러오기
    print('waring: sheet data of A line and B line MUST BE random_variable and probability, Please check the example xlsx file.')
    while True:
        try:
            filePath, sheetName = input('File path & Sheet name : ').split()
            excelData = pd.read_excel( filePath,sheet_name=sheetName, engine='openpyxl')
            break
        except FileNotFoundError :
            print('Faile file path to open')
        except ValueError as m :
            print(m)

    excelData =  pd.DataFrame(excelData)
    RV, pro = list(excelData.columns) ,excelData.iloc[0]
    colLen = len(RV)

    #그래프 생성 및 계산 -> html 열기
    openHTML(mean(RV, pro), variance1(RV, pro), SD(RV, pro), createStatic(RV,pro, colLen))
    delfiles()
#E:\programing\a.xlsx