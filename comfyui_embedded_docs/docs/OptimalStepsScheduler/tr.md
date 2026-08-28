# OptimalAdımlarZamanlayıcı

OptimalStepsScheduler düğümü, difüzyon örneklemesi sırasında kullanılmak üzere bir gürültü takvimi (bir sigma değerleri dizisi) oluşturur. Temel gürültü seviyelerini seçilen model türünden alır, denoising kısmen uygulandığında takvimi ayarlar ve döndürülen sigmaların istenen adım sayısıyla eşleşmesi için seviyeleri enterpolasyon yapar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_türü` | Gürültü seviyesi hesaplaması için kullanılacak difüzyon modelinin türü. | COMBO | Evet | "FLUX"<br>"Wan"<br>"Chroma" |
| `adımlar` | Hesaplanacak toplam örnekleme adımı sayısı (varsayılan: 20). | INT | Evet | 3 ile 1000 |
| `gürültü_azaltma` | Denoising gücünü kontrol eder, efektif adım sayısını ayarlar (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |

**Not:** `denoise` değeri 1.0'dan küçük olduğunda, düğüm toplam efektif adım sayısı olarak `round(steps * denoise)` kullanır. `denoise` 0.0 ise, düğüm boş bir tensör döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Difüzyon örneklemesi için gürültü takvimini temsil eden sigma değerleri dizisi. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
