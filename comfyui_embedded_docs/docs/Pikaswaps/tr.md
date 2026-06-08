Pika Swaps düğümü, videonuzdaki nesneleri veya bölgeleri yeni bir görüntüyle değiştirir. Değiştirilecek alanları bir maske kullanarak tanımlarsınız ve düğüm, video dizisi boyunca belirtilen içeriği sorunsuz bir şekilde değiştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | İçinde nesne değiştirilecek video. | VIDEO | Evet | - |
| `image` | Videodaki maskelenmiş nesneyi değiştirmek için kullanılan görüntü. | IMAGE | Evet | - |
| `mask` | Videoda değiştirilecek alanları tanımlamak için maskeyi kullanın. | MASK | Evet | - |
| `prompt_text` | İstenen değiştirmeyi tanımlayan metin istemi. | STRING | Evet | - |
| `negative_prompt` | Değiştirmede kaçınılması gerekenleri tanımlayan metin istemi. | STRING | Evet | - |
| `seed` | Tutarlı sonuçlar için rastgele tohum değeri. | INT | Evet | 0 ile 4294967295 arası |

**Not:** Bu düğüm, tüm giriş parametrelerinin sağlanmasını gerektirir. `video`, `image` ve `mask` birlikte çalışarak değiştirme işlemini tanımlar; maske, videonun hangi alanlarının sağlanan görüntü ile değiştirileceğini belirtir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Belirtilen nesne veya bölgenin değiştirildiği işlenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/tr.md)

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`
