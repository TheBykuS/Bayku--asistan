# quiz.py

def get_daily_quiz():
    quiz = [
        {
            "soru": "Dünyanın en yüksek dağı hangisidir?",
            "secenekler": ["a) K2", "b) Everest", "c) Kilimanjaro", "d) Aconcagua"],
            "cevap": "b"
        },
        {
            "soru": "Hangi gezegen Güneş Sistemi'ndeki en büyük gezegendir?",
            "secenekler": ["a) Mars", "b) Jüpiter", "c) Uranüs", "d) Venüs"],
            "cevap": "b"
        },
        {
            "soru": "Birleşmiş Milletler ne zaman kuruldu?",
            "secenekler": ["a) 1945", "b) 1950", "c) 1960", "d) 1975"],
            "cevap": "a"
        },
        {
            "soru": "Hangi elementin kimyasal sembolü 'O'dur?",
            "secenekler": ["a) Altın", "b) Oksijen", "c) Gümüş", "d) Karbon"],
            "cevap": "b"
        },
        {
            "soru": "Dünyanın en büyük okyanusu hangisidir?",
            "secenekler": ["a) Atlantik Okyanusu", "b) Hint Okyanusu", "c) Pasifik Okyanusu", "d) Arktik Okyanusu"],
            "cevap": "c"
        },
        # Diğer sorular benzer şekilde eklendi.
    ]
    return quiz

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.lower()
