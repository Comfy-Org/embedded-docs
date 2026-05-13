> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/tr.md)

Bu düğüm, bir metin istemi ve maske kullanarak görüntünün belirli alanlarını değiştirir. Recraft API'sini kullanarak yalnızca maskelenmiş bölgeleri akıllıca düzenlerken, görüntünün geri kalanını değiştirmeden bırakır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Değiştirilecek giriş görüntüsü |
| `mask` | MASK | Evet | - | Görüntünün hangi alanlarının değiştirileceğini tanımlayan maske |
| `prompt` | STRING | Evet | - | Görüntü oluşturma için istem (varsayılan: boş dize, maksimum uzunluk: 1000 karakter) |
| `n` | INT | Evet | 1-6 | Oluşturulacak görüntü sayısı (varsayılan: 1, minimum: 1, maksimum: 6) |
| `seed` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) |
| `recraft_style` | STYLEV3 | Hayır | - | Recraft API'si için isteğe bağlı stil parametresi. Sağlanmazsa, varsayılan olarak "realistic_image" stili kullanılır |
| `negative_prompt` | STRING | Hayır | - | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) |

*Not: `image` ve `mask` parametrelerinin iç boyama işleminin çalışması için birlikte sağlanması gerekir. Maske, görüntü boyutlarına uyacak şekilde otomatik olarak yeniden boyutlandırılır. `prompt` doğrulanır ve maksimum 1000 karakter uzunluğundadır.*

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | İstem ve maskeye göre oluşturulan değiştirilmiş görüntü(ler). Giriş görüntüsü başına `n` parametresiyle çarpılmış sayıda görüntü döndürür |

---
**Source fingerprint (SHA-256):** `3eb6505a19173d8e4ea4216348f9592fd996cdfe2f07a9e79ccec5f738a8fb93`
