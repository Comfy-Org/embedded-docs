> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/tr.md)

CLIPMergeSubtract düğümü, bir CLIP modelinin ağırlıklarını diğerinden çıkararak model birleştirme işlemi gerçekleştirir. İlk modeli klonlayarak ve ardından ikinci modelden anahtar yamaları çıkararak, çıkarma gücünü kontrol etmek için ayarlanabilir bir çarpanla yeni bir CLIP modeli oluşturur. Bu, temel modelden belirli özellikleri kaldırarak ince ayarlı model harmanlamasına olanak tanır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Evet | - | Klonlanacak ve değiştirilecek temel CLIP modeli |
| `clip2` | CLIP | Evet | - | Anahtar yamaları temel modelden çıkarılacak CLIP modeli |
| `çarpan` | FLOAT | Evet | -10.0 ile 10.0 arası | Çıkarma işleminin gücünü kontrol eder (varsayılan: 1.0) |

**Not:** Düğüm, çarpan değerinden bağımsız olarak `.position_ids` ve `.logit_scale` parametrelerini çıkarma işleminden hariç tutar.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `clip` | CLIP | İkinci modelin ağırlıklarının birinciden çıkarılmasıyla elde edilen sonuç CLIP modeli |

---
**Source fingerprint (SHA-256):** `3136cf509fcbfa291af8f820928a6cc14de7a586f953af0ada9bea949b437d86`
