> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/tr.md)

**## Genel Bakış**

Get Video Components düğümü, bir video dosyasından tüm ana bileşenleri çıkarır. Videoyu tek tek karelere ayırır, ses parçasını çıkarır ve video kare hızı bilgisini sağlar. Bu, her bir bileşen üzerinde bağımsız olarak çalışarak ileri işleme veya analiz yapmanıza olanak tanır.

## ## Girdiler

| Parametre | Veri Tipi | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Bileşenlerin çıkarılacağı video. |

## ## Çıktılar

| Çıktı Adı | Veri Tipi | Açıklama |
|-------------|-----------|-------------|
| `images` | IMAGE | Videodan çıkarılan, ayrı görüntüler halindeki tek tek kareler. |
| `audio` | AUDIO | Videodan çıkarılan ses parçası. |
| `fps` | FLOAT | Videonun saniyedeki kare sayısı (FPS) cinsinden kare hızı. |