# TextEncodeMageFlowEdit

## Genel Bakış

Bu düğüm, Mage-Flow-Edit modeli için bir düzenleme talimatını (istem) ve bir veya daha fazla referans görüntüyü kodlar. Tüm referans görüntüleri hedef çıktı çözünürlüğüne yeniden boyutlandırır, bir VAE sağlanmışsa bunları gizli uzaya (latent space) kodlar ve referans gizli değerlerini conditioning çıktısına ekler. Örnekleme için doğru boyutlara sahip boş bir gizli tensör de oluşturulur; boyutun her zaman çıktı genişliği ve yüksekliğiyle eşleşmesi sağlanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `clip` | Metin istemlerini tokenize etmek ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet | |
| `prompt` | Uygulanacak düzenleme talimatı (pozitif istem). | STRING | Evet | multiline, dynamic prompts enabled |
| `negative_prompt` | Kaçınılması gereken negatif istem. Varsayılan: boş dize (boş olduğunda dahili olarak bir boşluk kullanılır). Arayüzün gelişmiş bölümünde gösterilir. | STRING | Hayır | çok satırlı, dinamik istemler etkin |
| `vae` | Referans görüntüleri gizli uzaya kodlamak için VAE modeli. Sağlanmazsa, conditioning'e referans gizli değerleri eklenmez. | VAE | Hayır | |
| `images` | Düzenlenecek referans görüntüler. Kodlamadan önce tüm referanslar çıktı çözünürlüğüne yeniden boyutlandırılır. | IMAGE (otomatik büyüme) | Hayır | En fazla 16 görüntü (`image_1`…`image_16` adlarıyla), en az 0 |
| `width` | Piksel cinsinden çıktı genişliği. 0 olarak ayarlanırsa, ilk referans görüntünün genişliği kullanılır. Her zaman 16'nın katına yuvarlanır. Varsayılan: 0. | INT | Evet | 0 ila 8192 (adım 16) |
| `height` | Piksel cinsinden çıktı yüksekliği. Genişlikle aynı geri dönüş davranışına sahiptir. Varsayılan: 0. | INT | Evet | 0 ila 8192 (adım 16) |
| `batch_size` | Oluşturulacak gizli örnek sayısı. Varsayılan: 1. | INT | Evet | 1 ila 4096 |

**Parametre bağımlılıklarına ilişkin notlar:**
- `width` ve/veya `height` 0 ise ve hiçbir referans görüntü sağlanmamışsa, her ikisi de 1024'e geri döner.
- `width` veya `height` değerlerinden yalnızca biri 0 ise, eksik boyut ilk referans görüntüsünden alınırken açıkça ayarlanan boyut korunur.
- `vae` parametresi isteğe bağlıdır; referans gizli değerleri yalnızca bir VAE bağlandığında oluşturulur ve conditioning'e eklenir.
- `negative_prompt` alanı isteğe bağlıdır – boş bırakılırsa, dahili olarak negatif metin olarak tek bir boşluk kullanılır.
- Metin koşullandırması için her referans görüntü, eğitim ön işlemesiyle uyumlu olarak en uzun kenarı en fazla 384 piksel olacak şekilde yeniden boyutlandırılır. VAE kodlama dalı ise tüm referansları tam çıktı çözünürlüğüne yeniden boyutlandırır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `positive` | Pozitif istem tokenlerini ve (bir VAE sağlanmışsa) kodlanmış referans gizli değerlerini içeren conditioning çıktısı. | CONDITIONING |
| `negative` | Negatif istem tokenlerini ve (VAE sağlanmışsa) aynı referans gizli değerlerini içeren conditioning çıktısı. | CONDITIONING |
| `latent` | Örnekleme sırasında başlangıç gürültüsü olarak kullanılmak üzere `[batch_size, 128, height÷16, width÷16]` şeklinde boş bir gizli tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMageFlowEdit/tr.md)

---
**Source fingerprint (SHA-256):** `880d8856b7f6e656bc68ca953fbf892898d05bc5d65290ae3bf7a4405ee09be3`
