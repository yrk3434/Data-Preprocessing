'''
한글폰트가 없는 서비스에서 그래프를 그릴 때
한글 폰트를 저장 후 적용
'''

from matplotlib import font_manager
font_path = './malgun.ttf'
font_manager.fontManager.addfont(font_path)
