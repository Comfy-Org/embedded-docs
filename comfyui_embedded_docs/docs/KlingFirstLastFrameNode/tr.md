# Kling 3.0 İlk-Son-Kareden Videoya

Bu düğüm, Kling 3.0 modelini kullanarak bir video oluşturur. Videoyu bir metin istemine, belirtilen bir süreye ve sağlanan iki görsele (başlangıç karesi ve bitiş karesi) dayanarak oluşturur. Düğüm, video için isteğe bağlı olarak eşlik eden bir ses de oluşturabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Video oluşturmayı yönlendiren metin açıklaması. 1 ile 2500 karakter arasında olmalıdır. | STRING | Evet | Yok |
| `süre` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Hayır | 3 ile 15 |
| `ilk_kare` | Video için başlangıç görseli. En az 300x300 piksel olmalı ve en boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. | IMAGE | Evet | Yok |
| `son_kare` | Video için bitiş görseli. En az 300x300 piksel olmalı ve en boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. | IMAGE | Evet | Yok |
| `ses_oluştur` | Video için ses oluşturulup oluşturulmayacağını kontrol eder (varsayılan: True). | BOOLEAN | Hayır | Yok |
| `model` | Model ve oluşturma ayarları. Bu seçeneğin seçilmesi, iç içe geçmiş bir `resolution` parametresini ortaya çıkarır. | COMBO | Hayır | `"kling-v3"` |
| `model.resolution` | Oluşturulan video için çözünürlük. Bu parametre yalnızca `model` `"kling-v3"` olarak ayarlandığında kullanılabilir (varsayılan: `"1080p"`). | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol etmek için kullanılan bir sayı. Tohum değerinden bağımsız olarak sonuçlar deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 |

**Not:** Düğümün düzgün çalışması için `first_frame` ve `end_frame` görsellerinin belirtilen minimum boyut ve en boy oranı gereksinimlerini karşılaması gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `5c904fec35b2bb41cf521263b1b06fd36ba227400b4cec24e79a4e80618e4bae`
