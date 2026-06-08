## Genel Bakış

Krea 2 Görsel düğümü, Krea 2 yapay zeka modelini kullanarak görseller oluşturur. İki model çeşidini destekler: Orta (Medium) ifade edici illüstrasyonlar için, Büyük (Large) ise ifade edici fotogerçekçilik için. Oluşturulan görseli etkilemek için isteğe bağlı olarak bir ruh hali panosu (moodboard) ve en fazla 10 görsel stil referansı ekleyebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Görsel için metin istemi. | STRING | Evet | Yok |
| `model` | Krea 2 Orta, ifade edici illüstrasyonlar için en iyisidir; Krea 2 Büyük ise ifade edici fotogerçekçilik için en iyisidir. | DICT | Evet | Aşağıya bakın |
| `seed` | Tekrarlanabilirlik için rastgele tohum (varsayılan: 0). | INT | Evet | 0 ile 2147483647 arası |

`model` parametresi, aşağıdaki alt parametrelere sahip bir sözlüktür:

| Alt Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Krea 2 model çeşidini seçer. | STRING | Evet | `"krea 2 medium"`<br>`"krea 2 large"` |
| `aspect_ratio` | Oluşturulan görsel için en-boy oranı. | STRING | Evet | Yok |
| `resolution` | Oluşturulan görsel için çözünürlük. | STRING | Evet | Yok |
| `creativity` | Oluşturmanın yaratıcılık seviyesini kontrol eder. | FLOAT | Evet | Yok |
| `moodboard_id` | Görseli etkilemek için bir Krea ruh hali panosunun UUID'si. Geçerli bir UUID olmalıdır. | STRING | Hayır | Yok |
| `moodboard_strength` | Ruh hali panosu etkisinin gücü (varsayılan: 0.35). | FLOAT | Hayır | Yok |
| `style_reference` | Görsel stil referanslarının listesi. Her referans bir `url` (STRING) ve `strength` (FLOAT) içermelidir. | LIST | Hayır | 0 ile 10 öğe arası |

**Kısıtlamalar:**
- `moodboard_id` geçerli bir UUID olmalıdır (örneğin, `"123e4567-e89b-12d3-a456-426614174000"`). Krea web sitesinden kopyalayın.
- `style_reference` en fazla 10 görsel stil referansı kabul eder.
- `prompt` en az 1 karakter uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Bir tensör olarak oluşturulan görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `6aeb2d935ef5df5699a19271c9ceb766892ef4b0e4f67bfa540bf12ffadf362d`
