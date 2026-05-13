> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/tr.md)

Kontrast Ayarla düğümü, bir giriş görüntüsünün kontrast seviyesini değiştirir. Görüntünün açık ve koyu alanları arasındaki farkı ayarlayarak çalışır. 1,0 faktörü görüntüyü değiştirmez, 1,0'ın altındaki değerler kontrastı azaltır ve 1,0'ın üzerindeki değerler kontrastı artırır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Kontrastı ayarlanacak giriş görüntüsü. |
| `factor` | FLOAT | Hayır | 0,0 - 2,0 | Kontrast faktörü. 1,0 = değişiklik yok, <1,0 = daha az kontrast, >1,0 = daha fazla kontrast. (varsayılan: 1,0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Kontrastı ayarlanmış sonuç görüntüsü. |

---
**Source fingerprint (SHA-256):** `01148cdd9d951e78c712c1c3159c5562a680a5147bd4a76e33d91543d5245854`
