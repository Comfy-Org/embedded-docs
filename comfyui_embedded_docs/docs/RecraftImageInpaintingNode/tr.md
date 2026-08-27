# Recraft Görüntü İç Boyama

Bu düğüm, bir metin istemine ve maskeye dayalı olarak görüntünün belirli bölgelerini değiştirir. Recraft API'sini kullanarak yalnızca maskelenmiş bölgeleri akıllıca düzenler ve görüntünün geri kalanını değiştirmeden korur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Değiştirilecek giriş görüntüsü | IMAGE | Evet | - |
| `maske` | Görüntünün hangi bölümlerinin değiştirileceğini tanımlayan maske | MASK | Evet | - |
| `istem` | Görüntü üretimi için istem (varsayılan: boş dize, maksimum uzunluk: 1000 karakter) | STRING | Evet | - |
| `n` | Oluşturulacak görüntü sayısı (varsayılan: 1, minimum: 1, maksimum: 6) | INT | Evet | 1-6 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak belirlenemezdir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Recraft API'si için isteğe bağlı stil parametresi. Sağlanmazsa "realistic_image" stilini varsayılan alır | STYLEV3 | Hayır | - |
| `negatif_istem` | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) | STRING | Hayır | - |

*Not: `image` ve `mask` birlikte sağlanmalıdır; aksi takdirde inpainting işlemi çalışmaz. Maske, görüntü boyutlarıyla eşleşecek şekilde otomatik olarak yeniden boyutlandırılır. `prompt` doğrulanır ve maksimum uzunluğu 1000 karakterdir. Sonsuz Stil Kütüphanesi'nden bir `style_id` kullanılıyorsa, bunun Vektör sanat stili olmadığından emin olun; aksi takdirde API, görüntü yerine SVG verisi döndürebilir.*

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | İstem ve maskeye dayalı olarak oluşturulan değiştirilmiş görüntü(ler). Her bir giriş görüntüsü için `n` parametresi ile çarpılan sayıda görüntü döndürür | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/tr.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`
