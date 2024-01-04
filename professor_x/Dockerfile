# 基於 Python 官方映像
FROM python:3.8

# 設置環境變數
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 創建工作目錄
WORKDIR /app

# 安裝依賴
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 拷貝專案文件
COPY . /app/

# 啟動命令
CMD ["gunicorn", "professor_x.wsgi:application", "--bind", "0.0.0.0:8000"]
