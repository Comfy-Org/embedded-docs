# AdımlarınıHizalaZamanlayıcı

The AlignYourStepsScheduler düğümü, farklı difüzyon modeli türleri için gürültü giderme sürecinde kullanılan sigma değerlerini oluşturur. Seçilen model için temel gürültü seviyelerini belirler, `denoise` ayarına göre adım sayısını ayarlar ve 0 ile biten bir sigma tensörü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_type` | Temel gürültü seviyelerini seçmek için kullanılan model türü (varsayılan: "SD1") | COMBO | Evet | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | Oluşturulacak toplam örnekleme adımı sayısı (varsayılan: 10) | INT | Evet | 1 to 10000 |
| `denoise` | Örnekleme sürecinin ne kadarının kullanılacağını kontrol eder: 1.0 tüm adımları kullanır, daha düşük değerler daha az adım kullanır ve 0.0 boş bir sigma tensörü döndürür (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Gürültü giderme işlemi için hesaplanan sigma değerleri. `denoise` 0.0 ise boş bir tensör döndürülür. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
