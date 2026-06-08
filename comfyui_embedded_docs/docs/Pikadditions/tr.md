Pikadditions düğümü, videonuza herhangi bir nesne veya görsel eklemenizi sağlar. Bir video yükler ve eklemek istediğiniz öğeyi belirterek kusursuz bir şekilde bütünleşmiş bir sonuç elde edersiniz. Bu düğüm, doğal görünümlü bir entegrasyonla videolara görseller eklemek için Pika API'sini kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Görsel eklenecek video. | VIDEO | Evet | - |
| `image` | Videoya eklenecek görsel. | IMAGE | Evet | - |
| `prompt_text` | Videoya ne ekleneceğine dair metin açıklaması. | STRING | Evet | - |
| `negative_prompt` | Videoda kaçınılması gerekenlerin metin açıklaması. | STRING | Evet | - |
| `seed` | Tekrarlanabilir sonuçlar için rastgele tohum değeri. | INT | Evet | 0 ile 4294967295 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Görselin eklendiği işlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/tr.md)

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`
