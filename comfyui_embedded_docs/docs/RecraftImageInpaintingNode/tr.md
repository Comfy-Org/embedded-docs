# Recraft Görüntü İç Boyama

Bu düğüm, bir metin istemi ve bir maske temelinde görüntünün belirli alanlarını değiştirir. Recraft API'yi kullanarak yalnızca maskelenmiş bölgeleri akıllıca düzenler ve görüntünün geri kalanını değiştirmeden korur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Değiştirilecek giriş görüntüsü | IMAGE | Evet | - |
| `mask` | Görüntünün hangi alanlarının değiştirileceğini tanımlayan maske | MASK | Evet | - |
| `prompt` | Görüntü üretimi için istem (varsayılan: boş dize, maksimum uzunluk: 1000 karakter) | STRING | Evet | - |
| `n` | Üretilecek görüntü sayısı (varsayılan: 1, minimum: 1, maksimum: 6) | INT | Evet | 1-6 |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_style` | Recraft API için isteğe bağlı stil parametresi. Sağlanmazsa, varsayılan olarak "realistic_image" stili kullanılır | STYLEV3 | Hayır | - |
| `negative_prompt` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) | STRING | Hayır | - |

*Not: `image` ve `mask` onarım (inpainting) işleminin çalışması için birlikte sağlanmalıdır. Maske, görüntü boyutlarına uyacak şekilde otomatik olarak yeniden boyutlandırılır. `prompt` doğrulanır ve maksimum uzunluğu 1000 karakterdir. Infinite Style Library'den bir `style_id` kullanılıyorsa, bunun bir Vektör sanat stili olmadığından emin olun; aksi takdirde API, görüntü yerine SVG verisi döndürebilir.*

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | İstem ve maske temelinde üretilen değiştirilmiş görüntü(ler). Girdi görüntüsü başına, `n` parametresiyle çarpılarak bir görüntü döndürür | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/tr.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`
