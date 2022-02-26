import math                                       # math.sin(x) 을 사용하기 위해 import 했음

class Canvas:                                       # 그림을 그릴 Canvas 라는 class 생성
    def __init__(self):                               # Canvas 를 생성하자마자 함께 호출되는 함수
        self.width = 39                                 # 가로길이 39
        self.height = 50                                # 세로길이 50
        self.arr = []                                   # 그림을 저장할 배열
        for i in range(0, self.height):                 # 배열의 생성, 초기화
            self.arr.append([])
            for k in range(0, self.width):
                self.arr[i].append('.')
            
    def draw(self, function, char = '*'):             # 캔버스에 그림을 그리는 함수. 함수(f(x)같은)와 문자(찍을 점의 모양. 기본 모양은 '*')를 매개변수로 받는다
        for x in range(0, self.width):                  # x는 0부터 증가
            y = round(function(x))                      # y = f(x) (y값은 반올림됨)
            if y in range(0, self.height):              # y값이 캔버스의 크기보다 안쪽이면
                self.arr[y][x] = char                   # 캔버스에 y = f(x) 그래프를 그림(점을 찍음)

    def show(self):                                   # 캔버스를 화면에 출력하는 함수
        for i in reversed(range(0, self.height)):       # 프로그래밍 할때는 아래로 갈수록 y값이 증가하니까 뒤집어서 출력할거임. 그래야 제대로 보임
            for k in range(0, self.width):
                print(self.arr[i][k], end = ' ')        # 출력하고 줄바꿈 안함
            print(end = '\n')                           # 다시 줄바꿈을 하도록 바꿈
        print("\n\n")
        
    def clear(self):                                  # 캔버스를 초기화하는(백지로 만드는) 함수
        for i in reversed(range(0, self.height)):
            for k in range(0, self.width):
                self.arr[i][k] = '.'


def f(x):                                             # 예시 함수 
    return (1/16)*(x-16)**2 + 19


canvas = Canvas()

canvas.draw(lambda x : (1/90)*(x-16)**3 + 19, '1')    # 예시 함수 같이 새로운 함수를 만들지 않고 일회용 함수를 만들어서 넘기는 방법 - f(x) = (1/90)*(x-16)**3 + 19 을 만들어준거임
canvas.show()

canvas.draw(f, '2')                                   # 함수와 찍을 점을 넘긴다
canvas.show()

canvas.clear()
canvas.show()

canvas.draw(lambda x : 10*math.sin(x/5) + 16)         # 삼각함수도 그릴수 있다
canvas.show()
