# ClipTextEncode

`CLIP Text Encode (CLIPTextEncode)` bir çevirmen gibi çalışır; metin açıklamalarınızı yapay zekanın anlayabileceği bir biçime dönüştürür. Bu, yapay zekanın girdinizi yorumlamasına ve istenen görüntüyü oluşturmasına yardımcı olur.

Bunu farklı bir dil konuşan bir sanatçıyla iletişim kurmak gibi düşünün. Geniş görüntü-metin çiftleriyle eğitilen CLIP modeli, açıklamalarınızı yapay zeka modelinin takip edebileceği "talimatlara" dönüştürerek bu boşluğu kapatır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `metin` | Kodlanacak metin. Çok satırlı girdiyi ve dinamik promptları destekler. | STRING | Evet | Herhangi bir metin |
| `clip` | Metni kodlamak için kullanılan CLIP modeli. | CLIP | Evet | Yüklenmiş CLIP modelleri |

Not: `clip` girdisi None ise (örneğin, checkpoint yükleyiciden gelen checkpoint geçerli bir CLIP veya metin kodlayıcı modeli içermiyorsa), düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `CONDITIONING` | Diffüzyon modelini yönlendirmek için kullanılan, gömülü metni içeren bir koşullandırma. | CONDITIONING |

## Prompt Özellikleri

### Embedding Modelleri

Embedding modelleri, belirli sanatsal efektler veya stiller uygulamanıza olanak tanır. Desteklenen biçimler `.safetensors`, `.pt` ve `.bin` şeklindedir. Bir embedding modeli kullanmak için:

1. Dosyayı `ComfyUI/models/embeddings` klasörüne yerleştirin.
2. Metninizde `embedding:model_name` kullanarak ona başvurun.

Örnek: Eğer `ComfyUI/models/embeddings` klasörünüzde `EasyNegative.pt` adında bir modeliniz varsa, bunu şu şekilde kullanabilirsiniz:

```
worst quality, embedding:EasyNegative, bad quality
```

**ÖNEMLİ**: Embedding modellerini kullanırken, dosya adının eşleştiğini ve modelinizin mimarisiyle uyumlu olduğunu doğrulayın. Örneğin, SD1.5 için tasarlanmış bir embedding, SDXL modeliyle doğru çalışmayacaktır.

### Prompt Ağırlığı Ayarı

Açıklamanızın belirli bölümlerinin önemini parantez kullanarak ayarlayabilirsiniz. Örneğin:

- `(beautiful:1.2)` "beautiful" ifadesinin ağırlığını artırır.
- `(beautiful:0.8)` "beautiful" ifadesinin ağırlığını azaltır.
- Düz parantezler `(beautiful)` varsayılan ağırlık olarak 1.1 uygular.

Klavye kısayolları `ctrl + yukarı/aşağı ok` ile ağırlıkları hızlıca ayarlayabilirsiniz. Ağırlık ayarlama adım boyutu ayarlardan değiştirilebilir.

Promptunuzda ağırlığı değiştirmeden gerçek parantezler kullanmak istiyorsanız, bunları bir ters eğik çizgi ile kaçış karakteri olarak belirtebilirsiniz; örn. `\(word\)`.

### Wildcard/Dinamik Promptlar

Dinamik promptlar oluşturmak için `{}` kullanın. Örneğin, `{day|night|morning}` prompt her işlendiğinde seçeneklerden birini rastgele seçer.

Promptunuzda dinamik davranışı tetiklemeden gerçek süslü parantezler kullanmak istiyorsanız, bunları bir ters eğik çizgi ile kaçış karakteri olarak belirtebilirsiniz; örn. `\{word\}`.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/tr.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
