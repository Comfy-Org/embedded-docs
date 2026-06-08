# Ideogram 4 Zamanlayıcı

Ideogram 4 Zamanlayıcı düğümü, Ideogram 4 referans programına dayalı olarak difüzyon örnekleme süreci için bir sigma değerleri (gürültü seviyeleri) dizisi oluşturur. Görüntü boyutlarına uyum sağlayan ve istatistiksel parametreler aracılığıyla ince ayar yapılmasına olanak tanıyan özel bir gürültü programı oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `adımlar` | Programın oluşturulacağı örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1 ila 200 |
| `genişlik` | Piksel cinsinden görüntü genişliği (varsayılan: 1024) | INT | Evet | 256 ila 8192 (adım: 16) |
| `yükseklik` | Piksel cinsinden görüntü yüksekliği (varsayılan: 1024) | INT | Evet | 256 ila 8192 (adım: 16) |
| `mu` | Logit-normal dağılımı için ortalama parametresi, merkezi gürültü seviyesini kontrol eder (varsayılan: 0.0) | FLOAT | Evet | -10.0 ila 10.0 (adım: 0.05) |
| `std` | Logit-normal dağılımı için standart sapma parametresi, gürültü seviyelerinin yayılımını kontrol eder (varsayılan: 1.75) | FLOAT | Evet | 0.1 ila 5.0 (adım: 0.05) |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `SIGMAS` | Gürültü programını temsil eden, uzunluğu `steps + 1`'e eşit olan sigma değerleri tensörü. Değerler yüksek gürültüden düşük gürültüye doğru azalır ve tam gürültü giderme için son değer 0.0 olarak ayarlanır. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/tr.md)

---
**Source fingerprint (SHA-256):** `408ea680158500690e28e300098a5c4fd13eb1a2c96c3d95db06244151116f22`
