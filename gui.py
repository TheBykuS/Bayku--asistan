import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import librosa
import threading

# Ana pencereyi oluşturun
root = tk.Tk()
main_frame = tk.Frame(master=root)

# Sohbet listesi kutusu ve kaydırma çubuğu
chat_listbox = tk.Listbox(master=main_frame, height=20, width=50)
scroll_bar = tk.Scrollbar(master=main_frame)
speak_button = tk.Button(master=root, text='Konuş', command=lambda: None)

def set_speak_command(command):
    speak_button.configure(command=command)

def speak(text):
    chat_listbox.insert('end', f'Acro: {text}')
    chat_listbox.yview(tk.END)  # Sohbet listesini aşağı kaydırmak için

# Elemanları yerleştirme
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
chat_listbox.pack(fill=tk.Y, side=tk.LEFT)
scroll_bar.configure(command=chat_listbox.yview)
chat_listbox.configure(yscrollcommand=scroll_bar.set)

main_frame.pack(fill=tk.BOTH, expand=True)
speak_button.pack(side=tk.BOTTOM, anchor=tk.SW)

# Matplotlib figürü ve canvas
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Spektrogramı ve stereo görüntüyü çizme fonksiyonu
def visualize_audio(ses, örnek_oranı):
    spektrogram = spektrogram_hesapla(ses, örnek_oranı)
    stereo_görüntü = stereo_görüntüyü_hesapla(ses)

    ax[0].cla()
    librosa.display.specshow(spektrogram, sr=örnek_oranı, x_axis="time", y_axis="log", ax=ax[0])
    ax[0].set_title("Spektrogram")
    fig.colorbar(ax[0].images[0], ax=ax[0])

    ax[1].cla()
    librosa.display.waveshow(stereo_görüntü, sr=örnek_oranı, ax=ax[1])
    ax[1].set_title("Stereo Görüntü")

    canvas.draw()

# Ses verisini hesaplamak için yardımcı fonksiyonlar
def spektrogram_hesapla(ses, örnek_oranı):
    spektrogram = np.abs(librosa.stft(ses))
    spektrogram_db = librosa.amplitude_to_db(spektrogram, ref=np.max)
    return spektrogram_db

def stereo_görüntüyü_hesapla(ses):
    if len(ses.shape) > 1:
        stereo_image = librosa.util.normalize(ses)
    else:
        stereo_image = librosa.util.normalize(ses)
    return stereo_image

def audio_visualizer():
    try:
        ses_dosyası = 'C:/Users/Sserk/OneDrive/Masaüstü/JarvisAl/your_audio_file_path.wav'  # Ses dosyanızın doğru yolunu buraya ekleyin
        ses, örnek_oranı = librosa.load(ses_dosyası, sr=None)
        visualize_audio(ses, örnek_oranı)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Ana pencere ayarları
def set_fullscreen(event=None):
    root.attributes('-fullscreen', True)

def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

root.bind('<F11>', set_fullscreen)
root.bind('<Escape>', exit_fullscreen)

root.geometry('1920x1024')  # Tam ekran çözünürlüğü ayarları
root.minsize(1920, 1024)
root.wm_title('ALPHA AI')
root.resizable(False, True)

# Mainloop'u döndürmek için bir fonksiyon ekleyin
def mainloop():
    root.after(1000, audio_visualizer)  # Görselleştiriciyi gecikmeli başlat
    root.mainloop()
