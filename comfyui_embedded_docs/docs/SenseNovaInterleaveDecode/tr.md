# SenseNova Interleave Decode

SenseNova Conditioning tarafından bırakılan interleave geçmişini kullanılabilir metin, görüntü ve düşünmeye dönüştürün. Modelin tek geçişte ürettiği her şeyi toplamak için bunu döngünün sonunda, End Loop accumulate devre dışıyken çalıştırın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Oluşturulan token'ları çözmek için kullanılan SenseNova CLIP modeli. | CLIP | Evet | - |
| `koşullandırma` | SenseNova Conditioning'den gelen interleave koşullandırması. | CONDITIONING | Evet | - |
| `örnekler` | Son KSampler piksel latent değeri; döngü bir görüntü isteğiyle sona erdiğinde gerekir. | LATENT | Hayır | - |

**Kısıtlamalar ve davranış:**

* Koşullandırma, SenseNova Conditioning'den `interleave` veya `self-correction` görevinde gelmelidir; bunun dışındaki herhangi bir şey hata oluşturur.
* Model bir görüntü beklerken, örnekleyicinin LATENT çıktısını `samples` parametresine bağlayın.
* Çalıştırmanın başında bağlanan referans görüntüleri çıktıdan hariç tutulur ve görüntü oluşturulmadığında görüntü tüketicileri atlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `text` | Interleave geçmişinden çözülen metin; görüntü işaretleri boş satırlarla değiştirilmiştir. | STRING |
| `images` | Modelin çalıştırma sırasında oluşturduğu görüntüler. | IMAGE |
| `thinking` | Modelin ürettiği akıl yürütme metni. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaInterleaveDecode/tr.md)

---
**Source fingerprint (SHA-256):** `62c7ded50c1348e2242319209729a17d543d80e4d01ddf173cf8b77e4fd0be50`
