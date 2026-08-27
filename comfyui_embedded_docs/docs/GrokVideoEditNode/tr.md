# Grok Video Düzenle

Bu düğüm, Grok API'sini kullanarak mevcut bir videoyu metin istemine göre düzenler. Videonuzu yükler, yapay zeka modeline açıklamanıza göre videoyu değiştirmesi için istek gönderir ve yeni oluşturulan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video düzenleme için kullanılacak yapay zeka modeli (varsayılan: "grok-imagine-video"). | COMBO | Evet | "grok-imagine-video" |
| `istem` | İstenen videonun metin açıklaması. | STRING | Evet | N/A |
| `video` | Düzenlenecek giriş videosu. Desteklenen maksimum süre 8,7 saniye ve 50MB dosya boyutudur. | VIDEO | Evet | N/A |
| `tohum` | Düğümün yeniden çalışıp çalışmayacağını belirleyen seed değeri; gerçek sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 |

**Kısıtlamalar:**

* `prompt` boş olmamalıdır.
* Giriş `video` süresi 1 ila 8,7 saniye arasında olmalıdır.
* Giriş `video` dosya boyutu 50MB'ı aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Yapay zeka modeli tarafından oluşturulan düzenlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`
