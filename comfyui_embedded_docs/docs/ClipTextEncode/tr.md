> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/tr.md)

`CLIP Text Encode (CLIPTextEncode)`, metin açıklamalarınızı yapay zekanın anlayabileceği bir formata dönüştüren bir çevirmen görevi görür. Bu, yapay zekanın girdinizi yorumlamasına ve istenen görüntüyü oluşturmasına yardımcı olur.

Bunu, farklı bir dil konuşan bir sanatçıyla iletişim kurmak gibi düşünün. Devasa görüntü-metin çiftleri üzerinde eğitilmiş CLIP modeli, açıklamalarınızı yapay zeka modelinin takip edebileceği "talimatlara" dönüştürerek bu boşluğu doldurur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `metin` | STRING | Evet | Herhangi bir metin | Kodlanacak metin. Çok satırlı girişi ve dinamik promptları destekler. |
| `clip` | CLIP | Evet | Yüklenmiş CLIP modelleri | Metni kodlamak için kullanılan CLIP modeli. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `CONDITIONING` | CONDITIONING | Difüzyon modelini yönlendirmek için kullanılan, gömülü metni içeren bir koşullandırma. |

## Prompt Özellikleri

### Gömme Modelleri

Gömme modelleri, belirli sanatsal efektler veya stiller uygulamanıza olanak tanır. Desteklenen formatlar `.safetensors`, `.pt` ve `.bin`'dir. Bir gömme modeli kullanmak için:

1. Dosyayı `ComfyUI/models/embeddings` klasörüne yerleştirin.
2. Metninizde `embedding:model_adı` kullanarak ona başvurun.

Örnek: `ComfyUI/models/embeddings` klasörünüzde `EasyNegative.pt` adında bir modeliniz varsa, onu şu şekilde kullanabilirsiniz:

```
worst quality, embedding:EasyNegative, bad quality
```

**ÖNEMLİ**: Gömme modellerini kullanırken, dosya adının eşleştiğini ve modelinizin mimarisiyle uyumlu olduğunu doğrulayın. Örneğin, SD1.5 için tasarlanmış bir gömme, bir SDXL modeli için doğru çalışmayacaktır.

### Prompt Ağırlık Ayarı

Parantez kullanarak açıklamanızın belirli bölümlerinin önemini ayarlayabilirsiniz. Örneğin:

- `(beautiful:1.2)` "beautiful" kelimesinin ağırlığını artırır.
- `(beautiful:0.8)` "beautiful" kelimesinin ağırlığını azaltır.
- Düz parantezler `(beautiful)` varsayılan olarak 1.1 ağırlığı uygulayacaktır.

Ağırlıkları hızlı bir şekilde ayarlamak için `ctrl + yukarı/aşağı ok` klavye kısayollarını kullanabilirsiniz. Ağırlık ayarlama adım boyutu ayarlardan değiştirilebilir.

Promptunuzda ağırlığı değiştirmeden gerçek parantez karakterlerini kullanmak istiyorsanız, bunları bir ters eğik çizgi ile kaçış karakteri olarak kullanabilirsiniz, örn. `\(kelime\)`.

### Joker Karakter/Dinamik Promptlar

Dinamik promptlar oluşturmak için `{}` kullanın. Örneğin, `{gündüz|gece|sabah}` promptu her işlendiğinde rastgele bir seçenek seçecektir.

Promptunuzda dinamik davranışı tetiklemeden gerçek küme parantezlerini kullanmak istiyorsanız, bunları bir ters eğik çizgi ile kaçış karakteri olarak kullanabilirsiniz, örn. `\{kelime\}`.

### Promptlarda Yorumlar

Aşağıdakileri kullanarak prompttan hariç tutulan yorumlar ekleyebilirsiniz:

- Tek bir satırı yorum satırı yapmak için `//`.
- Bir bölümü veya birden çok satırı yorum satırı yapmak için `/* */`.

Örnek:

```
// bu satır prompttan hariç tutulur.
a beautiful landscape, /* bu kısım yok sayılır */ high quality
```

---
**Source fingerprint (SHA-256):** `e8f286cdec879c529270e110ccf5959ed6df77737cfb5a8019379afac9266118`
