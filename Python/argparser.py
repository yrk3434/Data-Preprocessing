'''
실행파일 내부
'''

import argparser

parser = argparser.ArgumentParser()
parser.add_argument("--input1", type=str, default = 'myinput')
args = parser.parse_args()

input1 = args.input1

'''
실행: 터미널
'''
python ./path/run_file.py --input1 'new'

'''
실행: 주피터 노트북
'''
exec("python ./path/run_file.py --input1 'new'") # 큰따옴표, 작은 따옴표 주의
