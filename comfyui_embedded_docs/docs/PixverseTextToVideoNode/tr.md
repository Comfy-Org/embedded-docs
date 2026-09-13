# PixVerse Metinden Videoya

PixVerse API'sini kullanarak bir metin isteminden videolar üretir. Bu düğüm, videonun şeklini, kalitesini, uzunluğunu ve hareket stilini kontrol etmenizi sağlar ve isteğe bağlı olarak kaydedilmiş bir stil şablonu uygulayabilir. İsteği gönderir, üretimin tamamlanmasını bekler ve tamamlanan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için istem (varsayılan: "") | STRING | Evet | En az 1 karakter içermelidir |
| `aspect_ratio` | Üretilen video için en-boy oranı | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `quality` | Video kalitesi ayarı (varsayılan: "540p") | COMBO | Evet | `"540p"`<br>`"1080p"` |
| `duration_seconds` | Üretilen videonun saniye cinsinden süresi | COMBO | Evet | `"5"`<br>`"10"` |
| `motion_mode` | Video üretimi için hareket stili | COMBO | Evet | `"normal"`<br>`"fast"` |
| `seed` | Video üretimi için tohum (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |
| `negative_prompt` | Bir görüntüdeki istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") | STRING | Hayır | - |
| `pixverse_template` | Üretim stilini etkilemek için PixVerse Template düğümü tarafından oluşturulan isteğe bağlı şablon | CUSTOM | Hayır | - |

**Not:** `prompt` en az 1 karakter içermelidir. 1080p kalitesi seçildiğinde, hareket modu otomatik olarak `normal` olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki herhangi bir süre için hareket modu da otomatik olarak `normal` olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
