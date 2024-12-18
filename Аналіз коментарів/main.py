import os
from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Зміна змінних середовища для API ключа YouTube
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
API_KEY = 'AIzaSyB36Qlze8fVflX8Ni26rCkAGAhkDJW-oIM'  # Замініть 'YOUR_API_KEY' на ваш API ключ YouTube

def get_and_clean_comments(video_id):
    # Створюємо об'єкт YouTube API
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Запит на отримання коментарів до відео
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        maxResults=100  # Встановлюємо максимальну кількість коментарів
    )
    
    response = request.execute()

    # Збір і очищення коментарів
    cleaned_comments = []
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        cleaned_comment = re.sub(r'[^\w\s]', '', comment.lower())
        cleaned_comments.extend(cleaned_comment.split())
    
    return cleaned_comments

def analyze_comments(comments):
    # Використовуємо Counter для підрахунку частот слів
    return Counter(comments)

def plot_word_frequency(word_count):
    # Отримання 30 найбільш поширених слів та їх частот
    top_words = dict(word_count.most_common(30))
    
    # Розділення даних на слова і відповідні частоти
    words = list(top_words.keys())
    frequencies = list(top_words.values())

    # Обчислення процентного співвідношення
    total_words = sum(frequencies)
    percentages = [freq / total_words * 100 for freq in frequencies]

    # Побудова стовпчастого діаграми
    plt.figure(figsize=(14, 6))
    bars = plt.bar(words, frequencies, color='skyblue')
    
    # Додавання відсотків над стовпчиками
    for bar, percentage in zip(bars, percentages):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{percentage:.2f}%', ha='center', va='bottom', fontsize=8)
    
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Word Frequency in Comments')
    plt.xticks(rotation=45, ha='right')  # Ротація підписів осі X
    plt.tight_layout()
    plt.show()

# Основний скрипт
if __name__ == "__main__":
    video_id = '0BjlBnfHcHM'  # Замініть 'INSERT_VIDEO_ID' на ID відео на YouTube

    # Отримання та очищення коментарів
    cleaned_comments = get_and_clean_comments(video_id)
    
    # Аналіз коментарів
    word_count = analyze_comments(cleaned_comments)
    
    # Побудова графіка
    plot_word_frequency(word_count)
