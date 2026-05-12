> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/tr.md)

Bu belge, yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/en.md)

## Genel Bakış

Bu düğüm, Luma UNI-1 modeli tarafından desteklenen bir metin istemi kullanarak mevcut bir görüntüyü düzenler. Bir kaynak görüntü ve istenen değişikliğin açıklamasını alır, ardından görüntünün yeni, düzenlenmiş bir sürümünü oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `source` | IMAGE | Evet | - | Düzenlenecek kaynak görüntü. |
| `prompt` | STRING | Evet | 1–6000 karakter | İstenen düzenlemenin açıklaması. Varsayılan: "" (boş dize). |
| `model` | MODEL | Evet | `"uni-1"`<br>`"uni-1-max"` | Düzenleme için kullanılacak model. |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar, tohumdan bağımsız olarak deterministik değildir. Varsayılan: 0. |

**Parametre Kısıtlamaları:**
- `prompt` 1 ile 6000 karakter arasında olmalıdır.
- `model` parametresi, `"uni-1"` veya `"uni-1-max"` olarak ayarlandığında ek alt parametreler (`style`, `web_search` ve `image_ref` gibi) sağlayan dinamik bir kombinasyon kutusudur. `image_ref` alt parametresi en fazla 8 görüntü referansı kabul eder.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Luma UNI-1 modeli tarafından oluşturulan düzenlenmiş görüntü. |