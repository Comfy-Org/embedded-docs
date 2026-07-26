# Video-Metin Çiftlerini Karıştır

Bu düğüm, video-metin çiftlerinin sırasını rastgele karıştırır ve her videonun kendi metniyle eşleşmiş kalmasını sağlar. Eşit uzunlukta iki liste alır ve aynı rastgele permütasyonu her ikisine de uygulayarak, karıştırma işleminden sonra orijinal eşleşmelerin korunmasını garantiler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `videos` | Karıştırılacak videoların listesi. | VIDEO | Evet | List of video items |
| `texts` | Karıştırılacak metinlerin listesi. | STRING | Evet | List of text strings |
| `seed` | Karıştırma sırasını kontrol eden rastgele tohum (varsayılan: 0). | INT | Evet | 0 to 18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `videos` | Yeni rastgele sıradaki karıştırılmış videolar. | VIDEO |
| `texts` | Videolarla aynı yeni sıradaki karıştırılmış metinler. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/tr.md)

---
**Source fingerprint (SHA-256):** `33b763a6d48ca1036d5267139f90eadb3b2080a02fa57ce5bcae6087a077efa1`
