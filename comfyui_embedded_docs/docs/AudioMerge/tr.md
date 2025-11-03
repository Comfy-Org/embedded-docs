> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/tr.md)

AudioMerge düğümü, iki ses parçasını dalga formlarını üst üste bindirerek birleştirir. Her iki ses girişinin örnekleme hızlarını otomatik olarak eşleştirir ve birleştirmeden önce uzunluklarını eşit olacak şekilde ayarlar. Düğüm, ses sinyallerini birleştirmek için çeşitli matematiksel yöntemler sağlar ve çıktının kabul edilebilir ses seviyeleri içinde kalmasını garanti eder.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `audio1` | AUDIO | gerekli | - | - | Birleştirilecek ilk ses girişi |
| `audio2` | AUDIO | gerekli | - | - | Birleştirilecek ikinci ses girişi |
| `merge_method` | COMBO | gerekli | - | ["add", "mean", "subtract", "multiply"] | Ses dalga formlarını birleştirmek için kullanılan yöntem. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Birleştirilmiş dalga formu ve örnekleme hızını içeren birleştirilmiş ses çıktısı |