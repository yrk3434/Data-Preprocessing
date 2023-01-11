'''
패키지만들기 - 경로
'''

# -- 절대경로 -- #
import sys
sys.path.append(path) # path: 모듈 최상단 경로

# -- 상대경로 -- #
# 참고: https://dojang.io/mod/page/view.php?id=2449
# 모듈 내 하위 경로마다 __init__.py 필요
# .을 통해 경로 참조 
# ex. 동일 폴더 내 다른 함수 부르려면 from . import function1
# ex. 두 개 상위 폴더 내 다른 함수 부르려면 from ..module1 import function1

'''
module path
'''
import os
path = os.path.abspath(a_module.__file__)

path = Path(os.path.dirname(a_module.__file__)).absolute()


'''
add file path
'''
from os.path import dirname, abspath
sys.path.append(dirname(abspath(__file__)))
