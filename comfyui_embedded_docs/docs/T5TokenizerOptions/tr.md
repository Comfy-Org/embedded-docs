# T5JetonlaştırıcıSeçenekleri

T5TokenizerOptions düğümü, çeşitli T5 model türleri için belirteç (tokenizer) ayarlarını yapılandırır. t5xxl, pile_t5xl, t5base, mt5xl ve umt5xxl dahil birden çok T5 model varyantı için minimum padding ve minimum uzunluk parametrelerini ayarlar. Düğüm bir CLIP girdisi alır, ayarları bunun bir kopyasına uygular ve değiştirilmiş CLIP'i döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Belirteç seçeneklerinin yapılandırılacağı CLIP modeli | CLIP | Evet | - |
| `min_dolgu` | Tüm T5 model türleri için ayarlanacak minimum padding değeri (varsayılan: 0) | INT | Evet | 0 ile 10000 |
| `min_uzunluk` | Tüm T5 model türleri için ayarlanacak minimum uzunluk değeri (varsayılan: 0) | INT | Evet | 0 ile 10000 |

Not: Bu düğüm ComfyUI'de deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm T5 varyantlarına güncellenmiş belirteç seçenekleri uygulanmış değiştirilmiş CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/tr.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
