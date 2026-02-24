> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/tr.md)

Batch Masks düğümü, birden fazla bireysel maske girdisini tek bir toplu işte birleştirir. Değişken sayıda maske girdisi alır ve bunları tek bir toplu maske tensörü olarak çıktılar, böylece sonraki düğümlerde maskelerin toplu işlem görmesine olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `mask_0` | MASK | Evet | - | İlk maske girdisi. |
| `mask_1` | MASK | Evet | - | İkinci maske girdisi. |
| `mask_2` ila `mask_49` | MASK | Hayır | - | Ek isteğe bağlı maske girdileri. Düğüm toplamda minimum 2, maksimum 50 maske kabul edebilir. |

**Not:** Bu düğüm otomatik büyüyen bir girdi şablonu kullanır. En az iki maske (`mask_0` ve `mask_1`) bağlamanız gerekir. Toplamda 50 maske olacak şekilde en fazla 48 ek isteğe bağlı maske girdisi (`mask_2`'den `mask_49`'a kadar) ekleyebilirsiniz. Bağlanan tüm maskeler tek bir toplu işte birleştirilecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | MASK | Tüm girdi maskelerinin üst üste istiflendiği tek bir toplu maske. |
