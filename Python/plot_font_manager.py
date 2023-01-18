'''
한글폰트가 없는 서비스에서 그래프를 그릴 때
한글 폰트를 저장 후 적용
'''
import matplotlib
from matplotlib import font_manager
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font',family=font_name)
font_manager.fontManager.addfont(font_path)
