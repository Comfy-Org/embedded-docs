# Splat'ı Dönüştür

Transform Splat düğümü, bir gauss sıçramasına (gaussian splat) öteleme, döndürme ve ölçekleme dönüşümleri uygular. Tüm sıçramayı tek bir nesne olarak taşır, döndürür ve yeniden boyutlandırır; tek tip olmayan ölçekleme uygulandığında, doğru sonuçlar için her bir gauss sıçramasını da yeniden şekillendirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `splat` | Dönüştürülecek gauss sıçraması | SPLAT | Evet | - |
| `x_ekseni_taşı` | X ekseni boyunca öteleme (varsayılan: 0.0) | FLOAT | Evet | -100.0 ila 100.0 |
| `y_ekseni_taşı` | Y ekseni boyunca öteleme (varsayılan: 0.0) | FLOAT | Evet | -100.0 ila 100.0 |
| `z_ekseni_taşı` | Z ekseni boyunca öteleme (varsayılan: 0.0) | FLOAT | Evet | -100.0 ila 100.0 |
| `x_ekseni_döndür` | X ekseni etrafında derece cinsinden döndürme (varsayılan: 0.0) | FLOAT | Evet | -360.0 ila 360.0 |
| `y_ekseni_döndür` | Y ekseni etrafında derece cinsinden döndürme (varsayılan: 0.0) | FLOAT | Evet | -360.0 ila 360.0 |
| `z_ekseni_döndür` | Z ekseni etrafında derece cinsinden döndürme (varsayılan: 0.0) | FLOAT | Evet | -360.0 ila 360.0 |
| `x_ekseni_ölçek` | X ekseni boyunca ölçek faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.01 ila 100.0 |
| `y_ekseni_ölçek` | Y ekseni boyunca ölçek faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.01 ila 100.0 |
| `z_ekseni_ölçek` | Z ekseni boyunca ölçek faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.01 ila 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `splat` | Güncellenmiş konumlar, ölçekler ve döndürmelerle dönüştürülmüş gauss sıçraması | SPLAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TransformSplat/tr.md)

---
**Source fingerprint (SHA-256):** `19e6a7da7b4f0d8c9674ead2d35d742df460576b01c4ab4108dd59a2d08dfcb0`
