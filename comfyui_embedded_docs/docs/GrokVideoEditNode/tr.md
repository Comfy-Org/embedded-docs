# Grok Video Düzenle

Bu düğüm, mevcut bir videoyu metin istemine dayalı olarak düzenlemek için Grok API'sini kullanır. Videonuzu yükler, açıklamanıza göre videoyu değiştirmesi için AI modeline bir istek gönderir ve yeni oluşturulan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video düzenleme için kullanılacak AI modeli (varsayılan: "grok-imagine-video"). | COMBO | Evet | "grok-imagine-video" |
| `istem` | İstenen videonun metin açıklaması. | STRING | Evet | Yok |
| `video` | Düzenlenecek giriş videosu. Desteklenen maksimum süre 8,7 saniye ve dosya boyutu 50 MB'tır. | VIDEO | Evet | Yok |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 - 2147483647 |

**Kısıtlamalar:**

* `prompt` boş olmamalıdır.
* Giriş `video` süresi 1 ile 8,7 saniye arasında olmalıdır.
* Giriş `video` dosya boyutu 50 MB'ı aşmamalıdır.

**Not:** Bu düğüm bir API düğümüdür ve çalıştırmak için bir Comfy.org hesabı ve API anahtarı gerektirir. Kullanım, video saniyesi başına yaklaşık 0,06 $ olarak ücretlendirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | AI modeli tarafından oluşturulan düzenlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`
