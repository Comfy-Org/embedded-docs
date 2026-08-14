# Google Gemini Omni (Video)

Google'ın Gemini Omni Flash modelini kullanarak bir metin prompt'undan sesli video oluşturun. Sonucu yönlendirmek veya düzenlemek için isteğe bağlı olarak referans görseller ve/veya videolar sağlayın. İstenen uzunluğu (3-10 sn) ve en-boy oranını (16:9 veya 9:16) doğrudan prompt içinde belirtin.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan Gemini video modeli. | COMBO | Evet | "Omni Flash" |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Omni Flash Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak videoyu tanımlayın. Uzunluğu ve en-boy oranını doğrudan prompt içinde belirtin, örn. "16:9'da 6 saniyelik bir klip". Uzunluk 3-10 saniye olabilir; en-boy oranı 16:9 (yatay) veya 9:16 (dikey) olmalıdır. Çıktı 720p, 24 FPS ve seslidir. | STRING | Evet | Boşluklar temizlendikten sonra en az 1 karakter |
| `images` | Genişletilebilir yuva: Videoyu yönlendirmek veya canlandırmak için bir veya daha fazla referans görseli (`image_1`...`image_14`) bağlayın. Toplamda en fazla 14 görsel. | IMAGE | Hayır | 0-14 görsel |
| `videos` | Genişletilebilir yuva: Yönlendirmek veya düzenlemek için bir veya daha fazla referans videosu (`video_1`...`video_3`) bağlayın. En fazla 3 video; her biri en fazla 10 saniye uzunluğunda. | VIDEO | Hayır | 0-3 video, her biri maksimum 10 saniye |
| `temperature` | Rastgeleliği kontrol eder. Düşük değer daha odaklı/deterministik, yüksek değer daha çeşitlidir (varsayılan: 1.0). | FLOAT | Hayır | 0.0 ile 2.0 arası |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapar (varsayılan: 0.95). | FLOAT | Hayır | 0.0 ile 1.0 arası |

Notlar:
- Bir görsel girdisi birden fazla kare içeriyorsa, her kare 14 görsel sınırına dahil sayılır.
- Referans görsel veya video sağlandığında, toplam kodlanmış medya boyutu yaklaşık 90 MB'ın altında kalmalıdır; aksi takdirde düğüm bir hata verir.
- Hiçbir referans görsel veya video sağlanmadığında, düğüm videoyu yalnızca metin prompt'undan oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Gemini modeli tarafından oluşturulan, ses içeren video. | VIDEO |
| `STRING` | Modelden gelen her türlü metin yanıtı (örneğin akıl yürütme veya açıklamalar). | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/tr.md)

---
**Source fingerprint (SHA-256):** `1b7ca51d07cfb6a166cfed2a7e7174fd62f3290abcc1bdfdce94369dda242d3f`
