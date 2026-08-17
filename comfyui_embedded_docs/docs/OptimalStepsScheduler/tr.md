# OptimalAdımlarZamanlayıcı

OptimalStepsScheduler düğümü, seçilen model türüne ve adım yapılandırmasına göre difüzyon modelleri için gürültü planı sigmalarını hesaplar. Denoise parametresine göre toplam adım sayısını ayarlar ve istenen adım sayısına uyacak şekilde gürültü seviyelerini enterpole eder. Düğüm, difüzyon örnekleme sürecinde kullanılan gürültü seviyelerini belirleyen bir dizi sigma değeri döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_type` | Gürültü seviyesi hesaplaması için kullanılacak difüzyon modelinin türü | COMBO | Evet | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | Hesaplanacak toplam örnekleme adımı sayısı (varsayılan: 20) | INT | Evet | 3-1000 |
| `denoise` | Gürültü giderme gücünü kontrol eder, bu da etkin adım sayısını ayarlar (varsayılan: 1.0) | FLOAT | Evet | 0.0-1.0 |

**Not:** `denoise` 1.0'dan düşük ayarlandığında, düğüm etkin adımları `steps * denoise` olarak hesaplar. `denoise` 0.0 olarak ayarlanırsa, düğüm boş bir tensör döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Difüzyon örnekleme için gürültü planını temsil eden bir dizi sigma değeri | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
