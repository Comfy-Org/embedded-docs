> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/tr.md)

## Genel Bakış

Krea 2 Görsel düğümü, Krea 2 yapay zeka modelini kullanarak görseller oluşturur. İki model çeşidini destekler: Orta (Medium) ifade edici illüstrasyonlar için, Büyük (Large) ise ifade edici fotogerçekçilik için. Oluşturulan görseli etkilemek için isteğe bağlı olarak bir ruh hali panosu (moodboard) ve en fazla 10 görsel stil referansı ekleyebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Görsel için metin istemi. |
| `model` | DICT | Evet | Aşağıya bakın | Krea 2 Orta, ifade edici illüstrasyonlar için en iyisidir; Krea 2 Büyük ise ifade edici fotogerçekçilik için en iyisidir. |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Tekrarlanabilirlik için rastgele tohum (varsayılan: 0). |

`model` parametresi, aşağıdaki alt parametrelere sahip bir sözlüktür:

| Alt Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|---------------|-----------|----------|-------|-------------|
| `model` | STRING | Evet | `"krea 2 medium"`<br>`"krea 2 large"` | Krea 2 model çeşidini seçer. |
| `aspect_ratio` | STRING | Evet | Yok | Oluşturulan görsel için en-boy oranı. |
| `resolution` | STRING | Evet | Yok | Oluşturulan görsel için çözünürlük. |
| `creativity` | FLOAT | Evet | Yok | Oluşturmanın yaratıcılık seviyesini kontrol eder. |
| `moodboard_id` | STRING | Hayır | Yok | Görseli etkilemek için bir Krea ruh hali panosunun UUID'si. Geçerli bir UUID olmalıdır. |
| `moodboard_strength` | FLOAT | Hayır | Yok | Ruh hali panosu etkisinin gücü (varsayılan: 0.35). |
| `style_reference` | LIST | Hayır | 0 ile 10 öğe arası | Görsel stil referanslarının listesi. Her referans bir `url` (STRING) ve `strength` (FLOAT) içermelidir. |

**Kısıtlamalar:**
- `moodboard_id` geçerli bir UUID olmalıdır (örneğin, `"123e4567-e89b-12d3-a456-426614174000"`). Krea web sitesinden kopyalayın.
- `style_reference` en fazla 10 görsel stil referansı kabul eder.
- `prompt` en az 1 karakter uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Bir tensör olarak oluşturulan görsel. |

---
**Source fingerprint (SHA-256):** `6aeb2d935ef5df5699a19271c9ceb766892ef4b0e4f67bfa540bf12ffadf362d`
