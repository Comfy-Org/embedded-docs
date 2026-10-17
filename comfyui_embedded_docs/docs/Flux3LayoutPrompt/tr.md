# FLUX 3 Image Layout Prompt

FLUX 3 Image'ın bir istemden okuduğu düzen tablosunu oluşturur. Create Bounding Boxes düğümünde çizilen öğeleri alır ve bunları isteminize, her biri bir kimlik, koordinatları ve açıklaması olan bir kutu listesi olarak ekler. İstemdeki bir kutuyu `<obj_N>` olarak belirtin; böylece sözcükleri o bölgeye bağlarsınız, ardından çıktıyı FLUX 3 Image düğümünün istem girişine bağlayın. Hiçbir öğe bağlı değilse istem değiştirilmeden döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | İstem metni. Sözcükleri ona bağlamak için N numaralı kutuyu `<obj_N>` olarak belirtin. | STRING | Evet | - |
| `element` | Düzene yerleştirilecek öğeler; Create Bounding Boxes düğümünden alınır. Renk paletleri kullanılmaz, bu nedenle renkleri bunun yerine açıklamada belirtin. | ARRAY | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `prompt` | Kutu düzen tablosu eklenmiş, FLUX 3 Image düğümüne beslenmeye hazır istem. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3LayoutPrompt/tr.md)

---
**Source fingerprint (SHA-256):** `ac8f61701c8da0a6fc8361aeebf7fc5e7aa338ce6ad8689718904caa9c53e3b8`
