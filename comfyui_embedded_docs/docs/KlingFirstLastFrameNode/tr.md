> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/tr.md)

Bu düğüm, Kling 3.0 modelini kullanarak bir video oluşturur. Videoyu bir metin istemine, belirtilen bir süreye ve sağlanan iki görsele (başlangıç karesi ve bitiş karesi) dayanarak oluşturur. Düğüm, video için isteğe bağlı olarak eşlik eden bir ses de oluşturabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Video oluşturmayı yönlendiren metin açıklaması. 1 ile 2500 karakter arasında olmalıdır. |
| `duration` | INT | Hayır | 3 ile 15 | Videonun saniye cinsinden uzunluğu (varsayılan: 5). |
| `first_frame` | IMAGE | Evet | Yok | Video için başlangıç görseli. En az 300x300 piksel olmalı ve en boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. |
| `end_frame` | IMAGE | Evet | Yok | Video için bitiş görseli. En az 300x300 piksel olmalı ve en boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. |
| `generate_audio` | BOOLEAN | Hayır | Yok | Video için ses oluşturulup oluşturulmayacağını kontrol eder (varsayılan: True). |
| `model` | COMBO | Hayır | `"kling-v3"` | Model ve oluşturma ayarları. Bu seçeneğin seçilmesi, iç içe geçmiş bir `resolution` parametresini ortaya çıkarır. |
| `model.resolution` | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` | Oluşturulan video için çözünürlük. Bu parametre yalnızca `model` `"kling-v3"` olarak ayarlandığında kullanılabilir (varsayılan: `"1080p"`). |
| `seed` | INT | Hayır | 0 ile 2147483647 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol etmek için kullanılan bir sayı. Tohum değerinden bağımsız olarak sonuçlar deterministik değildir (varsayılan: 0). |

**Not:** Düğümün düzgün çalışması için `first_frame` ve `end_frame` görsellerinin belirtilen minimum boyut ve en boy oranı gereksinimlerini karşılaması gerekir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `5c904fec35b2bb41cf521263b1b06fd36ba227400b4cec24e79a4e80618e4bae`
