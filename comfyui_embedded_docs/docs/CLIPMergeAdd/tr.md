# CLIP Birleştirme Ekle

CLIPMergeAdd düğümü, ikinci modeldeki yamaları birinci modele ekleyerek iki CLIP modelini birleştirir. Birinci CLIP modelinin bir kopyasını oluşturur ve ikinci modeldeki anahtar yamaları seçerek dahil eder; konum kimliklerini ve logit ölçeği parametrelerini hariç tutar. Bu, temel modelin yapısını korurken CLIP model bileşenlerini birleştirmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip1` | Birleştirme için temel olarak kullanılacak ve klonlanacak temel CLIP modeli | CLIP | Evet | - |
| `clip2` | Temel modele eklenecek anahtar yamaları sağlayan ikincil CLIP modeli | CLIP | Evet | - |

`clip2` içinde `.position_ids` veya `.logit_scale` ile biten anahtarlar atlanır; böylece bu parametreler `clip1` değerlerini korur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CLIP` | İkincil modelden eklenen yamalarla birlikte temel model yapısını içeren birleştirilmiş CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/tr.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
