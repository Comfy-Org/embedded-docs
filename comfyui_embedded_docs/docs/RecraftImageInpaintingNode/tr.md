# Recraft Görüntü İç Boyama

Bu düğüm, bir metin istemi ve maske kullanarak görüntünün belirli alanlarını değiştirir. Recraft API'sini kullanarak yalnızca maskelenmiş bölgeleri akıllıca düzenlerken, görüntünün geri kalanını değiştirmeden bırakır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Değiştirilecek giriş görüntüsü | IMAGE | Evet | - |
| `maske` | Görüntünün hangi alanlarının değiştirileceğini tanımlayan maske | MASK | Evet | - |
| `istem` | Görüntü oluşturma için istem (varsayılan: boş dize, maksimum uzunluk: 1000 karakter) | STRING | Evet | - |
| `n` | Oluşturulacak görüntü sayısı (varsayılan: 1, minimum: 1, maksimum: 6) | INT | Evet | 1-6 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Recraft API'si için isteğe bağlı stil parametresi. Sağlanmazsa, varsayılan olarak "realistic_image" stili kullanılır | STYLEV3 | Hayır | - |
| `negatif_istem` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) | STRING | Hayır | - |

*Not: `image` ve `mask` parametrelerinin iç boyama işleminin çalışması için birlikte sağlanması gerekir. Maske, görüntü boyutlarına uyacak şekilde otomatik olarak yeniden boyutlandırılır. `prompt` doğrulanır ve maksimum 1000 karakter uzunluğundadır.*

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | İstem ve maskeye göre oluşturulan değiştirilmiş görüntü(ler). Giriş görüntüsü başına `n` parametresiyle çarpılmış sayıda görüntü döndürür | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/tr.md)

---
**Source fingerprint (SHA-256):** `3eb6505a19173d8e4ea4216348f9592fd996cdfe2f07a9e79ccec5f738a8fb93`
