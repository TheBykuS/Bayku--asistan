import os
import random  # random modülünü içeri aktarıyoruz
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import pywhatkit
import webbrowser
import time
import threading
import speech_recognition as sr
import json
import requests

import tanisma
import saka
import weather
import news
import quiz

WEATHER_API_KEY = "fe3de17c803bf73d78606e6e2a665ca4"

responses = {}

if os.path.exists("responses.json"):
    with open("responses.json", "r", encoding="utf-8") as f:
        responses = json.load(f)

def save_responses():
    with open("responses.json", "w", encoding="utf-8") as f:
        json.dump(responses, f, ensure_ascii=False, indent=4)

def speak(audio, speed=1.0):
    print(f"Baykuş: {audio}")
    try:
        tts = gTTS(text=audio, lang='tr')
        tts.save("output.mp3")

        sound = AudioSegment.from_mp3("output.mp3")
        sound = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
        sound = sound.set_frame_rate(sound.frame_rate)

        play_thread = threading.Thread(target=play, args=(sound,))
        play_thread.start()
        play_thread.join()
        os.remove("output.mp3")
    except Exception as e:
        print(f"Konuşma Hatası: {e}")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='tr-TR')
        print(f"Kullanıcı dedi ki: {query}\n")
        return query
    except Exception as e:
        print(f"Tanıma Hatası: {e}")
        speak("Sizi anlayamadım, lütfen cevabınızı tekrar edin.")
        return ""

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
    response = requests.get(url)
    print(f"API Yanıt Kodu: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"API Yanıt Verisi: {data}")
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        weather_info = f"{city} için hava durumu: {temp} derece ve {description}."
        return weather_info
    else:
        print(f"API Hatası: {response.text}")
        return "Hava durumu bilgisi alınamadı."

def tell_joke():
    joke = saka.get_random_joke()
    speak(joke)

def ask_quiz():
    quiz_data = quiz.get_daily_quiz()
    for q in quiz_data:
        speak(q["soru"])
        for option in q["secenekler"]:
            speak(option)
        speak("Cevabınızı 'cevap a', 'cevap b' şeklinde belirtin.")
        user_answer = take_command().strip().lower()
        correct_answer = f"cevap {q['cevap']}".strip().lower()
        if user_answer == correct_answer:
            speak("Woow! Başarılı, çok doğru!")
        else:
            speak(f"Yanlış cevap, beyinsiz. Doğru cevap {q['cevap']}.")

def load_questions():
    with open("sorular.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_player_names():
    speak("Oyuncu 1'in adı nedir?")
    player1 = take_command()
    speak("Oyuncu 2'nin adı nedir?")
    player2 = take_command()
    return player1, player2

def ask_question(player, question):
    speak(f"{player}, sorunuz: {question['soru']}")
    answer = take_command().strip().lower()
    return answer

def play_trivia():
    speak("Trivia oyununa hoş geldiniz!")
    player1, player2 = get_player_names()
    players = {player1: 0, player2: 0}

    questions = load_questions()
    categories = list(questions.keys())
    random.shuffle(categories)

    for category in categories:
        speak(f"Kategori: {category.capitalize()}")

        question1 = random.choice(questions[category])
        answer1 = ask_question(player1, question1)
        
        question2 = random.choice(questions[category])
        answer2 = ask_question(player2, question2)

        if answer1 == question1['cevap'].strip().lower() and answer2 == question2['cevap'].strip().lower():
            speak("Her iki oyuncu da doğru cevap verdi!")
            players[player1] += 1
            players[player2] += 1
        elif answer1 == question1['cevap'].strip().lower():
            speak(f"{player1}, doğru cevap verdi!")
            players[player1] += 1
        elif answer2 == question2['cevap'].strip().lower():
            speak(f"{player2}, doğru cevap verdi!")
            players[player2] += 1
        else:
            speak("Hiçbir oyuncu doğru cevap vermedi.")

    speak("Oyun bitti! Sonuçlar:")
    for player, score in players.items():
        speak(f"{player}: {score} puan")

    if players[player1] > players[player2]:
        loser = player2
    elif players[player2] > players[player1]:
        loser = player1
    else:
        speak("Oyun berabere bitti! Ceza yok.")
        return

    speak(f"{loser}, kaybettiniz ve cezanız...")

    penalties = [
        "1 dakika boyunca tek ayak üstünde durmak",
        "Bir bardak su içmek",
        "Küçük bir dans gösterisi yapmak"
    ]
    speak(random.choice(penalties))

def run_assistant():
    try:
        tanisma.meet_user(take_command, speak)

        while True:
            command = take_command().lower()

            if command in responses:
                speak(responses[command])
            elif 'isimi değiştir' in command or 'isim değiştir' in command:
                tanisma.change_name(take_command, speak)
            elif 'youtube aç' in command:
                speak('YouTube açılıyor')
                webbrowser.open('https://www.youtube.com')
            elif 'google aç' in command:
                speak('Google açılıyor')
                webbrowser.open('https://www.google.com')
            elif 'şarkı çal' in command:
                song = command.replace('şarkı çal', '')
                speak(f'{song} çalınıyor')
                pywhatkit.playonyt(song)
            elif 'şaka yap' in command:
                tell_joke()
            elif 'hava durumu' in command:
                weather_info = get_weather('İstanbul', WEATHER_API_KEY)
                speak(weather_info)
            elif 'haberler' in command:
                news_info = news.get_news()
                if news_info:
                    speak(news_info)
                else:
                    speak('Haber bilgisi alınamadı.')
            elif 'quiz' in command:
                speak('Günün quizine hoş geldiniz!')
                ask_quiz()
            elif 'trivia oyna' in command:
                play_trivia()
            elif 'kapat' in command or 'çık' in command:
                speak('Görüşmek üzere!')
                break
            else:
                speak("Bunu bilmiyorum, bana öğretir misiniz? Ne söylemem gerekiyor?")
                response = take_command()
                if response:
                    responses[command] = response
                    save_responses()
                    speak("Teşekkür ederim, öğrendim.")
                else:
                    speak("Anlayamadım, lütfen tekrar deneyin.")

            time.sleep(2)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == '__main__':
    try:
        run_assistant()
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
