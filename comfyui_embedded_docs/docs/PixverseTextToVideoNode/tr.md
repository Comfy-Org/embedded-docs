# PixVerse Metinden Videoya

Metin istemine ve çeşitli üretim parametrelerine dayalı videolar üretir. Bu düğüm, PixVerse API'sini kullanarak video içeriği oluşturur; en boy oranı, kalite, süre, hareket stili ve daha fazlası üzerinde kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Video üretimi için istem (varsayılan: "") | STRING | Evet | - |
| `en_boy_oranı` | Üretilen video için en boy oranı | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `kalite` | Video kalitesi ayarı (varsayılan: "540p") | COMBO | Evet | `"540p"`<br>`"1080p"` |
| `süre_saniye` | Üretilen videonun saniye cinsinden süresi | COMBO | Evet | `"5"`<br>`"10"` |
| `hareket_modu` | Video üretimi için hareket stili | COMBO | Evet | `"normal"`<br>`"fast"` |
| `tohum` | Video üretimi için tohum (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |
| `negatif_istem` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") | STRING | Hayır | - |
| `pixverse_şablonu` | PixVerse Template düğümü tarafından oluşturulan, üretim stilini etkilemek için isteğe bağlı bir şablon | CUSTOM | Hayır | - |

**Not:** `prompt` en az 1 karakter içermelidir. 1080p kalite kullanıldığında, hareket modu otomatik olarak `normal` olarak ayarlanır ve süre 5 saniye ile sınırlıdır. 5 saniye dışındaki süreler için hareket modu da otomatik olarak `normal` olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
