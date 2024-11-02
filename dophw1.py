import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hashed = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == password_hashed:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео с названием '{video.title}' уже существует.")

    def get_videos(self, search_keyword):
        result = [video.title for video in self.videos if search_keyword.lower(
        ) in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено.")
            return
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        print(f"Начало просмотра видео: '{video.title}'")
        for second in range(video.duration):
            time.sleep(1)
            video.time_now += 1
            print(f"Сейчас: {video.time_now} секунд")

        print("Конец видео")
        video.time_now = 0


# Пример использования
if __name__ == "__main__":
    urtube = UrTube()
    # Регистрация пользователей
    urtube.register("user1", "password123", 20)
    urtube.register("user2", "password456", 16)
    # Вход пользователя
    urtube.log_in("user1", "password123")
    # Добавление видео
    video1 = Video("Лучший язык программирования 2024 года",
                   10, adult_mode=False)
    video2 = Video("Another Video", 20, adult_mode=True)
    urtube.add(video1, video2)
    # Получение видео
    print(urtube.get_videos('Лучший язык программирования 2024 года'))
    # Проигрывание видео
    urtube.watch_video("Лучший язык программирования 2024 года")
    # Попытка посмотреть видео с ограничением по возрасту
    urtube.log_out()  # Выход пользователя
    urtube.log_in("user2", "password456")  # Вход другого пользователя
    urtube.watch_video("Another Video")
    urtube.log_out()  # Выход пользователя
    urtube.watch_video("Лучший язык программирования 2024 года")
