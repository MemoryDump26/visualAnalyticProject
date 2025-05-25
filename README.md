# Phân tích tần suất chủng SAR-CoV-2
Phần demo của Lê Trọng Bảo - msv:21020608, môn INT3137: Phân tích dữ liệu trực quan.

# Tiền xử lý dữ liệu
Dữ liệu từ covariants.org cần phải convert từ JSON sang dạng CSV để vẽ plot:
1. Giải nén file perCountryData.zip
2. Chạy `python readJson.py`

Trong repo đã bao gồm kết quả bước này (`output.csv')

# Chạy project
1. Kích hoạt venv
2. Cài đặt thư viện: `pip íntall -r requirements.txt`
3. Chạy ứng dụng: `python app.py`
