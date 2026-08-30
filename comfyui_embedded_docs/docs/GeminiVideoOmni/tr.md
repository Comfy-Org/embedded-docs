# Google Gemini Omni (Video)

Google'ın Gemini Omni Flash modelini kullanarak metin isteminden sesli video oluşturun. İsteğe bağlı olarak, sonucu yönlendirmek veya düzenlemek için referans görseller ve/veya videolar sağlayın. İstenen süreyi (3-10sn) ve en-boy oranını (16:9 veya 9:16) doğrudan istemde belirtin.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan Gemini video modeli. | DYNAMIC_COMBO | Evet | "Omni Flash" |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ila 2147483647 |

### Omni Flash Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak videoyu tanımlayın. Uzunluğu ve en-boy oranını doğrudan istemde belirtin, örn. "16:9'da 6 saniyelik bir klip". Uzunluk 3-10 saniye olabilir; en-boy oranı 16:9 (yatay) veya 9:16 (dikey) olmalıdır. Çıktı 720p, 24 FPS ve seslidir. | STRING | Evet | Boşluklar temizlendikten sonra minimum 1 karakter |
| `temperature` | Rastgeleliği kontrol eder. Düşük değerler daha odaklı/deterministik, yüksek değerler daha çeşitlidir (varsayılan: 1.0). | FLOAT | Hayır | 0.0 ila 2.0 |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapın (varsayılan: 0.95). | FLOAT | Hayır | 0.0 ila 1.0 |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Büyütülebilir yuva: videoyu yönlendirmek veya canlandırmak için bir veya daha fazla referans görselini (`image_1`...`image_14`) bağlayın. Toplamda en fazla 14 görsel. | IMAGE | Hayır | 0 ila 14 görsel |
| `videos` | Büyütülebilir yuva: yönlendirmek veya düzenlemek için bir veya daha fazla referans videosunu (`video_1`...`video_3`) bağlayın. Her biri en fazla 10 saniye uzunluğunda olmak üzere en fazla 3 video. | VIDEO | Hayır | 0 ila 3 video, her biri maksimum 10 saniye |

Notlar:
- Bir görsel girdisi birden çok kare içeriyorsa, her kare 14 görsel sınırına sayılır.
- Referans görseller veya videolar sağlandığında, toplam kodlanmış medya boyutu yaklaşık 90 MB'ın altında kalmalıdır; aksi takdirde düğüm bir hata verir.
- Hiçbir referans görseli veya videosu sağlanmadığında, düğüm videoyu yalnızca metin isteminden oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Gemini modelinden sesli olarak oluşturulan video. | VIDEO |
| `STRING` | Modelden gelen akıl yürütme veya açıklamalar gibi herhangi bir metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/tr.md)

---
**Source fingerprint (SHA-256):** `648844868affb68298d2eac8ac20095bfe378d32e721396781de330ef6a6d69f`
