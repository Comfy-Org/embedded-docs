# OpenRouter Görseli

Bu düğüm, Microsoft'un MAI-Image-2.6 modellerini kullanarak OpenRouter üzerinden görüntü üretir veya düzenler. Metinden görüntü üretmenin yanı sıra, en fazla beş referans görüntüyle görüntü rehberliğinde düzenlemeyi, 1K veya 1.5K çözünürlükte yedi en-boy oranında destekler.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntüyü üretmek için kullanılan OpenRouter görüntü modeli. Bir model seçildiğinde, aşağıda listelenen modele özgü seçenekler görünür. | DYNAMIC_COMBO | Evet | `microsoft/mai-image-2.6`<br>`microsoft/mai-image-2.6-flash` |

### Mai Image 2.6 ve Mai Image 2.6 Flash Girdileri

Her iki model seçeneği (`microsoft/mai-image-2.6` ve `microsoft/mai-image-2.6-flash`) tarafından paylaşılır; bu seçenekler aynı parametre kümesini sunar.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretilecek görüntüyü veya referans görüntülere uygulanacak düzenlemeyi tanımlar. En fazla 20000 karakter. Varsayılan: `""` (boş). Çevresindeki boşluklar kaldırıldıktan sonra en az 1 karakter gerekir. | STRING | Evet | 1 ila 20000 karakter |
| `aspect_ratio` | Üretilen görüntünün en-boy oranı; referans görüntüler bağlandığında da uygulanır. Varsayılan: `"1:1"`. `"auto"`, metinden görüntü üretimi için oranı modelin seçmesini sağlar (1.5K boyutunda oluşturulur) ve düzenleme sırasında ilk referans görüntünün en-boy oranını korur. | COMBO | Evet | `"1:1"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"auto"` |
| `resolution` | Çıktı boyutu kademesi. 1K yaklaşık 1 megapikseldir (1:1 için 1024x1024, 16:9 için 1360x768); 1.5K yaklaşık 2,3 megapikseldir (1:1 için 1536x1536, 16:9 için 2048x1152). Varsayılan: `"1K"`. `aspect_ratio` `"auto"` olduğunda yok sayılır. | COMBO | Evet | `"1K"`<br>`"1.5K"` |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirlemek için kullanılan tohum değeri; API'de tohum yoktur, bu nedenle gerçek sonuçlar bu değerden bağımsız olarak deterministik değildir. Varsayılan: `42`. | INT | Evet | 0 ila 2147483647 |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image_1` ... `image_5` | Genişletilebilir yuva: görüntü rehberliğinde düzenleme için 1 ila 5 referans görüntü bağlayın; toplu bir girdi, her görüntü için bir kez sayılır. Yuvalar isteğe bağlıdır ve boş bırakılabilir (en az 0 bağlı). | IMAGE | Hayır | 0 ila 5 görüntü |

**Notlar:**

- Tüm bağlı yuvalar genelinde toplamda en fazla 5 referans görüntü desteklenir; toplu bir girdi, her görüntü için bir kez sayılır.
- `prompt`, çevresindeki boşluklar kaldırıldıktan sonra en az 1 karakter içermelidir ve 20000 karakteri aşamaz.
- Referans görüntüler PNG verisi olarak gönderilir ve toplamda 2048 x 2048 piksel ile sınırlıdır.
- `aspect_ratio` ayarı, referans görüntüler bağlı olsa bile çıktıya uygulanır.
- `aspect_ratio` `"auto"` olduğunda `resolution` ayarı yok sayılır. Referans görüntü yokken model metinden görüntü üretimi için oranı seçer ve 1.5K boyutunda oluşturur; referans görüntüler bağlıyken ilk referans görüntünün en-boy oranı korunur.
- Tohum değeri API sonucunu etkilemez; yalnızca düğümün yeniden çalışıp çalışmayacağını belirler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Üretilen veya düzenlenen görüntü. Hizmet birkaç görüntü döndürürse, bunlar tek bir toplu IMAGE çıktısında birleştirilir. Hiç görüntü döndürülmezse veya döndürülen bir görüntü çözümlenemezse bir hata oluşturulur. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `d201c18deccd2523041a24427996f51127ca201dfe10fad60c6f768ab79bf852`
