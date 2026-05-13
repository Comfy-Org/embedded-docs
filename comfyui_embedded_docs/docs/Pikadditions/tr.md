> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/tr.md)

Pikadditions düğümü, videonuza herhangi bir nesne veya görsel eklemenizi sağlar. Bir video yükler ve eklemek istediğiniz öğeyi belirterek kusursuz bir şekilde bütünleşmiş bir sonuç elde edersiniz. Bu düğüm, doğal görünümlü bir entegrasyonla videolara görseller eklemek için Pika API'sini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Görsel eklenecek video. |
| `image` | IMAGE | Evet | - | Videoya eklenecek görsel. |
| `prompt_text` | STRING | Evet | - | Videoya ne ekleneceğine dair metin açıklaması. |
| `negative_prompt` | STRING | Evet | - | Videoda kaçınılması gerekenlerin metin açıklaması. |
| `seed` | INT | Evet | 0 ile 4294967295 arası | Tekrarlanabilir sonuçlar için rastgele tohum değeri. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Görselin eklendiği işlenmiş video. |

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`
