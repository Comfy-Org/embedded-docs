Bu düğüm, LTXV ses modeli için özel bir metin kodlayıcı yükler. Belirli bir metin kodlayıcı dosyasını bir kontrol noktası dosyasıyla birleştirerek, sesle ilgili metin koşullandırma görevleri için kullanılabilecek bir CLIP modeli oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `text_encoder` | Yüklenecek LTXV metin kodlayıcı modelinin dosya adı. Mevcut seçenekler `text_encoders` klasöründen yüklenir. | STRING | Evet | Birden çok seçenek mevcut |
| `ckpt_name` | Yüklenecek kontrol noktasının dosya adı. Mevcut seçenekler `checkpoints` klasöründen yüklenir. | STRING | Evet | Birden çok seçenek mevcut |
| `device` | Modelin yükleneceği cihazı belirtir. CPU'ya yüklemeye zorlamak için `"cpu"` kullanın. Varsayılan davranış (`"default"`), sistemin otomatik cihaz yerleşimini kullanır. | STRING | Hayır | `"default"`<br>`"cpu"` |

**Not:** `text_encoder` ve `ckpt_name` parametreleri birlikte çalışır. Düğüm, tek ve işlevsel bir CLIP modeli oluşturmak için belirtilen her iki dosyayı da yükler. Dosyalar LTXV mimarisiyle uyumlu olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip` | Ses üretimi için metin istemlerini kodlamak amacıyla kullanıma hazır, yüklenmiş LTXV CLIP modeli. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/tr.md)

---
**Source fingerprint (SHA-256):** `c072a0b3393aa44333bb15ae42179c50868a4e9d7ca706d6c7da5922625373e6`
