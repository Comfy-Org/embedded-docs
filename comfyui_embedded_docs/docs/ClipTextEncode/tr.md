# CLIP Metin Kodlama (İstem)

`CLIP Text Encode (CLIPTextEncode)`, metin açıklamalarınızı yapay zekânın anlayabileceği bir biçime dönüştüren bir çevirmen gibi çalışır. Bu, yapay zekânın girdinizi yorumlamasına ve istenen görüntüyü oluşturmasına yardımcı olur.

Bunu farklı bir dil konuşan bir sanatçıyla iletişim kurmak gibi düşünün. Devasa görüntü-metin çiftleriyle eğitilmiş CLIP modeli, açıklamalarınızı yapay zekâ modelinin takip edebileceği "talimatlara" dönüştürerek bu boşluğu kapatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `text` | Kodlanacak metin. Çok satırlı girişi ve dinamik promptları destekler. | STRING | Evet | Herhangi bir metin |
| `clip` | Metni kodlamak için kullanılan CLIP modeli. | CLIP | Evet | Yüklenen CLIP modelleri |

**Not**: `clip` girdisi geçerli bir CLIP modeli olmalıdır. `None` ise, düğüm bir hata verir. Bu genellikle bir checkpoint yükleyici düğümü tarafından yüklenen checkpoint geçerli bir CLIP veya metin kodlayıcı modeli içermediğinde meydana gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Gömülü metni içeren ve difüzyon modelini yönlendirmek için kullanılan bir koşullandırma. | CONDITIONING |

## Prompt Özellikleri

### Embedding Modelleri

Embedding modelleri, belirli sanatsal efektler veya stiller uygulamanıza olanak tanır. Desteklenen biçimler `.safetensors`, `.pt` ve `.bin` dosyalarıdır. Bir embedding modeli kullanmak için:

1. Dosyayı `ComfyUI/models/embeddings` klasörüne yerleştirin.
2. Metninizde `embedding:model_name` kullanarak referans verin.

Örnek: `ComfyUI/models/embeddings` klasöründe `EasyNegative.pt` adında bir modeliniz varsa, onu şu şekilde kullanabilirsiniz:

```
worst quality, embedding:EasyNegative, bad quality
```

**ÖNEMLİ**: Embedding modellerini kullanırken dosya adının eşleştiğini ve modelinizin mimarisiyle uyumlu olduğunu doğrulayın. Örneğin, SD1.5 için tasarlanmış bir embedding, SDXL modeli için doğru çalışmayacaktır.

### Prompt Ağırlık Ayarı

Parantez kullanarak açıklamanızın belirli bölümlerinin önemini ayarlayabilirsiniz. Örneğin:

- `(beautiful:1.2)` "beautiful" kelimesinin ağırlığını artırır.
- `(beautiful:0.8)` "beautiful" kelimesinin ağırlığını azaltır.
- Düz parantezler `(beautiful)` varsayılan 1.1 ağırlığını uygular.

Ağırlıkları hızlıca ayarlamak için `ctrl + yukarı/aşağı ok` kısayol tuşlarını kullanabilirsiniz. Ağırlık ayarlama adım boyutu ayarlardan değiştirilebilir.

Promptunuzda ağırlığı değiştirmeden gerçek parantezler kullanmak istiyorsanız, onları bir ters eğik çizgi ile kaçış karakteri kullanarak belirtebilirsiniz, ör. `\(word\)`.

### Wildcard/Dinamik Promptlar

Dinamik promptlar oluşturmak için `{}` kullanın. Örneğin, `{day|night|morning}` prompt işlendiğinde her seferinde rastgele bir seçenek seçecektir.

Promptunuzda dinamik davranışı tetiklemeden gerçek küme parantezleri eklemek istiyorsanız, onları bir ters eğik çizgi ile kaçış karakteri kullanarak belirtebilirsiniz, ör. `\{word\}`.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/tr.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
