# Bria Video Arka Planını Kaldır (Şeffaf)

Bu düğüm, Bria'nın AI servisini kullanarak bir videonun arka planını kaldırır ve kırpılmış kareleri bir alfa maskesiyle birlikte çıktı olarak verir. Her iki çıktıyı bir kompozit düğüme bağlayın veya saydam bir video yazmak için bunları bir Save WEBM düğümüne besleyin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | İşlenecek giriş videosu. Video 60 saniye veya daha kısa olmalıdır. | VIDEO | Evet | - |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; tohumdan bağımsız olarak sonuçlar deterministik değildir (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görseller` | Arka planı kaldırılmış video kareleri, 0.0 ila 1.0 aralığında RGB görüntüler olarak | IMAGE |
| `mask` | Video kareleri için alfa maskesi; Load Image kuralını izler, 1 saydam anlamına gelir | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/tr.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
