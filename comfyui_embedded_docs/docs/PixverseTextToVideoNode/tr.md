# PixVerse Metinden Videoya

Bir metin istemi ve çeşitli üretim parametrelerine dayalı olarak videolar oluşturur. Bu düğüm, PixVerse API'sini kullanarak video içeriği üretir; en boy oranı, kalite, süre, hareket stili ve daha fazlası üzerinde kontrol sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Video üretimi için istem (varsayılan: "") | STRING | Evet | - |
| `en_boy_oranı` | Oluşturulan video için en boy oranı | COMBO | Evet | PixverseAspectRatio seçenekleri |
| `kalite` | Video kalite ayarı (varsayılan: PixverseQuality.res_540p) | COMBO | Evet | PixverseQuality seçenekleri |
| `süre_saniye` | Oluşturulan videonun saniye cinsinden süresi | COMBO | Evet | PixverseDuration seçenekleri |
| `hareket_modu` | Video üretimi için hareket stili | COMBO | Evet | PixverseMotionMode seçenekleri |
| `tohum` | Video üretimi için tohum değeri (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |
| `negatif_istem` | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") | STRING | Hayır | - |
| `pixverse_şablonu` | PixVerse Şablon düğümü tarafından oluşturulan, üretim stilini etkilemek için isteğe bağlı bir şablon | CUSTOM | Hayır | - |

**Not:** 1080p kalite kullanıldığında, hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki süreler için de hareket modu otomatik olarak normal olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
