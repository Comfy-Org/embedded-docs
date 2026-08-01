# Google Gemini Omni (Video)

Google'ın Gemini Omni Flash modelini kullanarak bir metin isteminden sesli video oluşturun. Sonucu yönlendirmek veya düzenlemek için isteğe bağlı olarak referans görseller ve/veya videolar sağlayın. İstenen süreyi (3-10s) ve en boy oranını (16:9 veya 9:16) doğrudan istemde belirtin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan Gemini video modeli. | COMBO | Evet | "Omni Flash" |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |
| `prompt` | Oluşturulacak videoyu tanımlayan metin istemi. Baştaki ve sondaki boşluklar temizlendikten sonra en az bir boşluk olmayan karakter içermelidir. | STRING | Evet | Boşluklar temizlendikten sonra en az 1 karakter |
| `images` | Video oluşturmayı yönlendirmek için isteğe bağlı referans görseller. Toplam en fazla 14 görsel. | IMAGE | Hayır | Birden fazla görsele izin verilir (en fazla 14) |
| `videos` | Video oluşturmayı yönlendirmek veya düzenlemek için isteğe bağlı referans videolar. En fazla 3 video, her biri en fazla 10 saniye. | VIDEO | Hayır | Birden fazla videoya izin verilir (en fazla 3, her biri en fazla 10s) |
| `temperature` | Oluşturmadaki rastgeleliği kontrol eder (varsayılan: 1.0). | FLOAT | Hayır | 0.0 ile 2.0 arası |
| `top_p` | Nucleus örnekleme parametresi (varsayılan: 0.95). | FLOAT | Hayır | 0.0 ile 1.0 arası |

Notlar:
- Bir görsel girdisi birden fazla kare içeriyorsa, her kare 14 görsel sınırına sayılır.
- `images` veya `videos` sağlandığında, birleşik kodlanmış medya boyutu yaklaşık 90 MB'ın altında kalmalıdır; aksi takdirde düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Gemini modelinden ses içeren oluşturulan video. | VIDEO |
| `STRING` | Modelden gelen, muhakeme veya açıklamalar gibi metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/tr.md)

---
**Source fingerprint (SHA-256):** `1b7ca51d07cfb6a166cfed2a7e7174fd62f3290abcc1bdfdce94369dda242d3f`
