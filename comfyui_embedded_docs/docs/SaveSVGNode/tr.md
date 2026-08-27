# SVGDüğümünüKaydet

SVG dosyalarını diske kaydeder. Bu düğüm, SVG verisini girdi olarak alır ve isteğe bağlı meta veri gömme ile çıktı dizininize kaydeder. Düğüm, sayaç son ekleriyle dosya adlandırmayı otomatik olarak yönetir ve iş akışı prompt bilgilerini doğrudan SVG dosyasına gömebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `svg` | Diske kaydedilecek SVG verisi | SVG | Evet | - |
| `dosya_adı_ön_eki` | Kaydedilecek dosya için önektir. %date:yyyy-MM-dd% veya %Empty Latent Image.width% gibi düğümlerden değer eklemek için biçimlendirme bilgileri içerebilir. (varsayılan: "svg/ComfyUI") | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `svg` | Kaydetme sonrasında iletilen orijinal SVG verisi | SVG |
| `ui` | ComfyUI arayüzünde görüntülenmek üzere dosya adı, alt klasör ve tür içeren kaydedilmiş dosya bilgisi | DICT |

**Not:** Bu düğüm, mevcut olduğunda iş akışı meta verilerini (prompt ve ek PNG bilgisi) SVG dosyasına otomatik olarak gömer. Meta veriler, SVG'nin metadata öğesi içinde bir CDATA bölümü olarak eklenir. Dosyalar `filename_prefix_00001_.svg` deseniyle kaydedilir; bir grup işlenirken, önekteki `%batch_num%` değeri, geçerli grup öğesinin diziniyle değiştirilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/tr.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
