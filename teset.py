import speech_recognition as sr

def test_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mikrofon testi. Lütfen konuşun...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("Ses tanınıyor...")
        query = r.recognize_google(audio, language='tr-TR')
        print(f"Söyledikleriniz: {query}")
    except Exception as e:
        print(f"Tanıma Hatası: {e}")

if __name__ == "__main__":
    test_microphone()
