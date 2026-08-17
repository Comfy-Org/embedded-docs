# SVGDüğümünüKaydet

SVG dosyalarını diske kaydedin. Bu düğüm, SVG verisini girdi olarak alır ve isteğe bağlı meta veri gömme ile çıktı dizininize kaydeder. Düğüm, sayaç son ekleriyle dosya adlandırmayı otomatik olarak yönetir ve iş akışı prompt bilgilerini doğrudan SVG dosyasına gömer.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `svg` | Diske kaydedilecek SVG verisi | SVG | Evet | - |
| `filename_prefix` | Kaydedilecek dosyanın önekidir. Bu, düğümlerden değerler eklemek için %date:yyyy-MM-dd% veya %Empty Latent Image.width% gibi biçimlendirme bilgileri içerebilir. (varsayılan: "svg/ComfyUI") | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `svg` | Diske kaydedilen SVG verisi | SVG |
| `ui` | ComfyUI arayüzünde görüntülenmek üzere dosya adı, alt klasör ve tür dahil dosya bilgilerini döndürür | DICT |

**Not:** Bu düğüm, mevcut olduğunda iş akışı meta verilerini (prompt ve ek PNG bilgisi) otomatik olarak SVG dosyasına gömer. Meta veri, SVG'nin meta veri öğesi içine bir CDATA bölümü olarak eklenir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/tr.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
