import pandas as pd
import requests
from pymongo import MongoClient
import time
import re

"""
# Đọc file CSV
df = pd.read_csv('/home/doanhuy/Desktop/Project_2/products-id.csv')  # File chứa cột 'id'

# Kết nối với MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['project_02']  # Tên cơ sở dữ liệu
collection = db['products']  # Tên collection

batch_size = 1000  # Kích thước batch insert
batch_data = []  # Danh sách để lưu dữ liệu trước khi insert vào MongoDB
n = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json'
}
# Lặp qua từng ID và lấy dữ liệu
for product_id in df['id'][1:]:
    url = f'https://api.tiki.vn/product-detail/api/v1/products/{product_id}'
    response = requests.get(url, headers=headers)
    time.sleep(0.1)  # Điều chỉnh thời gian chờ phù hợp
    # Optional: Sleep để tránh quá tải API
    if response.status_code == 200:
        # Lấy dữ liệu JSON từ API
        data = response.json()
        description = data.get('description')
        if description:
            description = re.sub(r'<.*?>', '', description)
        else:
            description = ''

        # Lọc các trường cần thiết
        filtered_data = {
            'id': data.get('id'),
            'name': data.get('name'),
            'url_key': data.get('url_key'),
            'price': data.get('price'),
            'description': description,
            'images': data.get('images')
        }

        # Thêm vào danh sách batch
        batch_data.append(filtered_data)

        # Nếu số lượng dữ liệu đạt tới kích thước batch, thực hiện insert
        if len(batch_data) == batch_size:
            collection.insert_many(batch_data)
            batch_data = []  # Reset batch sau khi insert
            print(f"Đã insert {n*1000} sản phẩm vào MongoDB")
            n += 1

    else:
        print(f'Lỗi khi lấy dữ liệu cho ID {product_id}: {response.status_code}')

# Insert bất kỳ sản phẩm nào còn lại trong batch_data sau khi kết thúc vòng lặp
if batch_data:
    collection.insert_many(batch_data)
    print(f"Đã insert phần còn lại vào MongoDB")

"""



import requests
import browser_cookie3
#import cloudscraper

#scraper = cloudscraper.create_scraper()
#url = 'https://api.tiki.vn/product-detail/api/v1/products/138083218'
url = 'https://www.zenrows.com/'
#url = 'https://www.glamira.com/sitemap.xml'
#url = 'https://tpc.googlesyndication.com/simgad/12327616521430979548'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',

}


try:
    response = requests.get('https://www.glamira.com/' ,timeout=10)  # Thời gian timeout là 10 giây
    #response = scraper.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        print("Thành công")
    else:
        print(f'Lỗi khi lấy dữ liệu: {response.status_code}')
    r = requests.get('https://www.zenrows.com/headers')
    print(r.text)

except requests.exceptions.Timeout:
    print("Request đã bị timeout, kiểm tra kết nối mạng hoặc tăng thời gian timeout.")
except requests.exceptions.RequestException as e:
    print(f"Lỗi khi thực hiện request: {e}")



