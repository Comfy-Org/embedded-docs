# Google Gemini Omni (Video)

Google'ın Gemini Omni Flash modelini kullanarak bir metin isteminden sesli video oluşturun. Sonucu yönlendirmek veya düzenlemek için isteğe bağlı olarak referans görseller ve/veya videolar sağlayın. İstenen süreyi (3-10 sn) ve en boy oranını (16:9 veya 9:16) doğrudan istemde belirtin.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan Gemini video modeli. | MODEL | Evet | "Omni Flash" |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |
| `prompt` | Oluşturulacak videoyu tanımlayan metin istemi. Baştaki ve sondaki boşluklar temizlendikten sonra en az bir boşluk olmayan karakter içermelidir. | STRING | Evet | Boşluklar temizlendikten sonra minimum 1 karakter |
| `images` | Video oluşturmayı yönlendirmek için isteğe bağlı referans görseller. Toplamda en fazla 14 görsel. | IMAGE | Hayır | Birden çok görsele izin verilir (en fazla 14) |
| `videos` | Video oluşturmayı yönlendirmek veya düzenlemek için isteğe bağlı referans videolar. Her biri en fazla 10 saniye olmak üzere en fazla 3 video. | VIDEO | Hayır | Birden çok videoya izin verilir (en fazla 3, her biri en fazla 10 sn) |
| `temperature` | Oluşturmadaki rastgeleliği kontrol eder (varsayılan: 1.0). | FLOAT | Hayır | 0.0 ile 2.0 arası |
| `top_p` | Nucleus örnekleme parametresi (varsayılan: 0.95). | FLOAT | Hayır | 0.0 ile 1.0 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Gemini modelinden sesli olarak oluşturulan video. | VIDEO |
| `STRING` | Modelden gelen akıl yürütme veya açıklamalar gibi herhangi bir metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/tr.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
