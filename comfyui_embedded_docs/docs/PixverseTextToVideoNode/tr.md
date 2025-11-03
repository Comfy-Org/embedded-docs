> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/tr.md)

Metin ve çıktı boyutuna dayalı olarak videolar oluşturur. Bu düğüm, PixVerse API'si aracılığıyla video çıktısı üreterek, metin açıklamaları ve çeşitli oluşturma parametrelerini kullanarak video içeriği oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Video oluşturma için komut (varsayılan: "") |
| `en_boy_oranı` | COMBO | Evet | PixverseAspectRatio'dan seçenekler | Oluşturulan video için en-boy oranı |
| `kalite` | COMBO | Evet | PixverseQuality'dan seçenekler | Video kalite ayarı (varsayılan: PixverseQuality.res_540p) |
| `süre_saniye` | COMBO | Evet | PixverseDuration'dan seçenekler | Oluşturulan videonun saniye cinsinden süresi |
| `hareket_modu` | COMBO | Evet | PixverseMotionMode'dan seçenekler | Video oluşturma için hareket stili |
| `tohum` | INT | Evet | 0 ile 2147483647 arası | Video oluşturma için tohum değeri (varsayılan: 0) |
| `negatif_istem` | STRING | Hayır | - | İstenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") |
| `pixverse_şablonu` | CUSTOM | Hayır | - | Oluşturma stilini etkilemek için PixVerse Şablon düğümü tarafından oluşturulan isteğe bağlı bir şablon |

**Not:** 1080p kalite kullanıldığında, hareket modu otomatik olarak normal olarak ayarlanır ve süre 5 saniye ile sınırlandırılır. 5 saniye olmayan süreler için hareket modu da otomatik olarak normal olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |