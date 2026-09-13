# AdımlarınıHizalaZamanlayıcı

AlignYourStepsScheduler düğümü, farklı model türlerine göre gürültü giderme işlemi için sigma değerleri (gürültü seviyeleri) üretir. Örnekleme sürecinin her adımı için uygun gürültü seviyelerini hesaplar ve toplam adım sayısını `denoise` parametresine göre ayarlar; böylece örnekleme adımlarının farklı difüzyon modellerinin özel gereksinimleriyle uyumlu hale getirilmesine yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_type` | Sigma hesaplaması için kullanılacak model türünü belirtir (varsayılan: "SD1") | COMBO | Evet | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | Üretilecek toplam örnekleme adımı sayısı (varsayılan: 10) | INT | Evet | 1 ile 10000 |
| `denoise` | Görüntüde ne kadar gürültü giderme yapılacağını kontrol eder; 1.0 tüm adımları kullanır ve daha düşük değerler daha az adım kullanır (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (adım: 0.01) |

Not: Her model türünün, 10 adım için 11 sigma değeri içeren yerleşik bir gürültü seviyesi çizelgesi vardır. `denoise` 0.0 olduğunda düğüm boş bir sigma tensörü döndürür. `denoise` 0.0 ile 1.0 arasında olduğunda, etkin adım sayısı `round(steps × denoise)` olarak hesaplanır ve sigma çizelgesinin yalnızca karşılık gelen son kısmı kullanılır. İstenen `steps` değeri yerleşik çizelge uzunluğuyla eşleşmiyorsa, gürültü seviyeleri istenen adım sayısına uyacak şekilde log-doğrusal enterpolasyon uygulanarak hesaplanır. Son sigma değeri her zaman 0 olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Gürültü giderme işlemi için hesaplanan sigma değerlerini döndürür | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
