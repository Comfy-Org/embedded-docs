Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/en.md)

## Genel Bakış

Bu düğüm, Luma UNI-1 modeli tarafından desteklenen bir metin istemi kullanarak mevcut bir görüntüyü düzenler. Bir kaynak görüntü ve istenen değişikliğin açıklamasını alır, ardından görüntünün yeni bir düzenlenmiş sürümünü oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `source` | Düzenlenecek kaynak görüntü. | IMAGE | Evet | - |
| `prompt` | İstenen düzenlemenin açıklaması. Varsayılan: "" (boş dize). | STRING | Evet | 1–6000 karakter |
| `model` | Düzenleme için kullanılacak model. | MODEL | Evet | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 ile 2147483647 arası |

**Parametre Kısıtlamaları:**
- `prompt` 1 ile 6000 karakter arasında olmalıdır.
- `model` parametresi, `"uni-1"` veya `"uni-1-max"` olarak ayarlandığında ek alt parametreler (`style`, `web_search` ve `image_ref` gibi) sağlayan dinamik bir birleşik giriş kutusudur. `image_ref` alt parametresi en fazla 8 görüntü referansı kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Luma UNI-1 modeli tarafından oluşturulan düzenlenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/tr.md)

---
**Source fingerprint (SHA-256):** `7026e3ce818b0a9710624bd071fc2049950290f89c7d0365ff44236e9ad5eaed`
