
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



