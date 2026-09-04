from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
import csv
from selenium.common.exceptions import TimeoutException

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
def fill(name,stt):
    xpaths = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{}]/div/div/div[2]/div/div[1]/div/div[1]/input'.format(stt+1),
        #//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{}]/div/div/div[2]/div/div[1]/div[2]/textarea'.format(stt+1)
        #//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]/textarea
    ]

# Biến để lưu phần tử tìm thấy
    element = None

    # Thử từng XPath
    for xpath in xpaths:
        try:
            # Chờ tối đa 10 giây để phần tử với xpath này xuất hiện
            element = WebDriverWait(driver, 0.2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            break
        except TimeoutException:
            continue
    element.send_keys(name) 

def filla(name):
    xpaths = [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    ]

# Biến để lưu phần tử tìm thấy
    element = None

    # Thử từng XPath
    for xpath in xpaths:
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            break  # Nếu tìm thấy phần tử, thoát vòng lặp
        except:
            continue
    

    if element is None:
        raise Exception("Không tìm thấy phần tử phù hợp với bất kỳ XPath nào.")
    element.send_keys(name)
def tn(ques1,stt,number_answers):
    vitri = 1
    my_string = []
    radio_buttons = []
    
    for i in range(1, number_answers+1):
        my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div[1]/div/span/div/div[{i}]/label/div/div[1]/div')

        radio_buttons.append(WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, my_string[i-1]))
        ))
        
        for radio in radio_buttons[i-1]:
            if radio.get_attribute("data-value") == ques1 or str(vitri) == ques1:
                driver.execute_script("arguments[0].click();", radio)
        vitri += 1
def mntx(ques1,stt,number_answers):

    
    k=3
    vitri=1                
    radio2_select = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[1]/div[1]/div[1]'))) #lấy xpath ô chọn
    for radio2 in radio2_select:
        driver.execute_script("arguments[0].click();", radio2)
    time.sleep(1)
    my_string = []
    radio_buttons = []
    for i in range(1, number_answers+1):
        my_string.append(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[2]/div[{k}]')   
                        #/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt}]/div/div/div[2]/div/div[1]/div[1]/div[1]
        
        #câu trắc nghiệm 
        radio_buttons.append(WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[i-1])))) #lấy xpath ô trắc nghiệm 1
        for radio in radio_buttons[i-1]:
            if radio.get_attribute("data-value") == ques1 or str(vitri) == ques1:
                driver.execute_script("arguments[0].click();", radio)
                return
        vitri=vitri+1
        k=k+1
def hk(*args, stt):

    compare_values = list(args)
    number_answers = len(compare_values)  # Số câu trả lời sẽ tự động bằng số lượng tham số
    vitri=1
    my_string = []
    for i in range(1, number_answers+1):
        my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div[1]/div[{i}]/label/div/div[1]')
                        #/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label/div/div[1]
        #câu trắc nghiệm 
        radio_buttons = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[i-1]))) #lấy xpath ô trắc nghiệm 1
        for radio in radio_buttons:
            for value in compare_values[i-1]:
                if radio.get_attribute("data-answer-value")[0] == value[0] or str(vitri) == value:
                    driver.execute_script("arguments[0].click();", radio)
                    break
def day(month, date, year,stt):

    #ngày tháng năm/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input
    xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
    month_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))) #xpath tháng
    date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))) #xpath ngày
    year_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))) #xpath năm
    input_array = [month_input,date_input,year_input]
    for i in range(len(input_array)):
        input_array[i].clear()
        input_array[i].send_keys([month,date, year][i])
def gio(hour, minute,stt):
    hour_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'))) #xpath giờ
    minute_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input'))) #xpath phút
    input_array = [hour_input,minute_input]
    for i in range(len(input_array)):
        input_array[i].clear()
        input_array[i].send_keys([hour, minute][i])
