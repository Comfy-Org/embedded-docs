# CLIP Birleştirme Çıkar

CLIPMergeSubtract düğümü, bir modelin ağırlıklarını diğerinden çıkararak iki CLIP modelini birleştirir. İlk modeli klonlayarak ve ardından ikinci modelden anahtar yamaları çıkararak yeni bir CLIP modeli oluşturur; çıkarma gücünü kontrol etmek için ayarlanabilir bir çarpan kullanır. Bu, temel modelden belirli özelliklerin kaldırılmasıyla ince ayarlı model harmanlamasına olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip1` | Klonlanacak ve değiştirilecek temel CLIP modeli | CLIP | Yes | - |
| `clip2` | Anahtar yamaları temel modelden çıkarılacak CLIP modeli | CLIP | Yes | - |
| `multiplier` | Çıkarma işleminin gücünü kontrol eder (varsayılan: 1.0) | FLOAT | Yes | -10.0 ila 10.0 (adım: 0.01) |

**Not:** Düğüm, çarpan değerinden bağımsız olarak `.position_ids` ve `.logit_scale` parametrelerini çıkarma işlemine dahil etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip` | İkinci modelin ağırlıklarının birinciden çıkarılmasıyla elde edilen CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/tr.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`
