> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/tr.md)

LTXVConcatAVLatent düğümü, bir video gizli temsili ile bir ses gizli temsilini birleştirerek tek, birleştirilmiş bir gizli çıktı oluşturur. Her iki girdinin `samples` tensörlerini ve varsa `noise_mask` tensörlerini de birleştirerek, bunları bir video oluşturma işlem hattında ileri işlemeye hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video_latent` | LATENT | Evet | | Video verisinin gizli temsili. |
| `audio_latent` | LATENT | Evet | | Ses verisinin gizli temsili. |

**Not:** `video_latent` ve `audio_latent` girdilerinin `samples` tensörleri birleştirilir. Eğer girdilerden herhangi biri bir `noise_mask` içeriyorsa, bu kullanılır; eğer biri eksikse, onun için birlerden oluşan bir maske (ilgili `samples` ile aynı şekilde) oluşturulur. Ortaya çıkan maskeler daha sonra yine birleştirilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latent` | LATENT | Video ve ses girdilerinden birleştirilmiş `samples`'ı ve uygulanabilirse birleştirilmiş `noise_mask`'i içeren tek bir gizli sözlük. |
