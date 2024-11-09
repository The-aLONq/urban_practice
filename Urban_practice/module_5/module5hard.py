import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.data = {}

    def __str__(self):
        return f"User (nickname='{self.nickname}', age={self.age})"

class Video:

    def __init__(self, title, duration, time_now = 0 , adult_mode = False):
        self.title = title
        self.duration = duration #продолжительность, секунд
        self.time_now = time_now #секунда оставки = 0
        self.adult_mode = adult_mode #ограничение по возврату

class UrTube:

    def __init__(self):
        self.users = {} #список юзеров
        self.videos = [] #список видео
        self.current_user = None #текущий пользователь

    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[nickname].password == hash(password):
                self.current_user = self.users[nickname]
                print(f'Вы вошли к аккаунт {nickname}')
            else:
                print('Вы ввели неверный пароль')
        else:
            print('Такой пользователь не найден')

    def register(self, nickname, password, age):
        if nickname not in self.users:
            user = User(nickname,hash(password), age)
            self.users[nickname] = user
            self.current_user = user
            print(f'{nickname} вы успешно зарегестрировались')
        else:
            print(f'Никнейм {nickname} уже существует')

    def log_out(self):
        if self.current_user:
            print(f'Вы вышли из аккаунта')
            self.current_user = None
        else:
            print('Вы не авторизованы')

    def add(self, *videos):
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                print(f'Видео "{video.title}" уже существует')
            else:
                self.videos.append(video)
                print(f'Видео "{video.title}" добавлено')

    def get_videos(self, search_word):
        search_word = search_word.lower()
        found = False

        for item in self.videos:
            words = item.title.lower().split()
            if search_word in words:
                print(f"Видео найдено: '{item.title}'")
                found = True

        if not found:
            return "Видео не найдено"

    def watch_video(self, name_video):
        if self.current_user:
            video = next((v for v in self.videos if v.title == name_video), None)
            if video:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                else:
                    for i in range(1,video.duration + 1):
                        print(f'Секунда: {i}')
                        time.sleep(1)
                    print('Конец видео')

            else:
                print('Видео не найдено')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')




