# Text Encode MOSS-Image Edit

Bir düzenleme talimatını referans görsellerle birlikte MOSS-Image düzenleme LoRA'sı için koşullandırmaya kodlar. Çıktıyı pozitif koşullandırma olarak bağlayın ve negatif için aynı referanslarla ikinci bir örnek çalıştırın. Referanslar geldikleri boyutta kullanılır, bu nedenle bağlamadan önce ölçeklendirin. Bu düğüm ComfyUI'da deneysel olarak işaretlenmiştir. VAE olmadan görseller yalnızca metin kodlayıcıya gider.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Talimatı tokenize eden ve kodlayan CLIP modeli. | CLIP | Evet | - |
| `prompt` | Düzenlemeyi tanımlayan talimat. Çok satırlı metin ve dinamik istemleri destekler. | STRING | Evet | Herhangi bir metin |
| `vae` | Referans görselleri referans latentlerine kodlamak için kullanılan VAE. İsteğe bağlı: olmadan görseller yalnızca metin kodlayıcıya gider.| VAE | Hayır | - |
| `edit_format` | Düzenleme LoRA'sının eğitildiği düzen. Referans latentleri yöntemini ve metin kodlayıcının referansları da görüp görmeyeceğini seçer. | COMBO | Evet | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Büyütülebilir yuva: bir veya daha fazla referans görseli bağlayın (`image_1`, `image_2`, ...). Her görsel geldiği boyutta kullanılır, alfa kanalı çıkarılır ve bir referans latentine VAE ile kodlanır. VAE bağlıysa alfa atılır ve her görsel referans latentine kodlanır; VAE yoksa görseller yalnızca metin kodlayıcıya gider.| IMAGE | Evet | 1 veya daha fazla görsel |
| `image_strength` | Metin kodlayıcının gördüğü görsellere modelin ne kadar dikkat ettiğini ölçekler (ai-toolkit biçimleri veya VAE yok): 0 yok sayar, 1 değişmez, 1 üstü vurgular. Gelişmiş. Varsayılan: 1.0. | FLOAT | Evet | 0.0 to 100.0 (step 0.05) |

**Not:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Kodlanmış talimat, referans latentleri ve eşleşen referans latentleri yöntemi eklenmiş olarak. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/tr.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
