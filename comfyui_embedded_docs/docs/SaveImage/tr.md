# Görüntüyü Kaydet

SaveImage düğümü, aldığı görselleri `ComfyUI/output` dizininize kaydeder. Her görseli bir PNG dosyası olarak kaydeder ve ileride başvurmak üzere, istem (prompt) gibi iş akışı meta verilerini kaydedilen dosyaya gömer.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Kaydedilecek görseller. | IMAGE | Evet | - |
| `filename_prefix` | Kaydedilecek dosyanın öneki. Bu, düğümlerden değerler eklemek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: "ComfyUI"). | STRING | Evet | - |
| `prompt` | Gizli girdi, ComfyUI tarafından otomatik sağlanır: kaydedilen PNG dosyasına meta veri olarak gömülen istem verisi. | PROMPT | Hayır | - |
| `extra_pnginfo` | Gizli girdi, ComfyUI tarafından otomatik sağlanır: kaydedilen PNG dosyasına meta veri olarak gömülen ek iş akışı bilgisi. | EXTRA_PNGINFO | Hayır | - |

Her görsel bir PNG dosyası olarak kaydedilir. Kaydedilen dosya adında, önekteki `%batch_num%` ifadesi görselin batch numarasıyla değiştirilir ve sonuna sıfırla doldurulmuş bir sayaç eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Kaydedilen görsellerin aynısı; diğer düğümler tarafından kullanılabilmeleri için olduğu gibi iletilir. | IMAGE |
| `ui` | ComfyUI arayüzünde görüntülenen, kaydedilen görsellerin dosya adları, alt klasörleri ve türlerinin listesini içeren UI sonucu. | UI_RESULT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/tr.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
