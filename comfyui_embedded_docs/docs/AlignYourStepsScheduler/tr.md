# AdımlarınıHizalaZamanlayıcı

AlignYourStepsScheduler düğümü, farklı model türlerine dayalı olarak gürültü giderme işlemi için sigma değerleri üretir. Örnekleme sürecinin her adımı için uygun gürültü seviyelerini hesaplar ve `denoise` parametresine göre toplam adım sayısını ayarlar. Bu, örnekleme adımlarının farklı difüzyon modellerinin belirli gereksinimleriyle uyumlu hale getirilmesine yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_türü` | Sigma hesaplaması için kullanılacak model türünü belirtir (varsayılan: "SD1") | COMBO | Evet | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `adımlar` | Oluşturulacak toplam örnekleme adım sayısı (varsayılan: 10) | INT | Evet | 1-10000 |
| `gürültü_azaltma` | Görüntünün ne kadar gürültü giderileceğini kontrol eder; 1.0 tüm adımları kullanır, daha düşük değerler daha az adım kullanır (varsayılan: 1.0) | FLOAT | Evet | 0.0-1.0 |

Not: Her model türü, 10 adım için 11 sigma değeri içeren yerleşik bir gürültü seviyesi çizelgesine sahiptir. `denoise` 0.0 olduğunda düğüm boş bir sigma tensörü döndürür. `denoise` 0.0 ile 1.0 arasında olduğunda, etkili adım sayısı `round(steps × denoise)` olarak hesaplanır ve sigma çizelgesinin yalnızca buna karşılık gelen son kısmı kullanılır. İstenen `steps` değeri yerleşik çizelge uzunluğuyla eşleşmezse, gürültü seviyeleri istenen adım sayısıyla eşleşecek şekilde log-doğrusal olarak enterpolasyon yapılır. Son sigma değeri her zaman 0 olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Gürültü giderme işlemi için hesaplanan sigma değerlerini döndürür | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
