# Breeze Voice Selector

Öne çıkan bir Breeze sesini veya herhangi bir Breeze ses kimliğini seçer ve bunu Breeze Text to Speech'e iletir. Düğüm yalnızca bir kimliği çözümler ve hiçbir API çağrısı yapmaz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `language` | Öne çıkan seslerin dil grubu veya bir kimlik girmek için `custom`. Varsayılan: `"English"`. | DYNAMIC_COMBO | Evet | `"English"`<br>`"Chinese"`<br>`"Japanese"`<br>`"custom"` |

### Dil "English", "Chinese" ve "Japanese" Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `voice` | O dildeki öne çıkan ses. | COMBO | Evet | Birden çok seçenek mevcut |

### Dil "custom" Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `voice_id` | Diğer Breeze düğümleri tarafından oluşturulan bir ses gibi herhangi bir Breeze ses kimliği. Yalnızca harfler, rakamlar, `_` ve `-`. Varsayılan: boş. | STRING | Evet | Breeze ses kimliği |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voice` | Seçilen Breeze sesi. | BREEZE_VOICE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/tr.md)

---
**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`
