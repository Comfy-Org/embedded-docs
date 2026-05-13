> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/tr.md)

Pika Swaps düğümü, videonuzdaki nesneleri veya bölgeleri yeni bir görüntüyle değiştirir. Değiştirilecek alanları bir maske kullanarak tanımlarsınız ve düğüm, video dizisi boyunca belirtilen içeriği sorunsuz bir şekilde değiştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | İçinde nesne değiştirilecek video. |
| `image` | IMAGE | Evet | - | Videodaki maskelenmiş nesneyi değiştirmek için kullanılan görüntü. |
| `mask` | MASK | Evet | - | Videoda değiştirilecek alanları tanımlamak için maskeyi kullanın. |
| `prompt_text` | STRING | Evet | - | İstenen değiştirmeyi tanımlayan metin istemi. |
| `negative_prompt` | STRING | Evet | - | Değiştirmede kaçınılması gerekenleri tanımlayan metin istemi. |
| `seed` | INT | Evet | 0 ile 4294967295 arası | Tutarlı sonuçlar için rastgele tohum değeri. |

**Not:** Bu düğüm, tüm giriş parametrelerinin sağlanmasını gerektirir. `video`, `image` ve `mask` birlikte çalışarak değiştirme işlemini tanımlar; maske, videonun hangi alanlarının sağlanan görüntü ile değiştirileceğini belirtir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Belirtilen nesne veya bölgenin değiştirildiği işlenmiş video. |

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`
