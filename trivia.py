import random
import json

# Soruları JSON dosyasından oku
def load_questions():
    with open('sorular.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Oyuncu isimlerini al
def get_player_names():
    player1 = input("Oyuncu 1'in adı nedir? ")
    player2 = input("Oyuncu 2'nin adı nedir? ")
    return player1, player2

# Soruları sor ve cevapları al
def ask_question(player, question):
    print(f"{player}, sorunuz: {question['soru']}")
    answer = input("Cevabınız nedir? ").strip().lower()
    return answer

# Oyun ana fonksiyonu
def play_trivia():
    print("Trivia oyununa hoş geldiniz!")
    player1, player2 = get_player_names()
    players = {player1: 0, player2: 0}

    questions = load_questions()
    categories = list(questions.keys())
    random.shuffle(categories)

    for category in categories:
        print(f"Kategori: {category.capitalize()}")

        question1 = random.choice(questions[category])
        answer1 = ask_question(player1, question1)
        
        question2 = random.choice(questions[category])
        answer2 = ask_question(player2, question2)

        if answer1 == question1['cevap'].strip().lower() and answer2 == question2['cevap'].strip().lower():
            print("Her iki oyuncu da doğru cevap verdi!")
            players[player1] += 1
            players[player2] += 1
        elif answer1 == question1['cevap'].strip().lower():
            print(f"{player1}, doğru cevap verdi!")
            players[player1] += 1
        elif answer2 == question2['cevap'].strip().lower():
            print(f"{player2}, doğru cevap verdi!")
            players[player2] += 1
        else:
            print("Hiçbir oyuncu doğru cevap vermedi.")

    # Sonuçları göster
    print("Oyun bitti! Sonuçlar:")
    for player, score in players.items():
        print(f"{player}: {score} puan")

    # Kaybedeni belirle ve ceza ver
    if players[player1] > players[player2]:
        loser = player2
    elif players[player2] > players[player1]:
        loser = player1
    else:
        print("Oyun berabere bitti! Ceza yok.")
        return

    print(f"{loser}, kaybettiniz ve cezanız...")

    # Küçük cezalar örneği
    penalties = [
        "1 dakika boyunca tek ayak üstünde durmak",
        "Bir bardak su içmek",
        "Küçük bir dans gösterisi yapmak"
    ]
    print(random.choice(penalties))

# Ana fonksiyon
if __name__ == "__main__":
    play_trivia()
