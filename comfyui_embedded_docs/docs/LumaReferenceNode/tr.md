> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/tr.md)

Bu düğüm, Luma Görüntü Oluştur düğümüyle kullanılmak üzere bir görüntü ve ağırlık değeri tutar. Görüntü oluşturmayı etkilemek için diğer Luma düğümlerine aktarılabilen bir referans zinciri oluşturur. Düğüm, ya yeni bir referans zinciri başlatabilir ya da mevcut bir zincire ekleme yapabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `görüntü` | IMAGE | Evet | - | Referans olarak kullanılacak görüntü. |
| `ağırlık` | FLOAT | Evet | 0.0 - 1.0 | Görüntü referansının ağırlığı (varsayılan: 1.0). |
| `luma_referansı` | LUMA_REF | Hayır | - | Eklenecek isteğe bağlı mevcut Luma referans zinciri. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `luma_referansı` | LUMA_REF | Görüntü ve ağırlığı içeren Luma referans zinciri. |

---
**Source fingerprint (SHA-256):** `1ad653f0ad7c56702f607ebc3c3d117196295e4e3b044a2c6f1aa3db18869a40`
