# File3DToSplat

Bu düğüm, gaussian splat verisi içeren bir 3D dosyayı, düğüm grafiğinde kullanılabilecek gaussian splat formatına dönüştürür. PLY, SPLAT, KSPLAT ve SPZ dosya formatlarını destekler; dosya formatı, dosya içeriğinden otomatik olarak algılanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `model_3d` | Bir gaussian splat 3D dosyası | FILE3D | Evet | - |

Giriş dosyası, desteklenen formatlardan birinde olmalıdır: PLY, SPLAT, KSPLAT veya SPZ. PLY dosyaları tam küresel harmonik verileri taşırken, diğer formatlar yalnızca temel renk bilgisi içerir. Format, dosya içeriğinden otomatik olarak algılanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `splat` | Konum, ölçek, dönüş, opaklık ve küresel harmonik verileri içeren bir gaussian splat | SPLAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/File3DToSplat/tr.md)

---
**Source fingerprint (SHA-256):** `9f45210a1366e57a91de6e1251f0e2e09f39e6498dbec1db7bf9826ebedd167b`
