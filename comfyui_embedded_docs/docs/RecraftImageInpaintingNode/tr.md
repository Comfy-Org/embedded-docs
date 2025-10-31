> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/tr.md)

Bu düğüm, görüntüleri bir metin istemi ve maske temelinde değiştirir. Recraft API'sini kullanarak, bir maske ile tanımladığınız belirli alanları akıllıca düzenlerken, görüntünün geri kalanını değiştirmeden bırakır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Değiştirilecek giriş görüntüsü |
| `mask` | MASK | Evet | - | Görüntünün hangi alanlarının değiştirileceğini tanımlayan maske |
| `prompt` | STRING | Evet | - | Görüntü oluşturma için istem (varsayılan: boş dize) |
| `n` | INT | Evet | 1-6 | Oluşturulacak görüntü sayısı (varsayılan: 1, minimum: 1, maksimum: 6) |
| `seed` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak belirsizdir (varsayılan: 0, minimum: 0, maksimum: 18446744073709551615) |
| `recraft_style` | STYLEV3 | Hayır | - | Recraft API'si için isteğe bağlı stil parametresi |
| `negative_prompt` | STRING | Hayır | - | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) |

*Not: Boyama işleminin çalışması için `image` ve `mask` birlikte sağlanmalıdır. Maske, görüntü boyutlarına uyacak şekilde otomatik olarak yeniden boyutlandırılacaktır.*

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | İstem ve maske temelinde oluşturulan değiştirilmiş görüntü(ler) |