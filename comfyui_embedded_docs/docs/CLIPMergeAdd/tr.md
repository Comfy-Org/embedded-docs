> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/tr.md)

CLIPMergeAdd düğümü, ikinci modelden yamaları birinci modele ekleyerek iki CLIP modelini birleştirir. İlk CLIP modelinin bir kopyasını oluşturur ve ikinci modelden konum kimlikleri ile logit ölçek parametreleri hariç tutularak anahtar yamaları seçici bir şekilde dahil eder. Bu, temel modelin yapısını korurken CLIP model bileşenlerini birleştirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | Evet | - | Kopyalanacak ve birleştirme için temel olarak kullanılacak ana CLIP modeli |
| `clip2` | CLIP | Evet | - | Temel modele eklenecek anahtar yamaları sağlayan ikincil CLIP modeli |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CLIP` | CLIP | İkincil modelden eklenen yamalarla birlikte temel model yapısını içeren birleştirilmiş bir CLIP modeli |