def pvtt(a,stt,number_answers):   
    my_string = []
    radio_buttons = []
    for i in range(1, number_answers+1):
        my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div[1]/span/div/label[{i}]/div[2]/div/div')
        
        
        #câu trắc nghiệm 
        radio_buttons.append(WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[i-1])))) #lấy xpath ô trắc nghiệm 1
        for radio in radio_buttons[i-1]:
            if radio.get_attribute("data-value") == a:
                driver.execute_script("arguments[0].click();", radio)
def hk_grid(*args, stt, colums):
    compare_values = [list(arg) for arg in args]  # Chia thành các hàng (số câu hỏi)
    rows = len(compare_values)
    vitri=1
    k=2
    my_string = []
    radio_buttons = []
    for j in range(1, rows + 1):
        for i in range(1, colums +1):
            index = (j-1) * colums + (i-1)
            my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[1]/div/div[{k}]/span/div[{i+1}]/div/div')
            radio_buttons.append(WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[index])))) #lấy xpath ô trắc nghiệm 1
            for radio in radio_buttons[index]:
                for value in compare_values[j-1]:
                    if radio.get_attribute("data-value") == value  or str(vitri) == value:
                        driver.execute_script("arguments[0].click();", radio)
                        break
            vitri=vitri+1                        
        vitri=1
        k=k+2
def hk_luoi(*args, stt, rows, colums):
    compare_values = [list(args[i:i + colums]) for i in range(0, len(args), colums)]  # Chia thành các hàng
    vitri = 1
    k = 2
    my_string = []
    radio_buttons = []
    
    
    vitri=1
    k = 2
    my_string = []
    for j in range(1, rows+1):
        radio_buttons = []
        for i in range(1, colums + 1):
            index = (j-1) * colums + (i-1)
            my_string.append(f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[{stt+1}]/div/div/div[2]/div/div[1]/div/div[{k}]/label[{i}]/div/div')
            radio_buttons.append(WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, my_string[index])))) 
            for radio in radio_buttons[i-1]:
                for value in compare_values[j-1]:
                    if radio.get_attribute("data-answer-value") == value  or str(vitri) == value:
                        driver.execute_script("arguments[0].click();", radio)
                        break
            vitri=vitri+1                        
        vitri=1
        k += 2

def fill_form(name,stt):
    fill(name,stt)

def tracnghiem(ques1, stt, number_answers):
    tn(ques1,stt,number_answers)

def menuthaxuong(ques1, stt, number_answers):
    mntx(ques1,stt,number_answers)

def hopkiem(*args, stt):
    hk(*args, stt=stt)

def date(month, date, year,stt):
    day(month, date, year,stt)

def hour(hour, minute,stt):
    gio(hour, minute,stt)
    
def phamvituyentinh(a,stt,number_answers):
    pvtt(a,stt,number_answers)
          
def luoitracnghiem(*args, stt, colums):
    hk_grid(*args, stt=stt, colums=colums)

def luoihopkiem(*args, stt, rows, colums):
    hk_luoi(*args, stt=stt, rows=rows, colums=colums)
import os

# ... (Previous imports) ...

try:
    if not os.path.exists("test.csv"):
        print("ERROR: test.csv file not found!")
        exit(1)

    try:
        with open("index.txt", "r") as f:
            content = f.read().strip()
            if not content:
                index = 0
            else:
                index = int(content)
    except FileNotFoundError:
        index = 0
    except ValueError:
        index = 0

    # Mở và đọc đúng dòng trong CSV
    with open("test.csv", encoding="utf-8-sig") as file:
        reader = list(csv.reader(file))
        total_rows = len(reader)

    if total_rows == 0:
        print("File CSV rỗng!")
        exit(1)

    if index >= total_rows:
        print(f"STOPPING: Out of data! Current index {index} >= Total rows {total_rows}. Please add more data to test.csv.")
        exit(1)

    row = reader[index]
    print(f"Processing row index {index}: {row[:3]}...") # Log progress

except Exception as e:
    print(f"CRITICAL ERROR in initialization: {e}")
    exit(1)

