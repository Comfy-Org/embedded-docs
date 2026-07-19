# Stability AI Büyütme Yaratıcı

Görseli minimum değişiklikle 4K çözünürlüğe yükseltir. Bu düğüm, Stability AI'nin yaratıcı yükseltme teknolojisini kullanarak, orijinal içeriği korurken ve ince yaratıcı detaylar ekleyerek görüntü çözünürlüğünü artırır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Yükseltilecek giriş görseli | IMAGE | Evet | - |
| `istem` | Çıktı görselinde görmek istediğiniz şey. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, betimleyici bir istem daha iyi sonuçlara yol açacaktır. (varsayılan: boş dize) | STRING | Evet | - |
| `yaratıcılık` | Başlangıç görseli tarafından güçlü bir şekilde koşullandırılmamış ek detaylar oluşturma olasılığını kontrol eder. (varsayılan: 0.3) | FLOAT | Evet | 0.1-0.5 |
| `stil_önayarı` | Oluşturulan görsel için isteğe bağlı istenen stil. (varsayılan: "None") | STRING | Evet | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) | INT | Evet | 0-4294967294 |
| `negatif_istem` | Çıktı görselinde görmek istemediğiniz şeylerin anahtar kelimeleri. Bu gelişmiş bir özelliktir. (varsayılan: boş dize) | STRING | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | 4K çözünürlükte yükseltilmiş görsel | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/tr.md)

---
**Source fingerprint (SHA-256):** `46f7bdd3cb4254b6305407f43e4a9a69a54fd3a0ac285d784c899dbf52edd552`
