# Kontrastı Ayarla

Adjust Contrast düğümü, bir girdi görüntüsünün kontrast düzeyini değiştirir. Görüntünün açık ve koyu alanları arasındaki farkı ayarlayarak çalışır. 1.0 faktörü görüntüyü değiştirmez, 1.0'ın altındaki değerler kontrastı azaltır ve 1.0'ın üzerindeki değerler artırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Kontrastı ayarlanacak girdi görüntüsü. | IMAGE | Evet | - |
| `factor` | Kontrast faktörü. 1.0 = değişiklik yok, <1.0 = daha az kontrast, >1.0 = daha fazla kontrast. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 2.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Kontrastı ayarlanmış sonuç görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/tr.md)

---
**Source fingerprint (SHA-256):** `1f5fbd0f0b739492bc171d3c43ea2150a3ca76dc3ede9bf63cb97c45a90b9e44`
