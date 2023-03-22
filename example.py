import logging
import re

# logging.basicConfig(level=logging.DEBUG, filename='example.log')

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log를 파일에 출력
file_handler = logging.FileHandler('my.log', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


astarisk = '*'

logger.info('--- Example 1 ---')
for i in range(5):
    print(astarisk, end='')
print()

logger.info('--- Example 2 ---')
for i in range(5):
    for j in range(5):
        print(astarisk, end='')
    print()
print()

logger.info('--- Example 3 ---')
for i in range(5):
    for j in range(i+1):
        print(astarisk, end='')
    print()
print()

tmp_range = 5
logger.info('--- Example 4 ---')
for i in range(tmp_range):
    for j in range(tmp_range-i):
        print(astarisk, end='')
    print()
print()

logger.info('--- Example 5 ---')
for i in range(tmp_range):
    for j in range(4-i):
            print(' ', end='')
    for j in range(i+1):
            print('*', end='')
    print()
print()

logger.info('--- Example 6 ---')
for i in range(tmp_range):
    for j in range(i):
            print(' ', end='')
    for j in range(tmp_range-i):
            print('*', end='')
    print()
print()       

logger.info('--- Example 7 ---')
for i in range(tmp_range):
    for j in range(4-i):
            print(' ', end='')
    for j in range(2*(i+1)-1):
            print('*', end='')
    print("")
print() 

logger.info('--- Example 8 ---')
for i in range(tmp_range):
    for j in range(i):
            print(' ', end='')
    for j in range(2*(5-i)-1):
            print('*', end='')
    print("")
print()

logger.info('--- Example 9 ---')
apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 302, 303], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]
for floor in apart:
    for house in floor:
        if house in arrears:
                continue
        else:
                print("Newspaper delivery: ", house)

logger.info('--- Example 10 replace #re.sub ---')
my_str = "The quick brown fox jumps over the lazy dog."
result = re.sub("the", "a", my_str, flags=re.IGNORECASE)
print(result) # a quick brown fox jumps over a lazy dog.