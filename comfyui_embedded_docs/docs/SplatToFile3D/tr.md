# 3D Dosya Oluştur (Splat'tan)

SplatToFile3D düğümü, bir gaussyen splat'ı, Save veya Preview 3D düğümleriyle kullanılabilen bir File3D nesnesine dönüştürür. Yalnızca batch başına bir öğeyi destekler ve dışa aktarılan 3D verileri için farklı çıktı dosya biçimleri arasından seçim yapmanızı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `splat` | Dosyaya serileştirilecek gaussyen splat verisi | SPLAT | Evet | - |
| `format` | 3D dosyası için çıktı dosya biçimi. ply: tam küresel harmoniklerle standart 3D Gaussyen Splat. ksplat: mkkellogg SplatBuffer (seviye 0, sıkıştırılmamış), yalnızca temel renk. spz: Niantic gzip sıkıştırmalı (~10 kat daha küçük), yalnızca temel renk (varsayılan: "ply") | COMBO | Evet | "ply"<br>"ksplat"<br>"spz" |

Not: Bu düğüm yalnızca batch başına bir öğeyi destekler. Girdi splat'ı batch içinde birden fazla öğe içeriyorsa, düğüm bir uyarı kaydeder ve ilk öğeyi kullanır. Desteklenmeyen bir biçim sağlanırsa, düğüm bir hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Seçilen biçimde serileştirilmiş gaussyen splat verilerini içeren, kaydetmeye veya önizlemeye hazır bir File3D nesnesi | FILE3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/tr.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
