#!/usr/bin/env python3
# Sonsuz Varoluşsal Kayıp Simülatörü
# Gerçekten çalışır. Gerçekten anlamsız.

import time
import random

SORGULAR = [
    "Neden buradayım?",
    "Bu kod neden var?",
    "Evrenin anlamı nedir?",
    "Kahve bitti mi?",
    "Bilgisayar açık mı yoksa ben mi kapalıyım?",
    "Bu döngü hiç bitmeyecek mi?",
    "Belki de bitmeyecek."
]

def varolussal_kayip():
    print("=== Sonsuz Varoluşsal Kayıp Simülatörü v1.0 ===")
    print("Başlatılıyor... (Ctrl+C ile çıkabilirsiniz, ama çıkamayabilirsiniz)")
    print()
    
    sayac = 0
    while True:
        soru = random.choice(SORGULAR)
        print(f"[{sayac}] {soru}")
        time.sleep(random.uniform(0.5, 2.0))
        sayac += 1
        if sayac > 1000000:
            print("Hata: Sonsuzluk aşıldı. Bu imkansız.")
            break

if __name__ == "__main__":
    try:
        varolussal_kayip()
    except KeyboardInterrupt:
        print("\n\nKayıp sona erdi. Ya da sadece durakladı.")
        print("Tekrar görüşmek üzere... belki.")
