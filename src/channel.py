from googleapiclient.discovery import build
import json
import os
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pass

c = Channel('AIzaSyBpls0q5DFRSc6Nr6ZIIEvhjOYYi7yVH7s"')