> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/tr.md)

OptimalStepsScheduler düğümü, seçilen model türüne ve adım yapılandırmasına bağlı olarak difüzyon modelleri için gürültü planı sigma değerlerini hesaplar. Toplam adım sayısını `denoise` parametresine göre ayarlar ve istenen adım sayısına uyacak şekilde gürültü seviyelerini enterpole eder. Düğüm, difüzyon örnekleme sürecinde kullanılan gürültü seviyelerini belirleyen bir sigma değerleri dizisi döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_türü` | COMBO | Evet | "FLUX"<br>"Wan"<br>"Chroma" | Gürültü seviyesi hesaplaması için kullanılacak difüzyon modelinin türü |
| `adımlar` | INT | Evet | 3-1000 | Hesaplanacak toplam örnekleme adımı sayısı (varsayılan: 20) |
| `gürültü_azaltma` | FLOAT | Hayır | 0.0-1.0 | Gürültü giderme gücünü kontrol eder, etkin adım sayısını ayarlar (varsayılan: 1.0) |

**Not:** `denoise` değeri 1.0'dan küçük ayarlandığında, düğüm etkin adımları `steps * denoise` olarak hesaplar. `denoise` değeri 0.0 olarak ayarlanırsa, düğüm boş bir tensör döndürür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Difüzyon örneklemesi için gürültü planını temsil eden bir sigma değerleri dizisi |

---
**Source fingerprint (SHA-256):** `4379171dc6d525a1ece514fdd11a95bfd92ed0c8b301f69ca718c1a3256b9590`
