import ddddocr
import requests
import urllib3
from PIL import Image

# 禁用 urllib3 的 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#獲取驗證碼圖片，並儲存
captcha_url = "https://apmis.epa.gov.tw/air2/RegFacAdmin/getCaptcha"
response = requests.get(captcha_url, verify=False)
with open("captcha.png", "wb") as f:
    f.write(response.content)

# 開啟圖片
image = Image.open('captcha.png')

#使用ddddocr進行OCR辨識，beta版為更先進OCR模型，但還在測試中
ocr = ddddocr.DdddOcr(beta=True)
#避免png圖片被Alpha通道干擾
result = ocr.classification(image, png_fix=True)

#將辨識結果中的英文全部轉換成大寫
result_uppercase = ''.join(char.upper() if char.isalpha() else char for char in result)

#OCR辨識結果
print(f"ddddocr辨識結果: {result_uppercase}")