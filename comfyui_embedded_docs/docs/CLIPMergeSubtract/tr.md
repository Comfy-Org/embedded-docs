> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/tr.md)

CLIPMergeSubtract düğümü, bir CLIP modelinin ağırlıklarını diğerinden çıkararak model birleştirme işlemi gerçekleştirir. İlk modeli klonlayarak ve ardından ikinci modelin anahtar yamalarını, çıkarma gücünü kontrol eden ayarlanabilir bir çarpanla çıkararak yeni bir CLIP modeli oluşturur. Bu, temel modelden belirli özellikleri kaldırarak hassas ayarlanmış model harmanlamaya olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Evet | - | Klonlanacak ve değiştirilecek temel CLIP modeli |
| `clip2` | CLIP | Evet | - | Anahtar yamaları temel modelden çıkarılacak olan CLIP modeli |
| `multiplier` | FLOAT | Evet | -10.0 - 10.0 | Çıkarma işleminin gücünü kontrol eder (varsayılan: 1.0) |

**Not:** Düğüm, çarpan değerinden bağımsız olarak, çıkarma işleminden `.position_ids` ve `.logit_scale` parametrelerini hariç tutar.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `clip` | CLIP | İkinci modelin ağırlıkları birinciden çıkarıldıktan sonra elde edilen CLIP modeli |