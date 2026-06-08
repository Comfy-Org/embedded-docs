PixVerse Şablon düğümü, PixVerse video oluşturma için mevcut şablonlar arasından seçim yapmanızı sağlar. Seçtiğiniz şablon adını, PixVerse API'sinin video oluşturma için gerektirdiği karşılık gelen şablon kimliğine dönüştürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `şablon` | PixVerse video oluşturma için kullanılacak şablon. Mevcut seçenekler, PixVerse sistemindeki önceden tanımlanmış şablonlara karşılık gelir. | STRING | Evet | Birden çok seçenek mevcut |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pixverse_template` | Seçilen şablon adına karşılık gelen şablon kimliği. Bu kimlik, video oluşturma için diğer PixVerse düğümleri tarafından kullanılabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/tr.md)

---
**Source fingerprint (SHA-256):** `d6ea1eb1cc9a7d33cf69f101990e601189726b9ef9e199fe211087f7070f35d0`
