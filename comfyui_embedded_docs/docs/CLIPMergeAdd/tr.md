# CLIP Birleştirme Ekle

CLIPMergeAdd düğümü, ikinci modelden gelen yamaları birinci modele ekleyerek iki CLIP modelini birleştirir. İlk CLIP modelinin bir kopyasını oluşturur ve ikinci modelden konum kimlikleri ile logit ölçeği parametrelerini hariç tutarak anahtar yamaları seçici bir şekilde dahil eder. Bu, temel modelin yapısını koruyarak CLIP model bileşenlerini birleştirmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip1` | Birleştirme için temel olarak kullanılacak ve klonlanacak temel CLIP modeli | CLIP | Evet | - |
| `clip2` | Temel modele eklenecek anahtar yamaları sağlayan ikincil CLIP modeli | CLIP | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CLIP` | İkincil modelden eklenen yamalarla birlikte temel model yapısını içeren birleştirilmiş CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/tr.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
