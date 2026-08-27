# WanPhantomSubjectToVideo

WanPhantomSubjectToVideo düğümü, Wan video üretimi için koşullandırma verilerini ve bir latent hazırlar. İstenen genişlik, yükseklik, uzunluk ve toplu iş boyutuna göre boş bir latent video oluşturur ve referans görüntüler sağlandığında bunları VAE ile kodlayarak koşullandırmalara zaman boyutlu görsel rehberlik olarak ekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video üretimini yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Belirli özelliklerden kaçınmak için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Referans görüntüler sağlandığında bunları kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, 16'nın katı olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'nın katı olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `uzunluk` | Üretilen videodaki kare sayısı (varsayılan: 81, 4'ün katı olmalıdır) | INT | Evet | 1 ila MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `görseller` | Zaman boyutlu görsel rehberlik olarak kullanılan isteğe bağlı referans görüntüler | IMAGE | Hayır | - |

**Not:** `images` sağlandığında, bunlar otomatik olarak belirtilen `width` ve `height` değerlerine yükseltilir ve işleme için yalnızca ilk `length` görüntü kullanılır. Her görüntü `vae` ile kodlanır ve zaman boyutunda birleştirilir; her görüntünün yalnızca RGB kanalları kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Görüntüler sağlandığında, kodlanmış referans görüntülerin zaman boyutunda birleştirilmesiyle pozitif koşullandırma; aksi takdirde `positive` girdisi değiştirilmeden döndürülür | CONDITIONING |
| `negatif_metin` | Görüntüler sağlandığında, kodlanmış referans görüntülerin zaman boyutunda birleştirilmesiyle negatif koşullandırma; aksi takdirde `negative` girdisi değiştirilmeden döndürülür | CONDITIONING |
| `negatif_img_metin` | Görüntüler sağlandığında, sıfırlanmış zaman boyutlu birleştirme ile negatif koşullandırma; aksi takdirde `negative` girdisi değiştirilmeden döndürülür | CONDITIONING |
| `gizli` | 16 kanallı sıfır dolu latent video tensörü; kare sayısı `length` değerinden, uzamsal boyutları `height` ve `width` değerlerinden türetilir | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
