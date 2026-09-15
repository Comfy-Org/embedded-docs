# WanPhantomSubjectToVideo

WanPhantomSubjectToVideo düğümü, Wan video oluşturma için koşullandırma verilerini ve bir latent hazırlar. İstenen genişlik, yükseklik, uzunluk ve toplu iş boyutundan boş bir latent video oluşturur; referans görüntüler sağlandığında ise bunları VAE ile kodlar ve zaman boyutlu görsel kılavuz olarak koşullandırmalara ekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı yönlendirmek için pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Belirli özelliklerden kaçınmak için negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Referans görüntüler sağlandığında bunları kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı video genişliği piksel cinsinden (varsayılan: 832) | INT | Evet | 16 - MAX_RESOLUTION (adım 16) |
| `yükseklik` | Çıktı video yüksekliği piksel cinsinden (varsayılan: 480) | INT | Evet | 16 - MAX_RESOLUTION (adım 16) |
| `uzunluk` | Oluşturulan videodaki kare sayısı (varsayılan: 81) | INT | Evet | 1 - MAX_RESOLUTION (adım 4) |
| `toplu_iş_boyutu` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `görseller` | Zaman boyutlu görsel kılavuz olarak kullanılan isteğe bağlı referans görüntüler | IMAGE | Hayır | - |

**Not:** `images` sağlandığında, belirtilen `width` ve `height` ile eşleşecek şekilde otomatik olarak ölçeklenir ve işleme için yalnızca ilk `length` görüntü kullanılır. Her görüntü `vae` ile kodlanır ve zaman boyutunda birleştirilir; ayrıca her görüntünün yalnızca RGB kanalları kullanılır. `images` sağlanmadığında, üç koşullandırma çıktısının tümü girdi koşullandırmalarından değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görüntüler sağlandığında kodlanmış referans görüntülerin zaman boyutunda birleştirildiği pozitif koşullandırma; aksi halde girdi `positive` değiştirilmeden döndürülür | CONDITIONING |
| `negative_text` | Görüntüler sağlandığında kodlanmış referans görüntülerin zaman boyutunda birleştirildiği negatif koşullandırma; aksi halde girdi `negative` değiştirilmeden döndürülür | CONDITIONING |
| `negative_img_text` | Görüntüler sağlandığında sıfırlanmış zaman boyutlu birleştirmeye sahip negatif koşullandırma; aksi halde girdi `negative` değiştirilmeden döndürülür | CONDITIONING |
| `latent` | 16 kanallı sıfırlarla doldurulmuş latent video tensörü; kare sayısı `length` değerinden, uzamsal boyutları `height` ve `width` değerlerinden türetilir | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
