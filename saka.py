jokes = [
    "İki atom bir barda karşılaşır. Birinci atom: 'Elektronumu kaybettim!' İkinci atom: 'Emin misin?' Birinci atom: 'Evet, pozitifim!'",
    "Bir adam doktora gitmiş. Doktor: 'Size kötü bir haberim var, 24 saat ömrünüz kalmış.' Adam: 'Peki doktor, daha da kötüsü olabilir mi?' Doktor: 'Evet, dünden beri sizi arıyorum!'",
    "Kedinin biri müzik yapmaya karar vermiş. Arkadaşı sormuş: 'Ne çalıyorsun?' Kedi: 'Miyav-piyano!'",
    "İki balıkçı barajda balık tutuyorlarmış. Birisi diğerine sormuş: 'Burada neden hiç balık tutamıyoruz?' Diğeri: 'Çünkü burası sadece çizgi filmlerde balık tutulan baraj!'",
    "Bir fare birine aşık olmuş. Arkadaşına demiş ki: 'Ona söyleyemedim, kalbimi peynire dönüştürdü!'",
    "Adamın biri hayatta hep mutluydu. Arkadaşı sormuş: 'Nasıl hep mutlu olabiliyorsun?' Adam cevap vermiş: 'Çünkü ben polyannakistim!'",
    "Bir matematikçi aşk hayatında sorun yaşıyormuş. Arkadaşı sormuş: 'Ne oldu?' Matematikçi: 'Sürekli ayrışıyoruz!'",
    "Mühendis bir tavşan yapmaya karar vermiş. Tavşan: 'Benim adım artık Rob-bunny!'",
    "Doktor hastasına: 'Günde iki litre su içmen gerekiyor.' Hasta: 'Kralım, yüzme bilmiyorum!'",
    "İki bilgisayar konuşuyormuş. Biri diğerine demiş ki: 'Hadi biraz RAM'len!'",
    "Bir hayalet bakkala gitmiş. Bakkal sormuş: 'Ne alırsın?' Hayalet: 'Bir paket beyaz un!'",
    "Uzaylılar dünyaya inmiş. İnsanlar sormuş: 'Bize neden geldiniz?' Uzaylılar: 'Çünkü biz kuantum meraklılarıyız!'",
    "Süper kahraman Batman'in arabası varmış. Ne marka? Tabii ki Batmobil!",
    "Bir kaplumbağa tavşanı geçmeye çalışmış. Tavşan: 'Hey, yarışımız bitti bile!' Kaplumbağa: 'Yavaş ama steadyy kazanır!'",
    "İki muz kavanozda kapışıyormuş. Biri diğerine demiş ki: 'Senin kabuğunu soyarım!'",
    "Bir matematikçi restorana gitmiş. Garson sormuş: 'Masada kaç kişi var?' Matematikçi: 'Sonsuz küçük sayı kadar!'",
    "Bir karınca denize girmek istemiş. Arkadaşı sormuş: 'Yüzecek misin?' Karınca: 'Hayır, gemiyle gidiyorum!'",
    "Astronot uzayda yürüyormuş. Birdenbire arkadaşına dönüp: 'Ay'dan indim, yıldız oldum!'",
    "Bir dalgıç denizde kaybolmuş. Arkadaşı sormuş: 'Nasıl bulacağız?' Diğeri: 'Bizi takip et, dalgaların üstünde gideceğiz!'",
    "Bilgisayarını çok seven bir adam varmış. Sürekli format atıyormuş, çünkü temizlik imandandır!",
    "Bir beyin ameliyatında doktor: 'Hastanın beyninde garip bir sorun var.' Hemşire: 'O zaman düşünmesi mi yasak?'",
    "İki gözlükçü kavga etmiş. Biri diğerine: 'Sana bir lens daha takarım, gözün dört açılır!'",
    "Dinozorlar neden yok oldu? Çünkü biri diğerine 'Sen demode oldun!' demiş.",
    "Bir pizza teslimatçısı evlere pizza taşıyormuş. Bir gün bir sipariş unutmuş. Patronu sormuş: 'Neden getirmedin?' Teslimatçı: 'Pardon, yolumda kaybolmuş!'",
    "İki ceviz kavanozda kavga ediyormuş. Biri diğerine demiş: 'Sana çatlarım!'",
    "Bir filozof köpeğe sormuş: 'Gerçekten sen mi havlıyorsun?' Köpek: 'Ben zaten varlık diyarında yokum!'",
    "Bilim kurgu yazarı bir sinek yazmış. Arkadaşı sormuş: 'Neden sinek?' Yazarı: 'Çünkü sinek de bilimsel!'",
    "Bir koala ağaca tırmanmış. Arkadaşı sormuş: 'Neden tırmanıyorsun?' Koala: 'Çünkü evde kaldım!'",
    "Kayıp kediyi bulan biri sormuş: 'Kedinizin adı ne?' Diğeri: 'Biz ona 'Kayıp' diyoruz, çünkü hep kaybolur!'",
    "İki bulut birbirine aşkını itiraf etmiş. Birinci bulut: 'Seni gökyüzüne çıkaracağım!' İkincisi: 'Ben de sana yağmur olup düşeceğim!'",
    "Bir kaplumbağa balona binmiş. Baloncu sormuş: 'Nereye gidiyoruz?' Kaplumbağa: 'Gökyüzünün sınırlarına!'",
    "Bir robot aşık olmuş. Diğer robot sormuş: 'Kalbin var mı?' Aşık robot: 'Evet, çünkü sevgi yazılımını yükledim!'",
    "Bir kuş kargoya gidip paket vermiş. Çalışan sormuş: 'Ne gönderiyorsun?' Kuş: 'Kanat çırpıntısı!'",
    "Bir elma armuta demiş ki: 'Sen neden hep yeşilsin?' Armut: 'Çünkü sararma dönemindeyim!'",
    "Bir çocuk babasına sormuş: 'Baba, kediler niye düşmez?' Baba: 'Çünkü onlar hep dört ayak üstüne düşer!'",
    "Bir aslan kafeste uyuyormuş. Küçük aslan sormuş: 'Neden uyuyorsun?' Büyük aslan: 'Çünkü rüyalarımda avlanırım!'",
    "İki yıldız gökyüzünde kavga ediyormuş. Biri diğerine: 'Senin ışığın benden az!'",
    "Bir köpek balonu patlatmış. Diğeri sormuş: 'Neden patlattın?' Köpek: 'Çünkü balonla oynamak istemedim!'",
    "Bir ağaç meyve vermemiş. Bahçıvan sormuş: 'Neden meyve vermiyorsun?' Ağaç: 'Çünkü bu yıl protesto ediyorum!'",
    "Bir çita kaplumbağayı geçememiş. Kaplumbağa demiş ki: 'Yavaş ama steadyy kazanır!'",
    "Bir baykuş gece vakti tarlada uçuyormuş. Fare sormuş: 'Nereye gidiyorsun?' Baykuş: 'Gece avına!'",
    "Bir ördek gölde yüzüyormuş. Diğeri sormuş: 'Neden yüzüyorsun?' Ördek: 'Çünkü su benim doğal alanım!'",
    "Bir fil ormanda ağacı yıkmış. Arkadaşı sormuş: 'Neden yıktın?' Fil: 'Çünkü o benim oyun alanım!'",
    "Bir tavşan güneş gözlüğü takmış. Diğeri sormuş: 'Neden gözlük taktın?' Tavşan: 'Çünkü moda!'",
    "Bir panda bambu ağacını kesmiş. Diğeri sormuş: 'Neden kestin?' Panda: 'Çünkü o benim yemeğim!'",
    "Bir balık suda hızlı yüzüyormuş. Diğeri sormuş: 'Neden hızlı yüzüyorsun?' Balık: 'Çünkü yüzme yarışındayım!'",
    "Bir yılan ağaca tırmanmış. Diğeri sormuş: 'Neden tırmanıyorsun?' Yılan: 'Çünkü manzara çok güzel!'",
    "Bir zürafa kafasını eğmiş. Diğeri sormuş: 'Neden kafanı eğdin?' Zürafa: 'Çünkü aşağıdaki çiçekleri koklamak istiyorum!'",
    "Bir dinozor fosil olmuş. Diğeri sormuş: 'Neden fosil oldun?' Dinozor: 'Çünkü tarih yazıyorum!'"
]

def get_random_joke():
    import random
    return random.choice(jokes)
