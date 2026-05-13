> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/tr.md)

Flux Pro 1.1 Ultra API aracılığıyla, istem ve çözünürlüğe bağlı olarak görseller üretir. Bu düğüm, metin açıklamanıza ve belirtilen boyutlara göre görseller oluşturmak için harici bir hizmete bağlanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görsel oluşturma için istem (varsayılan: boş dize) |
| `istem_yükseltme` | BOOLEAN | Hayır | - | İstem üzerinde yukarı örnekleme yapılıp yapılmayacağı. Etkinleştirilirse, daha yaratıcı bir üretim için istemi otomatik olarak değiştirir, ancak sonuçlar deterministik değildir (aynı tohum değeri tam olarak aynı sonucu üretmez). (varsayılan: False) |
| `tohum` | INT | Hayır | 0 ile 18446744073709551615 arası | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) |
| `en_boy_oranı` | STRING | Hayır | - | Görselin en-boy oranı; 1:4 ile 4:1 arasında olmalıdır. (varsayılan: "16:9") |
| `ham` | BOOLEAN | Hayır | - | True olduğunda, daha az işlenmiş, daha doğal görünümlü görseller üretir. (varsayılan: False) |
| `görüntü_istemi` | IMAGE | Hayır | - | Üretimi yönlendirmek için isteğe bağlı referans görseli |
| `görüntü_istemi_gücü` | FLOAT | Hayır | 0.0 ile 1.0 arası | İstem ile görsel istemi arasındaki karışım oranı. (varsayılan: 0.1) |

**Not:** `aspect_ratio` parametresi 1:4 ile 4:1 arasında olmalıdır. `image_prompt` sağlandığında, `image_prompt_strength` etkinleşir ve referans görselin nihai çıktıyı ne kadar etkileyeceğini kontrol eder. `image_prompt` sağlanmazsa, `prompt` parametresinin boş olmadığı doğrulanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_image` | IMAGE | Flux Pro 1.1 Ultra'dan oluşturulan görsel |

---
**Source fingerprint (SHA-256):** `8632aeb76e9007d65d7f3fd51465fe78f56ba92264ef65ce505db2fc95cfd25b`
