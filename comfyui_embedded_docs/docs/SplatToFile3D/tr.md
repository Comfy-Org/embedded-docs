# SplatToFile3D Düğüm Belgelendirmesi

## Genel Bakış

SplatToFile3D düğümü, bir gauss sıçramasını (gaussian splat), Kaydet veya Önizleme 3D düğümleriyle kullanılabilen bir File3D nesnesine dönüştürür. Yalnızca parti başına bir öğeyi destekler ve dışa aktarılan 3D verileri için farklı çıktı dosya biçimleri arasından seçim yapmanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `splat` | Dosyaya serileştirilecek gauss sıçraması verisi | SPLAT | Evet | - |
| `format` | 3D dosyası için çıktı dosya biçimi. ply: tam küresel harmoniklerle standart 3D Gauss Sıçraması. ksplat: mkkellogg SplatBuffer (seviye 0, sıkıştırılmamış), yalnızca temel renk. spz: Niantic gzip sıkıştırmalı (~10 kat daha küçük), yalnızca temel renk (varsayılan: "ply") | COMBO | Evet | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model_3d` | Seçilen biçimde serileştirilmiş gauss sıçraması verilerini içeren, kaydetme veya önizleme için hazır bir File3D nesnesi | FILE3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/tr.md)

---
**Source fingerprint (SHA-256):** `c04fe04faa8ce81ad699e67c00d047550b0cadbfd037b687331f76944501a9f6`
