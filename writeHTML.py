import os

textCSS = '''
body, html {
    width : 100%;
    height : 100%;
    margin : 0;
}
body{
    display: flex;
    flex-dirction:column;
    justify-content: center;
    align-items : center;
}
#wrap-value{
}

'''


def openHTML(mean,variance, SD, static):
    textHTML = f'''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <link href="statistics.css" rel="stylesheet">
    <title>statistics</title>
</head>
<body>
    <img src="output.jpg">
    <div id="wrap-value">
        <div>mean is {mean}</div> 
        <div>variance is {variance}</div> 
        <div>standard Deviation is {SD}</div>
    </div>
</body>
</html>
'''

    f = open('src/statistics.html','w')
    f.write(textHTML)
    f.close
    f = open('src/statistics.css','w')
    f.write(textCSS)
    f.close
    os.startfile('src\statistics.html')
    

def delfiles():
    answer = input("Do you want to keep created files saved? 1 : yes 2 : no (default : 1) : ")
    if(answer == '1' or answer == '' ):
        return
    else:
        os.system("del /f src ")
