from ursina import *
import time as time_module

class SplashScreen:
    """
    Экран загрузки с анимацией и индикатором прогресса.
    """
    def __init__(self, on_complete=None):
        self.on_complete = on_complete
        self.progress = 0
        self.loading_steps = [
            "Загрузка...",
            "Создание объектов...",
            "Настройка сцены...",
            "Почти готово...",
            "Готово!"
        ]
        self.current_step = 0
        self.start_time = time_module.time()
        self.finished = False

        # Создаём UI элементы
        self._create_ui()

    def _create_ui(self):
        """Создаёт UI элементы splash-экрана строго на camera.ui"""

        # Черный фон во весь экран
        self.overlay = Entity(
            parent=camera.ui,
            model='quad',
            scale=(2, 2),
            color=color.black,
            z=-10
        )

        # Фото заставки
        self.logo = Entity(
            parent=camera.ui,
            model='quad',
            texture='',
            color=color.black,
            scale=( 1, 1),
            position=(0, 0, -11),
        )

        # Главный текст (Заменили Button на Text, чтобы не багало)
        # self.title = Text(
        #     text='Tower Defens',
        #     parent=camera.ui,
        #     position=(-0.2, 0.4, -11),
        #     color=color.dark_gray,
        #     scale=2.5
        # )

        # Текст загрузки над полосой
        self.loading_text = Text(
            text=self.loading_steps[0],
            parent=camera.ui,
            position=(0, -0.25, -12),
            origin=(0, 0),
            scale=1,
            color=color.white
        )

        # Полоса прогресса - фон
        self.progress_bg = Entity(
            model='quad',
            parent=camera.ui,
            position=(0, -0.35, -11),
            origin=(0, 0),
            scale=(0.49, 0.03),
            color=color.dark_gray
        )

        # Полоса прогресса - заполнение
        self.progress_bar = Entity(
            model='quad',
            parent=camera.ui,
            position=(-0.25, -0.35, -12),
            scale=(0, 0.03),
            origin_x=-0.5,
            color=color.cyan
        )

        # Индикатор версии
        self.version = Text(
            text='v0.1',
            parent=camera.ui,
            position=(0.275, -0.42, -12),
            scale=1,
            color=color.white
        )

    def finish(self):
        """Полностью и гарантированно уничтожает splash-экран"""
        if self.finished:
            return
        self.finished = True

        # Уничтожаем абсолютно все созданные объекты класса
        destroy(self.overlay)
        # destroy(self.title)
        destroy(self.loading_text)
        destroy(self.progress_bg)
        destroy(self.progress_bar)
        destroy(self.version)
        destroy(self.logo)

        # Вызываем появление главного меню
        if self.on_complete:
            self.on_complete()