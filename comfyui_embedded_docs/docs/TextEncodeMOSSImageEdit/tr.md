# Text Encode MOSS-Image Edit

Bir düzenleme talimatını referans görsellerle birlikte MOSS-Image düzenleme LoRA'sı için koşullandırmaya kodlar. Çıktıyı pozitif koşullandırma olarak bağlayın ve negatif için aynı referanslarla ikinci bir örnek çalıştırın. Referanslar geldikleri boyutta kullanılır, bu nedenle bağlamadan önce ölçeklendirin. Bu düğüm ComfyUI'da deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Talimatı tokenize eden ve kodlayan CLIP modeli. | CLIP | Evet | - |
| `prompt` | Düzenlemeyi tanımlayan talimat. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | Herhangi bir metin |
| `vae` | Referans görselleri referans latentlerine kodlamak için kullanılan VAE. | VAE | Evet | - |
| `edit_format` | Düzenleme LoRA'sının eğitildiği düzen. Referans latentleri yöntemini ve metin kodlayıcının referansları da görüp görmeyeceğini seçer. | COMBO | Evet | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Büyütülebilir yuva: bir veya daha fazla referans görseli bağlayın (`image_1`, `image_2`, ...). Her görsel geldiği boyutta kullanılır, alfa kanalı çıkarılır ve bir referans latentine VAE ile kodlanır. | IMAGE | Evet | 1 veya daha fazla görsel |

**Not:** `"ai-toolkit"` ve `"ai-toolkit (kv_cache off)"` ile metin kodlayıcı ayrıca her referansı görür; bunlar en fazla 384x384 piksele küçültülür ve istemde bir `Picture N:` işaretçisiyle öncelenir, böylece talimat bunlara numarayla atıfta bulunabilir. `"Moss-Image-Edit"` ile referanslar modele yalnızca referans latentleri olarak ulaşır ve metin kodlayıcı talimatı tek başına görür. `"ai-toolkit (kv_cache off)"` ek olarak referansların oluşturulan görsele dikkat etmesini sağlar, böylece her örnekleme adımında yeniden hesaplanırlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Kodlanmış talimat, referans latentleri ve eşleşen referans latentleri yöntemi eklenmiş olarak. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/tr.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
