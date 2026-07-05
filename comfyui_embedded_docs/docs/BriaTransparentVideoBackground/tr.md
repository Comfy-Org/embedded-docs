# Bria Video Arka Planını Kaldır (Şeffaf)

Bu düğüm, Bria'nın yapay zeka hizmetini kullanarak bir videonun arka planını kaldırır ve kesilmiş kareleri bir alfa maskesiyle birlikte çıktı olarak verir. Her iki çıktıyı bir birleştirme düğümüne bağlayın veya saydam bir video yazmak için bir WEBM Kaydet düğümüne besleyin.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `video` | İşlenecek giriş videosu | VIDEO | Evet | - |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `görseller` | Arka planı kaldırılmış video kareleri | IMAGE |
| `mask` | Video kareleri için alfa maskesi | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/tr.md)

---
**Source fingerprint (SHA-256):** `45fb3fc185b5c6420d6ac2b87f2403566e1ef6dcdc57791fb833b6ccb2a64cd9`
