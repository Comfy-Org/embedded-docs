> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/tr.md)

Bu düğüm, LTXV ses modeli için özelleştirilmiş bir metin kodlayıcı yükler. Belirli bir metin kodlayıcı dosyasını bir kontrol noktası dosyasıyla birleştirerek, sesle ilgili metin koşullandırma görevleri için kullanılabilecek bir CLIP modeli oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `text_encoder` | STRING | Evet | Birden fazla seçenek mevcut | Yüklenecek LTXV metin kodlayıcı modelinin dosya adı. Mevcut seçenekler `text_encoders` klasöründen yüklenir. |
| `ckpt_name` | STRING | Evet | Birden fazla seçenek mevcut | Yüklenecek kontrol noktasının dosya adı. Mevcut seçenekler `checkpoints` klasöründen yüklenir. |
| `device` | STRING | Hayır | `"default"`<br>`"cpu"` | Modelin yükleneceği cihazı belirtir. CPU'ya zorla yüklemek için `"cpu"` kullanın. Varsayılan davranış (`"default"`), sistemin otomatik cihaz yerleştirmesini kullanır. |

**Not:** `text_encoder` ve `ckpt_name` parametreleri birlikte çalışır. Düğüm, tek bir işlevsel CLIP modeli oluşturmak için belirtilen her iki dosyayı da yükler. Dosyalar LTXV mimarisiyle uyumlu olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `clip` | CLIP | Yüklenen LTXV CLIP modeli, ses üretimi için metin istemlerini kodlamak üzere kullanıma hazır. |
