> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/tr.md)

Bu düğüm, Luma Görüntü Oluştur düğümüyle kullanılmak üzere bir görüntü ve ağırlık değeri tutar. Görüntü oluşturmayı etkilemek için diğer Luma düğümlerine aktarılabilen bir referans zinciri oluşturur. Düğüm, ya yeni bir referans zinciri başlatabilir ya da mevcut bir zincire ekleme yapabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Referans olarak kullanılacak görüntü. |
| `weight` | FLOAT | Evet | 0.0 - 1.0 | Görüntü referansının ağırlığı (varsayılan: 1.0). |
| `luma_ref` | LUMA_REF | Hayır | - | Eklenecek isteğe bağlı mevcut Luma referans zinciri. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `luma_ref` | LUMA_REF | Görüntüyü ve ağırlığı içeren Luma referans zinciri. |