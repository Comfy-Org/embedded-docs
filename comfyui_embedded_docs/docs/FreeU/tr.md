> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/tr.md)

FreeU düğümü, görüntü oluşturma kalitesini artırmak için bir modelin çıktı bloklarına frekans alanı değişiklikleri uygular. Farklı kanal gruplarını ölçeklendirerek ve belirli özellik haritalarına Fourier filtrelemesi uygulayarak çalışır, bu da oluşturma süreci sırasında modelin davranışı üzerinde hassas kontrole olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | FreeU değişikliklerinin uygulanacağı model |
| `b1` | FLOAT | Evet | 0.0 - 10.0 | model_channels × 4 özellikleri için omurga ölçeklendirme faktörü (varsayılan: 1.1) |
| `b2` | FLOAT | Evet | 0.0 - 10.0 | model_channels × 2 özellikleri için omurga ölçeklendirme faktörü (varsayılan: 1.2) |
| `s1` | FLOAT | Evet | 0.0 - 10.0 | model_channels × 4 özellikleri için atlama bağlantısı ölçeklendirme faktörü (varsayılan: 0.9) |
| `s2` | FLOAT | Evet | 0.0 - 10.0 | model_channels × 2 özellikleri için atlama bağlantısı ölçeklendirme faktörü (varsayılan: 0.2) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | FreeU yamaları uygulanmış değiştirilmiş model |