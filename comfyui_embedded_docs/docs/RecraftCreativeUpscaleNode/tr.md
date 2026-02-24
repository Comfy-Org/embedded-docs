> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreativeUpscaleNode/tr.md)

Recraft Creative Upscale Image düğümü, bir tarama görüntüsünün çözünürlüğünü artırarak geliştirir. Görüntü içindeki küçük detaylara ve yüzlere odaklanan bir "yaratıcı yükseltme" işlemi kullanır. Bu işlem, harici bir API üzerinden eşzamanlı olarak gerçekleştirilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | | Yükseltilecek girdi görüntüsü. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | Geliştirilmiş detaylara sahip, yükseltilmiş sonuç görüntüsü. |
