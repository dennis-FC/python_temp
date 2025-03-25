
def insert_one(table, where, insert_contents):
   # 構建插入的列名和對應的值
    columns = ', '.join(insert_contents.keys())
    values = ', '.join([f"'{v}'" for v in insert_contents.values()])
    print(values)
    
    # sql = f"""
    #     BEGIN
    #         IF NOT EXISTS (SELECT 1 FROM {table} WHERE {where}) THEN
    #             INSERT INTO {table} ({columns}) VALUES ({values});
    #         END IF;
    #     END;
    #     """

def insert_many(table, where, insert_contents):
     # 構建插入的列名
        if insert_contents:
            columns = ', '.join(insert_contents[0].keys())  # 假設所有字典有相同的鍵

        # 準備所有要插入的值
        for content in insert_contents:
            values = ', '.join([f"'{v}'" for v in content.values()])
            print(values)

            
            # 使用where條件來檢查是否存在相同的資料，若不存在則插入新資料
            # sql = f"""
            # BEGIN
            #     IF NOT EXISTS (SELECT 1 FROM {table} WHERE {where}) THEN
            #         INSERT INTO {table} ({columns}) VALUES ({values});
            #     END IF;
            # END;
            # """
            
        #     try:
        #         # 執行每一條插入語句
        #         cursor.execute(sql)
        #     except cx_Oracle.DatabaseError as e:
        #         print(f"Database error occurred: {e}")
        #         connection.rollback()  # 如果出錯，回滾事務
        #         break  # 當發生錯誤時停止插入
        # else:
        #     # 提交事務 (只有當所有插入成功後才提交)
        #     connection.commit()

insert_contents = { "id": "AAA", "REMARK": "ABC", "VALUE": "CCC" }
insert_contents = { "id": 3}
insert_contents = [
    { "id": "AAA", "REMARK": "ABC", "VALUE": "CCC" },
    { "id": "AAA2", "REMARK": "ABC2", "VALUE": "CCC2" }
]
#insert_one("your_table_name", "id = 'AAA'", insert_contents)
insert_many("your_table_name", "id = 'AAA'", insert_contents)


#deepseek
# import cx_Oracle
# import os

# # 設置 Oracle 客戶端路徑（如果需要）
# os.environ["NLS_LANG"] = "AMERICAN_AMERICA.WE8ISO8859P1"  # 強制使用 ISO-8859-1 連接

# # 建立數據庫連接
# dsn = cx_Oracle.makedsn("your_host", "your_port", service_name="your_service_name")
# conn = cx_Oracle.connect(user="your_username", password="your_password", dsn=dsn)

# try:
#     cursor = conn.cursor()
    
#     # 直接查詢數據（將以 ISO-8859-1 解碼）
#     sql = "SELECT your_column FROM your_table"
#     cursor.execute(sql)
    
#     for row in cursor:
#         wrong_text = row[0]
#         if wrong_text:
#             # 將錯誤解碼的字符串重新編碼為 ISO-8859-1 bytes
#             bytes_data = wrong_text.encode('iso-8859-1')
            
#             # 用正確的 MS950 (Big5) 編碼解碼
#             try:
#                 correct_text = bytes_data.decode('big5')
#                 print(f"Correct text: {correct_text}")
#             except UnicodeDecodeError:
#                 print(f"Decoding failed for: {bytes_data}")
#         else:
#             print("NULL value")

# finally:
#     conn.close()

#chatgpt
# import cx_Oracle

# # 建立数据库连接
# connection = cx_Oracle.connect(
#     user="your_username",
#     password="your_password",
#     dsn="your_dsn",
#     encoding="UTF-8",  # 确保客户端编码是 UTF-8
#     nencoding="UTF-8"  # NCHAR 字符集编码为 UTF-8
# )

# cursor = connection.cursor()

# # 假设查询中文数据
# cursor.execute("SELECT your_column FROM your_table")
# rows = cursor.fetchall()

# for row in rows:
#     # 假设 row[0] 包含被错误解码的中文数据
#     # 首先，将其重新编码为字节数据（假设它被解码为 ISO-8859-1）
#     incorrect_data = row[0]
    
#     # 通过 ISO-8859-1 编码重新编码为字节数据，再用 MS950 解码
#     corrected_data = incorrect_data.encode('ISO-8859-1').decode('ms950')
    
#     print(corrected_data)


