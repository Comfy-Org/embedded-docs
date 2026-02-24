> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/tr.md)

`CLIP Text Encode (CLIPTextEncode)`, metin açıklamalarınızı AI'nın anlayabileceği bir formata dönüştüren bir çevirmen gibi çalışır. Bu, AI'nın girdinizi yorumlamasına ve istenen görseli oluşturmasına yardımcı olur.

Farklı bir dil konuşan bir sanatçıyla iletişim kurmak gibi düşünün. Geniş görsel-metin çiftleri üzerinde eğitilmiş CLIP modeli, açıklamalarınızı AI modelinin takip edebileceği "talimatlara" dönüştürerek bu boşluğu kapatır.

## Girdiler

| Parametre | Veri Türü | Girdi Yöntemi | Varsayılan | Aralık | Açıklama |
|-----------|-----------|--------------|---------|--------|-------------|
| text | STRING | Metin Girdisi | Boş | Herhangi bir metin | Oluşturmak istediğiniz görselin açıklamasını (prompt) girin. Detaylı açıklamalar için çok satırlı girdiyi destekler. |
| clip | CLIP | Model Seçimi | Yok | Yüklenmiş CLIP modelleri | Açıklamanızı AI modeli için talimatlara çevirirken kullanılacak CLIP modelini seçin. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| CONDITIONING | CONDITIONING | AI modelini bir görsel oluştururken yönlendiren, açıklamanızın işlenmiş "talimatları". |

## Prompt Özellikleri

### Gömme (Embedding) Modelleri

Gömme modelleri, belirli sanatsal efektler veya stiller uygulamanıza olanak tanır. Desteklenen formatlar `.safetensors`, `.pt` ve `.bin`'i içerir. Bir gömme modeli kullanmak için:

1. Dosyayı `ComfyUI/models/embeddings` klasörüne yerleştirin.
2. Metninizde `embedding:model_adi` kullanarak ona referans verin.

Örnek: `ComfyUI/models/embeddings` klasörünüzde `EasyNegative.pt` adlı bir modeliniz varsa, onu şu şekilde kullanabilirsiniz:

```
worst quality, embedding:EasyNegative, bad quality
```

**ÖNEMLİ**: Gömme modelleri kullanırken, dosya adının eşleştiğinden ve model mimarinizle uyumlu olduğundan emin olun. Örneğin, SD1.5 için tasarlanmış bir gömme, bir SDXL modeli için doğru çalışmayacaktır.

### Prompt Ağırlık Ayarlama

Parantez kullanarak açıklamanızın belirli bölümlerinin önemini ayarlayabilirsiniz. Örneğin:

- `(beautiful:1.2)`, "beautiful" kelimesinin ağırlığını artırır.
- `(beautiful:0.8)`, "beautiful" kelimesinin ağırlığını azaltır.
- Sade parantezler `(beautiful)`, varsayılan olarak 1.1 ağırlığı uygular.

Ağırlıkları hızlıca ayarlamak için `ctrl + yukarı/aşağı ok` klavye kısayollarını kullanabilirsiniz. Ağırlık ayarlama adım boyutu ayarlardan değiştirilebilir.

Prompt'unuzda ağırlığı değiştirmeden gerçek parantezler eklemek istiyorsanız, onları ters eğik çizgi kullanarak kaçış karakteri ile yazabilirsiniz, örn. `\(word\)`.

### Joker/Dinamik Prompt'lar

Dinamik prompt'lar oluşturmak için `{}` kullanın. Örneğin, `{day|night|morning}` her prompt işlendiğinde rastgele bir seçenek seçecektir.

Prompt'unuzda dinamik davranışı tetiklemeden gerçek süslü parantezler eklemek istiyorsanız, onları ters eğik çizgi kullanarak kaçış karakteri ile yazabilirsiniz, örn. `\{word\}`.

### Prompt'larda Yorumlar

Prompt'tan hariç tutulan yorumlar eklemek için şunları kullanabilirsiniz:

- Tek bir satırı yorum satırı yapmak için `//`.
- Bir bölümü veya birden çok satırı yorum satırı yapmak için `/* */`.

Örnek:

```
// bu satır prompt'tan hariç tutulur.
a beautiful landscape, /* bu kısım göz ardı edilir */ high quality
```
