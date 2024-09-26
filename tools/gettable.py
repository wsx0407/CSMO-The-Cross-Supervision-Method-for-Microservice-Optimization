#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zoey zhu
@file:gettable.py
@time:2024/02/22
"""
import re

def extract_tables_from_sql(sql):
    # 匹配INSERT、UPDATE、DELETE和SELECT语句中的表名
    pattern = re.compile(r'(?:INSERT\s+INTO|UPDATE|DELETE\s+FROM|FROM|JOIN)\s+([^\s;]+)', re.IGNORECASE)
    matches = pattern.findall(sql)
    return matches

# 测试SQL语句
sql = """
    SELECT column1, column2 FROM table1
    JOIN table2 ON table1.id = table2.id
    WHERE table1.column3 = 'value';

    INSERT INTO table3 (column1, column2) VALUES ('value1', 'value2');

    DELETE FROM table4 WHERE column1 = 'value';

    UPDATE table5 SET column1 = 'value' WHERE column2 = 'value';

    SELECT * FROM table6;
"""

tables = extract_tables_from_sql(sql)
print("Tables involved in the SQL statement:", tables)
if __name__ == '__main__':
    pass
