import json
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='tr')

def translate_jokes(input_file, output_file):
    translated_jokes = []
    
    # JSON dosyasını oku
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            joke_data = json.loads(line)
            english_joke = joke_data['joke']
            
            # Şakayı Türkçeye çevir
            translated_joke = translator.translate(english_joke)
            translated_jokes.append({"joke": translated_joke})
    
    # Çevrilen şakaları yeni bir JSON dosyasına yaz
    with open(output_file, 'w', encoding='utf-8') as f:
        for joke_data in translated_jokes:
            json.dump(joke_data, f, ensure_ascii=False)
            f.write('\n')

# Çeviri fonksiyonunu çağır
translate_jokes('şaka.json', 'şaka_tr.json')
