> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/tr.md)

T5TokenizerOptions düğümü, çeşitli T5 model türleri için tokenizer ayarlarını yapılandırmanıza olanak tanır. t5xxl, pile_t5xl, t5base, mt5xl ve umt5xxl dahil olmak üzere birden fazla T5 model varyantı için minimum dolgu ve minimum uzunluk parametrelerini ayarlar. Düğüm bir CLIP girişi alır ve belirtilen tokenizer seçenekleri uygulanmış şekilde değiştirilmiş bir CLIP döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | - | Tokenizer seçeneklerini yapılandırmak için kullanılacak CLIP modeli |
| `min_padding` | INT | Hayır | 0-10000 | Tüm T5 model türleri için ayarlanacak minimum dolgu değeri (varsayılan: 0) |
| `min_length` | INT | Hayır | 0-10000 | Tüm T5 model türleri için ayarlanacak minimum uzunluk değeri (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | CLIP | Tüm T5 varyantlarına uygulanmış güncellenmiş tokenizer seçenekleriyle değiştirilmiş CLIP modeli |