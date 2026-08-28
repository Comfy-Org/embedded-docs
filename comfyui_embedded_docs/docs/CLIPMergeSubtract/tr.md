# CLIP Birleştirme Çıkar

CLIPMergeSubtract düğümü, bir CLIP modelinin ağırlıklarını diğerinden çıkararak model birleştirme işlemi gerçekleştirir. İlk modeli klonlayarak yeni bir CLIP modeli oluşturur ve ardından ikinci modelin anahtar yamalarını, çıkarma gücünü kontrol etmek için ayarlanabilir bir çarpanla çıkarır. Bu, temel modelden belirli özellikleri kaldırarak ince ayarlı model harmanlamasına olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip1` | Klonlanacak ve değiştirilecek temel CLIP modeli | CLIP | Evet | - |
| `clip2` | Anahtar yamaları temel modelden çıkarılacak CLIP modeli | CLIP | Evet | - |
| `çarpan` | Çıkarma işleminin gücünü kontrol eder (varsayılan: 1.0) | FLOAT | Evet | -10.0 ile 10.0 (step: 0.01) |

**Not:** Düğüm, çarpan değerinden bağımsız olarak `.position_ids` ve `.logit_scale` parametrelerini çıkarma işleminden hariç tutar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip` | İkinci modelin ağırlıklarının birinciden çıkarılmasıyla elde edilen CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/tr.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`
