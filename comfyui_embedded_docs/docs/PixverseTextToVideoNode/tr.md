> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/tr.md)

Bir metin istemi ve çeşitli üretim parametrelerine dayalı olarak videolar oluşturur. Bu düğüm, PixVerse API'sini kullanarak video içeriği üretir; en boy oranı, kalite, süre, hareket stili ve daha fazlası üzerinde kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Video üretimi için istem (varsayılan: "") |
| `aspect_ratio` | COMBO | Evet | PixverseAspectRatio seçenekleri | Oluşturulan video için en boy oranı |
| `quality` | COMBO | Evet | PixverseQuality seçenekleri | Video kalite ayarı (varsayılan: PixverseQuality.res_540p) |
| `duration_seconds` | COMBO | Evet | PixverseDuration seçenekleri | Oluşturulan videonun saniye cinsinden süresi |
| `motion_mode` | COMBO | Evet | PixverseMotionMode seçenekleri | Video üretimi için hareket stili |
| `seed` | INT | Evet | 0 ila 2147483647 | Video üretimi için tohum değeri (varsayılan: 0) |
| `negative_prompt` | STRING | Hayır | - | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") |
| `pixverse_template` | CUSTOM | Hayır | - | PixVerse Şablon düğümü tarafından oluşturulan, üretim stilini etkilemek için isteğe bağlı bir şablon |

**Not:** 1080p kalite kullanıldığında, hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye dışındaki süreler için de hareket modu otomatik olarak normal olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
