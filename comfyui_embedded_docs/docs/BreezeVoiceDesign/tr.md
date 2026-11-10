# Breeze Voice Design

Yazılı bir açıklamadan yeni bir Breeze sesi oluşturur. Sesin bir açıklamasını ve konuşması için bir satır sağlayın; ses bu önizlemeden oluşturulur ve hesabınıza kaydedilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `description` | Sesin 3 ile 500 karakter arası açıklaması: yaş, cinsiyet, aksan, ton, hız. Varsayılan: boş. | STRING | Evet | 3 ile 500 karakter arası |
| `preview_text` | Yeni sesin önizlemede konuşacağı satır, en fazla 500 karakter. Seçilen dilde yazın, çünkü ses bu önizlemeden oluşturulur. Varsayılan: boş. | STRING | Evet | 1 ile 500 karakter arası |
| `language` | Önizleme metninin dili. İngilizce ve Çince her iki modeli de kullanabilir; diğer diller Breeze TTS 2 Multilingual kullanır. | DYNAMIC_COMBO | Evet | Birden çok seçenek mevcut |
| `strength` | Sesin açıklamaya ne kadar sıkı uyduğu. Varsayılan: 4.0. | FLOAT | Hayır | 1.0 ile 10.0 arası (adım: 0.1) |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak belirleyici değildir. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 arası |

### Dil "English" ve "Chinese" Girdileri

Bunlar yalnızca `language` "English" veya "Chinese" olduğunda görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` veya `Breeze TTS 2 Multilingual`. Varsayılan: `"Breeze TTS 2"`. | COMBO | Evet | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voice` | Açıklamaya göre adlandırılan yeni Breeze sesi. | BREEZE_VOICE |
| `preview` | Tasarlanan sesin ses önizlemesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceDesign/tr.md)

---
**Source fingerprint (SHA-256):** `5b0ea4ccd03e442972a71ec839be7b755f569686400e472967a09a956de0982f`
