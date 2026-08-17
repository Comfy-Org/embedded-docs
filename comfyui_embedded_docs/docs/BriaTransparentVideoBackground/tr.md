# Bria Video Arka Planını Kaldır (Şeffaf)

Bu düğüm, Bria'nın yapay zeka servisini kullanarak bir videonun arka planını kaldırır ve kesilmiş kareleri bir alfa maskesiyle birlikte döndürür. Her iki çıktıyı bir birleştirme düğümüne bağlayın veya şeffaf bir video yazmak için bir Save WEBM düğümüne besleyin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | İşlenecek giriş videosu. Maksimum süre 60 saniyedir. | VIDEO | Evet | - |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0 to 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Arka planı kaldırılmış video kareleri | IMAGE |
| `mask` | Video kareleri için alfa maskesi; 1, şeffaf anlamına gelir | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/tr.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
