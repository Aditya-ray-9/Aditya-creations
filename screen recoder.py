from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.video import Video
from kivy.config import ConfigParser
from PIL import ImageGrab, ImageDraw, Image
import imageio
import numpy as np
import os
import pyautogui
import time

from plyer import notification

class ScreenRecorderApp(App):
    def __init__(self, **kwargs):
        super(ScreenRecorderApp, self).__init__(**kwargs)
        self.recording = False
        self.frames = []
        self.fps = 10
        self.video_dir = "videos"
        os.makedirs(self.video_dir, exist_ok=True)
        self.theme = 'dark'  # Default theme

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Create a top bar for settings and quality management
        top_bar = BoxLayout(size_hint=(1, 0.1))

        # Add settings button to the top bar
        self.settings_button = Button(text="Settings", on_press=self.open_settings, size_hint=(None, None), size=(100, 50))
        top_bar.add_widget(self.settings_button)

        # Add quality management option to the top bar
        quality_label = Label(text="Quality", size_hint=(None, None), size=(100, 50))
        top_bar.add_widget(quality_label)
        self.quality_spinner = Spinner(
            text='720p',
            values=('360p', '480p', '720p', '1080p', '1440p'),
            size_hint=(None, None),
            size=(100, 50)
        )
        top_bar.add_widget(self.quality_spinner)

        self.layout.add_widget(top_bar)

        # Add a welcome message
        welcome_label = Label(text="Welcome to this screen recorder", size_hint=(1, 0.1))
        self.layout.add_widget(welcome_label)

        # Add scrollable file list
        self.file_scroll_view = ScrollView(size_hint=(1, 0.6))
        self.file_list_layout = StackLayout(size_hint_y=None)
        self.file_scroll_view.add_widget(self.file_list_layout)
        self.layout.add_widget(self.file_scroll_view)

        self.update_file_list()

        # Add start/stop button at the bottom
        self.start_stop_button = Button(text="Start Recording", on_press=self.toggle_recording, size_hint=(1, 0.1))
        self.layout.add_widget(self.start_stop_button)

        return self.layout

    def update_file_list(self):
        self.file_list_layout.clear_widgets()
        files = os.listdir(self.video_dir)
        self.file_list_layout.height = max(44 * len(files), 500)
        for file in files:
            file_button = Button(text=file, size_hint=(1, None), height=44)
            file_button.bind(on_release=self.on_file_button_release)
            self.file_list_layout.add_widget(file_button)

    def on_file_button_release(self, button):
        if button.collide_point(*button.last_touch.pos):
            if button.last_touch.button == 'right':
                self.show_context_menu(button)
            else:
                self.show_video(button.text)

    def toggle_recording(self, instance):
        if not self.recording:
            self.start_recording()
            self.show_recording_notification(True)
        else:
            self.stop_recording()
            self.show_recording_notification(False)

    def start_recording(self):
        self.recording = True
        self.start_stop_button.text = "Stop Recording"
        self.frames = []
        Clock.schedule_interval(self.capture_frame, 1 / self.fps)

    def stop_recording(self):
        self.recording = False
        self.start_stop_button.text = "Start Recording"
        Clock.unschedule(self.capture_frame)
        self.save_video()
        self.update_file_list()

    def capture_frame(self, dt):
        if self.recording:
            screen = ImageGrab.grab()
            frame = np.array(screen)
            self.frames.append(frame)

    def save_video(self):
        if self.frames:
            quality = self.quality_spinner.text
            resolutions = {
                '360p': (640, 360),
                '480p': (854, 480),
                '720p': (1280, 720),
                '1080p': (1920, 1080),
                '1440p': (2560, 1440)
            }
            width, height = resolutions[quality]
            resized_frames = [Image.fromarray(frame).resize((width, height), resample=Image.LANCZOS) for frame in self.frames]
            resized_frames = [np.array(frame) for frame in resized_frames]
            timestamp = int(time.time())
            video_filename = os.path.join(self.video_dir, f'screen_recording_{timestamp}.mp4')
            imageio.mimsave(video_filename, resized_frames, fps=self.fps)
            print(f"Video saved as {video_filename}")

    def show_video(self, filename):
        video_path = os.path.join(self.video_dir, filename)
        if os.path.exists(video_path):
            video_popup = Popup(title=filename, size_hint=(0.8, 0.8))
            video = Video(source=video_path, state='play')
            video_popup.content = video
            video_popup.open()

    def show_recording_notification(self, is_recording):
        if is_recording:
            notification_title = "Recording in Progress"
            notification_message = "Tap to stop recording"
        else:
            notification_title = "Recording Stopped"
            notification_message = ""

        notification.notify(
            title=notification_title,
            message=notification_message,
            app_name='ScreenRecorder',
            app_icon=None
        )

    def open_settings(self, instance):
        # Create a settings layout
        settings_layout = BoxLayout(orientation='vertical')

        # Add theme selection
        theme_label = Label(text='Theme', size_hint=(None, None), size=(100, 44))
        dark_button = ToggleButton(text='Dark', group='theme', size_hint=(None, None), size=(100, 44))
        light_button = ToggleButton(text='Light', group='theme', size_hint=(None, None), size=(100, 44))

        if self.theme == 'dark':
            dark_button.state = 'down'
        elif self.theme == 'light':
            light_button.state = 'down'

        dark_button.bind(on_press=lambda instance: self.set_theme('dark'))
        light_button.bind(on_press=lambda instance: self.set_theme('light'))

        settings_layout.add_widget(theme_label)
        settings_layout.add_widget(dark_button)
        settings_layout.add_widget(light_button)

        # Add about section
        about_label = Label(text='About', size_hint=(None, None), size=(100, 44))
        about_text = Label(text='This app is developed using Kivy Python and built for mobile.\nThanks for using my app!', size_hint=(None, None), size=(300, 100))

        settings_layout.add_widget(about_label)
        settings_layout.add_widget(about_text)

        # Create settings popup and open
        settings_popup = Popup(title='Settings', content=settings_layout, size_hint=(0.8, 0.8))
        settings_popup.open()

    def set_theme(self, theme):
        self.theme = theme
        if theme == 'dark':
            App.get_running_app().root_window.clearcolor = (0, 0, 0, 1)
        elif theme == 'light':
            App.get_running_app().root_window.clearcolor = (1, 1, 1, 1)

if __name__ == '__main__':
    ScreenRecorderApp().run()