time.sleep(1)
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfjaionNaeeeBWyJOV_vp_qOUIOK7cLe0CgnLARUZzowUf5YA/viewform')
time.sleep(0.2)
filla(row[0])
tracnghiem(row[1],1,2)
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
driver.execute_script("arguments[0].click();", next_button)
time.sleep(0.2)
tracnghiem(row[2],1,6)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.2)
tracnghiem(row[3],1,2)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.2)
tracnghiem(row[4],1,5)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.2)
tracnghiem(row[5],1,5)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.2)
tracnghiem(row[6],1,5)
hopkiem(row[7],row[8],row[9],row[10],row[11],row[12],row[13],stt=2)
hopkiem(row[14],row[15],row[16],row[17],row[18],row[19],row[20],stt=3)
tracnghiem(row[21],4,6)
hopkiem(row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],stt=5)
phamvituyentinh(row[30],6,5)
luoitracnghiem(row[31],row[32],row[33],row[34],stt=7,colums=5)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.2)
fill_form(row[35],1)
hopkiem(row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[43],row[44],row[45],row[46],row[47],row[48],stt=2)
hopkiem(row[49],row[50],row[51],row[52],row[53],row[54],row[55],row[56],stt=3)
hopkiem(row[57],row[58],row[59],row[60],row[61],row[62],row[63],stt=4)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.2)
luoitracnghiem(row[64],row[65],row[66],stt=2,colums=5)
tracnghiem(row[67],3,2)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
if row[68]=="1":
    tracnghiem(row[68],2,3)
    hopkiem(row[69],row[70],row[71],row[72],row[73],row[74],row[75],row[76],row[77],stt=3)
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(0.2)
    luoitracnghiem(row[78],row[79],row[80],row[81],row[82],row[83],stt=1,colums=5)
    luoitracnghiem(row[84],row[85],row[86],row[87],row[88],row[89],row[90],row[91],row[92],row[93],row[94],stt=2,colums=5)
    luoitracnghiem(row[95],row[96],row[97],row[98],row[99],row[100],row[101],row[102],row[103],row[104],stt=3,colums=5)
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(0.2)
    luoitracnghiem(row[105],row[106],row[107],stt=1,colums=5)
    hopkiem(row[108],row[109],row[110],row[111],row[112],row[113],row[114],row[115],row[116],stt=2)
    tracnghiem(row[117],3,5)
    hopkiem(row[118],row[119],row[120],row[121],row[122],row[123],row[124],stt=4)
    tracnghiem(row[125],6,5)
    phamvituyentinh(row[126],7,5)
    luoitracnghiem(row[127],row[128],row[129],row[130],stt=8,colums=5)
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
    driver.execute_script("arguments[0].click();", submit_button)
else:  
    tracnghiem(row[131],1,3)
    hopkiem(row[132],row[133],row[134],row[135],row[136],row[137],row[138],row[139],row[140],row[141],stt=2)
    luoitracnghiem(row[142],row[143],row[144],row[145],row[146],row[147],stt=3,colums=5)
    tracnghiem(row[148],4,4)
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
    driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.2)
hopkiem(row[149],row[150],row[151],row[152],row[153],row[154],row[155],row[156],row[157],stt=1)
luoitracnghiem(row[158],row[159],row[160],row[161],row[162],row[163],stt=2,colums=5)
hopkiem(row[164],row[165],row[166],row[167],row[168],row[169],row[170],row[171],row[172],row[173],row[174],stt=3)
hopkiem(row[175],row[176],row[177],row[178],row[179],row[180],row[181],stt=4)
hopkiem(row[182],row[183],row[184],row[185],row[186],row[187],stt=5)
hopkiem(row[188],row[189],row[190],row[191],row[192],row[193],stt=6)
luoitracnghiem(row[194],row[195],row[196],row[197],row[198],row[199],row[200],row[201],stt=7,colums=5)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.2)
tracnghiem(row[202],1,4)
tracnghiem(row[203],2,2)
tracnghiem(row[204],3,4)
tracnghiem(row[205],4,6)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(0.6)
time.sleep(1)

# Update index IMMEDIATELY after submission attempt
with open("index.txt", "w") as f:
    f.write(str(index + 1))
print(f"Updated index to {index + 1}")

time.sleep(random.randint(60,100))     
driver.close()













