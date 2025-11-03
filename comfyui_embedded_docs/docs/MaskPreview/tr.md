> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/tr.md)

MaskPreview düğümü, bir maskeyi 3 kanallı görüntü formatına dönüştürerek ve geçici bir dosya olarak kaydederek görsel bir önizlemesini oluşturur. Bir maske girdisi alır ve görüntü görüntüleme için uygun bir formata yeniden şekillendirir, ardından sonucu rastgele bir dosya adı öneki ile geçici dizine kaydeder. Bu, kullanıcıların iş akışı yürütülürken maske verilerini görsel olarak incelemesine olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `maske` | MASK | Evet | - | Önizlenecek ve görüntü formatına dönüştürülecek maske verisi |
| `filename_prefix` | STRING | Hayır | - | Çıktı dosya adı için önek (varsayılan: "ComfyUI") |
| `prompt` | PROMPT | Hayır | - | Meta veriler için istem bilgisi (otomatik olarak sağlanır) |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Meta veriler için ek PNG bilgisi (otomatik olarak sağlanır) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ui` | DICT | Görüntüleme için önizleme görüntüsü bilgisini ve meta verileri içerir |