# ClipTextEncode

Bir metin istemini CLIP modeli kullanarak, difüzyon modelini belirli görüntüler üretmeye yönlendirmek için kullanılabilecek bir gömmeye kodlar.

`CLIP Text Encode (CLIPTextEncode)`, metin açıklamalarınızı yapay zekânın anlayabileceği bir biçime dönüştüren bir çevirmen gibi çalışır. Bu, yapay zekânın girdinizi yorumlamasına ve istenen görüntüyü oluşturmasına yardımcı olur.

Bunu, farklı bir dil konuşan bir sanatçıyla iletişim kurmak gibi düşünün. Geniş görüntü-metin çiftleri üzerinde eğitilmiş CLIP modeli, açıklamalarınızı yapay zekâ modelinin takip edebileceği "talimatlara" dönüştürerek bu boşluğu kapatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `metin` | Kodlanacak metin. Çok satırlı girişi ve dinamik istemleri destekler. | STRING | Evet | Herhangi bir metin |
| `clip` | Metni kodlamak için kullanılan CLIP modeli. | CLIP | Evet | Yüklenmiş CLIP modelleri |

Not: `clip` girişi None ise (örneğin, checkpoint'i geçerli bir CLIP veya metin kodlayıcı modeli içermeyen bir checkpoint yükleyiciden geldiğinde), düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Difüzyon modelini yönlendirmek için kullanılan gömülü metni içeren bir koşullandırma. | CONDITIONING |

## İstem Özellikleri

### Gömme Modelleri

Gömme modelleri, belirli sanatsal efektleri veya stilleri uygulamanıza olanak tanır. Desteklenen biçimler `.safetensors`, `.pt` ve `.bin`'i içerir. Bir gömme modeli kullanmak için:

1. Dosyayı `ComfyUI/models/embeddings` klasörüne yerleştirin.
2. Metninizde `embedding:model_name` kullanarak ona başvurun.

Örnek: `ComfyUI/models/embeddings` klasörünüzde `EasyNegative.pt` adında bir modeliniz varsa, şu şekilde kullanabilirsiniz:

```
worst quality, embedding:EasyNegative, bad quality
```

**ÖNEMLİ**: Gömme modellerini kullanırken, dosya adının eşleştiğini ve modelinizin mimarisiyle uyumlu olduğunu doğrulayın. Örneğin, SD1.5 için tasarlanmış bir gömme, bir SDXL modeli için doğru çalışmaz.

### İstem Ağırlığı Ayarı

Açıklamanızın belirli bölümlerinin önemini parantez kullanarak ayarlayabilirsiniz. Örneğin:

- `(beautiful:1.2)`, "beautiful" ifadesinin ağırlığını artırır.
- `(beautiful:0.8)`, "beautiful" ifadesinin ağırlığını azaltır.
- Düz parantezler `(beautiful)`, varsayılan olarak 1.1 ağırlığı uygular.

Ağırlıkları hızlıca ayarlamak için `ctrl + yukarı/aşağı ok` klavye kısayollarını kullanabilirsiniz. Ağırlık ayarı adım boyutu ayarlardan değiştirilebilir.

İsteminizde ağırlığı değiştirmeden gerçek parantezler eklemek isterseniz, ters eğik çizgi kullanarak kaçış karakteriyle ayırabilirsiniz; örn. `\(word\)`.

### Joker/Dinamik İstemler

Dinamik istemler oluşturmak için `{}` kullanın. Örneğin, `{day|night|morning}`, istem her işlendiğinde rastgele bir seçenek seçer.

İsteminizde dinamik davranışı tetiklemeden gerçek süslü parantezler eklemek isterseniz, ters eğik çizgi kullanarak kaçış karakteriyle ayırabilirsiniz; örn. `\{word\}`.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/tr.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
