'''
pandas 데이터를 sql처럼 필터링하기
'''
from pandasql import sqldf

query = "SELECT * FROM df WHERE col = 'value1'"

result = sqldf(query)
