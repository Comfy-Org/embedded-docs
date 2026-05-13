> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreativeUpscaleNode/tr.md)

Recraft Creative Upscale Image düğümü, bir raster görüntüyü çözünürlüğünü artırarak iyileştirir. Görüntüdeki küçük detayları ve yüzleri iyileştirmeye odaklanan "yaratıcı büyütme" sürecini kullanır. Bu işlem, harici bir API aracılığıyla eşzamanlı olarak gerçekleştirilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | | Büyütülecek giriş görüntüsü. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | İyileştirilmiş detaylarla birlikte elde edilen büyütülmüş görüntü. |

---
**Source fingerprint (SHA-256):** `b638dd926e144c47ad2c2968cf49f3d322cbdddfcb8b2e86edb3ae9558a1ded6`
