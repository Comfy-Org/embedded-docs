> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/tr.md)

Görseli minimum değişiklikle 4K çözünürlüğe yükseltir. Bu düğüm, Stability AI'nin yaratıcı yükseltme teknolojisini kullanarak, orijinal içeriği korurken ve ince yaratıcı detaylar ekleyerek görüntü çözünürlüğünü artırır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Yükseltilecek giriş görseli |
| `istem` | STRING | Evet | - | Çıktı görselinde görmek istediğiniz şey. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, betimleyici bir istem daha iyi sonuçlara yol açacaktır. (varsayılan: boş dize) |
| `yaratıcılık` | FLOAT | Evet | 0.1-0.5 | Başlangıç görseli tarafından güçlü bir şekilde koşullandırılmamış ek detaylar oluşturma olasılığını kontrol eder. (varsayılan: 0.3) |
| `stil_önayarı` | STRING | Evet | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` | Oluşturulan görsel için isteğe bağlı istenen stil. (varsayılan: "None") |
| `tohum` | INT | Evet | 0-4294967294 | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) |
| `negatif_istem` | STRING | Hayır | - | Çıktı görselinde görmek istemediğiniz şeylerin anahtar kelimeleri. Bu gelişmiş bir özelliktir. (varsayılan: boş dize) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | 4K çözünürlükte yükseltilmiş görsel |

---
**Source fingerprint (SHA-256):** `46f7bdd3cb4254b6305407f43e4a9a69a54fd3a0ac285d784c899dbf52edd552`
