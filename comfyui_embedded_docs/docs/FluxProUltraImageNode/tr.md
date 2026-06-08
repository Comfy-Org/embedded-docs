Flux Pro 1.1 Ultra API aracılığıyla, istem ve çözünürlüğe bağlı olarak görseller üretir. Bu düğüm, metin açıklamanıza ve belirtilen boyutlara göre görseller oluşturmak için harici bir hizmete bağlanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Görsel oluşturma için istem (varsayılan: boş dize) | STRING | Evet | - |
| `istem_yükseltme` | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı bir üretim için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum değeri tam olarak aynı sonucu üretmez). (varsayılan: False) | BOOLEAN | Hayır | - |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) | INT | Hayır | 0 ile 18446744073709551615 arası |
| `en_boy_oranı` | Görselin en-boy oranı; 1:4 ile 4:1 arasında olmalıdır. (varsayılan: "16:9") | STRING | Hayır | - |
| `ham` | True olduğunda, daha az işlenmiş, daha doğal görünümlü görseller üretir. (varsayılan: False) | BOOLEAN | Hayır | - |
| `görüntü_istemi` | Üretimi yönlendirmek için isteğe bağlı referans görseli | IMAGE | Hayır | - |
| `görüntü_istemi_gücü` | İstem ile görsel istemi arasındaki karışım oranı. (varsayılan: 0.1) | FLOAT | Hayır | 0.0 ile 1.0 arası |

**Not:** `aspect_ratio` parametresi 1:4 ile 4:1 arasında olmalıdır. `image_prompt` sağlandığında, `image_prompt_strength` etkinleşir ve referans görselin nihai çıktıyı ne kadar etkileyeceğini kontrol eder. `image_prompt` sağlanmazsa, `prompt` parametresinin boş olmadığı doğrulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output_image` | Flux Pro 1.1 Ultra'dan oluşturulan görsel | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `8632aeb76e9007d65d7f3fd51465fe78f56ba92264ef65ce505db2fc95cfd25b`
