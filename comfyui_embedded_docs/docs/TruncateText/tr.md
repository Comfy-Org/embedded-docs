Bu belge, yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/en.md)

Bu düğüm, metni belirtilen maksimum uzunlukta keserek kısaltır. Herhangi bir girdi metnini alır ve yalnızca ayarladığınız karakter sayısına kadar olan ilk kısmı döndürür. Metnin belirli bir boyutu aşmamasını sağlamanın basit bir yoludur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `text` | Kısaltılacak metin dizesi. | STRING | Evet | Yok |
| `max_length` | Maksimum metin uzunluğu. Metin, bu karakter sayısından sonra kesilir (varsayılan: 77). | INT | Evet | 1 ile 10000 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `string` | Girdiden yalnızca ilk `max_length` karakterini içeren kısaltılmış metin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/tr.md)

---
**Source fingerprint (SHA-256):** `271a77a910967c4fd86a07485449679fb8db89f6b3f2bf0a8fa2ff224ea2f7b2`
