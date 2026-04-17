# from ursina import (
#     Entity, Vec3, color, camera, Text, Button,
#     window, load_texture, lerp, destroy, invoke, Sprite
# )
# from ursina.shaders import basic_lighting_shader
# import time as time_module
# from ursina import curve


# class SplashScreen:
#     """
#     Экран загрузки с анимацией и индикатором прогресса.
#     """

#     def __init__(self, on_complete=None):
#         self.on_complete = on_complete
#         self.progress = 0
#         self.loading_steps = [
#             "Загрузка...",
#             "Создание объектов...",
#             "Настройка сцены...",
#             "Почти готово...",
#             "Готово!"
#         ]
#         self.current_step = 0
#         self.start_time = time_module.time()
#         self.finished = False

#         # Создаём UI элементы
#         self._create_ui()

#     def _create_ui(self):
#         """Создаёт UI элементы splash-экрана"""
#         # Отключаем основное окно на время загрузки
#         self.overlay = Entity(
#             model='quad',
#             scale=(100, 100),
#             position=(0, 0, -10),
#             color=color.black
#         )

#         # Фото заставки
#         self.logo = Sprite(
#             texture='',
#             parent = camera.ui,
#             scale = (window.aspect_ratio,0.05),
#             position = (0, 0, -11),
#         )


#         self.title = Button(
#             text='',
#             position=(0, 0.4, -11),
#             color=color.clear,
#             text_color=color.cyan,
#             text_size=2.5,
#             borderless=True
#         )
#         self.title.disabled = True  # Не кликабельно

#         # Текст загрузки
#         self.loading_text = Button(
#             text=self.loading_steps[0],
#             position=(0, -0.3, -11),
#             scale=(0.5, 0.1),
#             color=color.clear,
#             text_color=color.white,
#             text_scale=1,
#             borderless=True
#         )
#         self.loading_text.disabled = True

#         # Полоса прогресса - фон
#         self.progress_bg = Entity(
#             model='quad',
#             parent=camera.ui,
#             position=(0, -0.35, -11),
#             scale=(0.5, 0.03),
#             color=color.dark_gray
#         )

#         # Полоса прогресса - заполнение
#         self.progress_bar = Entity(
#             model='quad',
#             parent=camera.ui,
#             position=(-0.25, -0.35, -12),
#             scale=(0, 0.03),
#             origin_x=-0.5,
#             color=color.cyan
#         )

#         # Индикатор версии
#         self.version = Button(
#             text='v0.1',
#             position=(0.85, -0.48, -11),
#             scale=(0.15, 0.05),
#             color=color.clear,
#             text_color=color.white,
#             text_scale=0.5,
#             borderless=True
#         )
#         self.version.disabled = True

#     def update(self):
#         if self.finished:
#             return

#         # 1. Держим фон растянутым
#         if hasattr(self, 'logo') and self.logo:
#             self.logo.scale_x = window.aspect_ratio

#         # 2. Считаем прогресс (от 0 до 1 за 5 секунд)
#         duration = 5.0
#         current_time = time_module.time() - self.start_time
#         progress_ratio = current_time / duration

#         # 3. Если время вышло — закрываем
#         if progress_ratio >= 1.0:
#             self.progress_bar.scale_x = 0.5 # Максимальная ширина
#             self.finish()
#             return

#         # 4. Двигаем полоску (0.5 — это полная ширина серой подложки)
#         self.progress_bar.scale_x = progress_ratio * 0.5

#         # 5. Меняем текст
#         step_index = int(progress_ratio * len(self.loading_steps))
#         step_index = min(step_index, len(self.loading_steps) - 1)

#         if step_index != self.current_step:
#             self.current_step = step_index
#             self.loading_text.text = self.loading_steps[step_index]
#     def finish(self):
#         """Завершает splash-экран"""
#         if self.finished:
#             return
#         self.finished = True

#         # Просто удаляем все элементы сразу
#         destroy(self.overlay)
#         destroy(self.title)
#         # destroy(self.subtitle)
#         destroy(self.loading_text)
#         destroy(self.progress_bg)
#         destroy(self.progress_bar)
#         destroy(self.version)
#         destroy(self.logo)

#         if self.on_complete:
#             self.on_complete()

#     def close(self):
#         """Принудительно закрывает splash-экран"""
#         self.finish()
