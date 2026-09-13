# SVGDüğümünüKaydet

SVG dosyalarını diske kaydeder. Bu düğüm, girdi olarak SVG verisi alır ve bunu ComfyUI çıktı dizinine yazar; dosya adlandırmayı sayaç son ekleriyle otomatik olarak yönetir. İş akışı prompt bilgisi mevcut olduğunda, doğrudan SVG dosyasına bir meta veri öğesi olarak gömülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `svg` | Diske kaydedilecek SVG verisi | SVG | Evet | - |
| `filename_prefix` | Kaydedilecek dosyanın ön eki. Düğümlerden değerleri dahil etmek için %date:yyyy-MM-dd% veya %Empty Latent Image.width% gibi biçimlendirme bilgileri içerebilir. (varsayılan: "svg/ComfyUI") | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `svg` | Kaydettikten sonra olduğu gibi iletilen özgün SVG verisi | SVG |
| `ui` | ComfyUI arayüzünde görüntülenmek üzere dosya adı, alt klasör ve türü içeren kaydedilmiş dosya bilgileri | DICT |

**Not:** Bu düğüm, mevcut olduğunda iş akışı meta verilerini (prompt ve ek PNG bilgileri) otomatik olarak SVG dosyasına gömer. Meta veriler, SVG'nin meta veri öğesi içinde bir CDATA bölümü olarak eklenir. Dosyalar `filename_prefix_00001_.svg` deseni kullanılarak kaydedilir; bir toplu işlem işlenirken ön ekteki `%batch_num%`, geçerli toplu işlem öğesinin diziniyle değiştirilir. Bu düğüm bir çıktı düğümüdür; bu nedenle dosyanın kendisi görsel önizleme olarak görüntülenmese bile çıktı klasöründe kaydedilmiş bir sonuç üretir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/tr.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
