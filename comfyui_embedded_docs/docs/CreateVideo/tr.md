> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/tr.md)

Video Oluştur düğümü, bir görüntü dizisinden video dosyası oluşturur. Videoyu saniyedeki kare sayısını belirterek oynatabilir ve isteğe bağlı olarak video ses ekleyebilirsiniz. Düğüm, görüntülerinizi belirtilen kare hızında oynatılabilen bir video formatında birleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntüler` | IMAGE | Evet | - | Videoyu oluşturmak için kullanılacak görüntüler. |
| `fps` | FLOAT | Evet | 1.0 - 120.0 | Video oynatım hızı için saniyedeki kare sayısı (varsayılan: 30.0). |
| `ses` | AUDIO | Hayır | - | Videoya eklenecek ses. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Girdi görüntülerini ve isteğe bağlı sesi içeren oluşturulmuş video dosyası. |