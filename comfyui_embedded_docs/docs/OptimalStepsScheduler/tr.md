# OptimalAdımlarZamanlayıcı

OptimalStepsScheduler düğümü, difüzyon örneklemesi sırasında kullanılmak üzere bir gürültü çizelgesi (bir sigma değerleri dizisi) oluşturur. Seçilen model türünden temel gürültü seviyelerini seçer, gürültü giderme yalnızca kısmen uygulandığında çizelgeyi ayarlar ve döndürülen sigmaların istenen adım sayısıyla eşleşmesi için seviyeleri enterpolasyonla hesaplar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_type` | Gürültü seviyesi hesaplaması için kullanılacak difüzyon modeli türü. Her seçenek kendi önceden tanımlanmış gürültü seviyesi tablosunu kullanır. | COMBO | Evet | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | Hesaplanacak toplam örnekleme adımı sayısı (varsayılan: 20). | INT | Evet | 3 - 1000 |
| `denoise` | Gürültü giderme gücünü kontrol eder; bu güç, etkin adım sayısını ayarlar (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |

**Not:** Seçilen `model_type` için temel gürültü seviyesi tablosu, uzunluğu `steps + 1` değerine eşit olmadığında log-doğrusal enterpolasyonla yeniden örneklenir; böylece çıktı her zaman istenen adım sayısıyla eşleşir.

**Not:** `denoise` 1.0'den küçük olduğunda, düğüm `round(steps * denoise)` değerini toplam etkin adım sayısı olarak kullanır ve çizelgenin yalnızca eşleşen kuyruk kısmını tutar. `denoise` 0.0 veya daha düşükse, düğüm boş bir tensör döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Difüzyon örneklemesi için gürültü çizelgesini temsil eden sigma değerleri dizisi. Dizideki son değer her zaman 0 olarak ayarlanır. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
