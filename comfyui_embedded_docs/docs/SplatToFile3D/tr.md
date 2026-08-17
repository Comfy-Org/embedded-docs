# 3D Dosya Oluştur (Splat'tan)

SplatToFile3D, bir gaussian splat'ı Save veya Preview 3D düğümleriyle kullanılabilen bir File3D nesnesine dönüştürür. Çıktı dosya formatını seçebilirsiniz. Düğüm, parti başına yalnızca bir öğeyi destekler; birden fazla öğe alırsa, ilkini kullanır ve günlüğe bir uyarı kaydeder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `splat` | Dosyaya serileştirilecek gaussian splat verisi. Parti başına yalnızca bir öğe desteklenir. Birden fazla öğe sağlanırsa, yalnızca ilki kullanılır. | SPLAT | Evet | - |
| `format` | 3D dosyası için çıktı dosya formatı. ply: tam küresel harmonikli standart 3D Gaussian Splat. ksplat: mkkellogg SplatBuffer (seviye 0, sıkıştırılmamış), yalnızca temel renk. spz: Niantic gzip ile sıkıştırılmış (~10 kat daha küçük), yalnızca temel renk (varsayılan: "ply") | COMBO | Evet | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Seçilen formatta serileştirilmiş gaussian splat verisi içeren, kaydetmeye veya önizlemeye hazır bir File3D nesnesi | FILE3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/tr.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
