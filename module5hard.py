import time


class User:



    age = 16

    def __init__(self, nickname, password, age):
        self.nickname=nickname
        self.password=password
        self.age=age





class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title=title
        self.duration=duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title





class UrTube:
    def __init__(self):
        self.users= {}
        self.videos= []
        self.current_user = None







    def register(self,nickname, password, age):
        if nickname not in self.users:
            self.users[nickname]=password
            self.current_user = User
            User.age = age





        else:
            print (f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        if nickname in self.users:
            self.users[nickname] = password
            self.current_user = self





    def log_out(self):
        del self.current_user


    def add(self,*args):
        self.videos.append(args)
        return self

    def get_videos(self,search):
        vid=[]
        for i in range(len(self.videos)):
            for j in range(len(self.videos[i])):
                strvideo = str(self.videos[i][j])
                if search.lower() in strvideo.lower():
                    vid.append(self.videos[i][j])
            return vid

    def watch_video(self,search):

        if self.current_user == User:
            for i in range(len(self.videos)):
                for j in range(len(self.videos[i])):
                     if self.videos[i][j].adult_mode or self.current_user.age >= 18:
                         strvideo = str(self.videos[i][j])
                         if search == strvideo:
                             for z in range(1,self.videos[i][j].duration):
                                 time.sleep(1)
                                 print(z)
                                 z+=1
                             time.sleep(1)
                             print("Конец видео")
                     else:
                         print("Вам нет 18 лет, пожалуйста покиньте страницу")
                         break
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")























ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')