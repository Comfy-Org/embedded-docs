> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/tr.md)

# Genel Bakış

Bir metin istemine dayanarak mevcut bir görüntüyü değiştirin. Bu düğüm, görsellerinizi ve bir metin açıklamasını Grok API'sine gönderir; API, görselleri talimatlarınıza göre düzenler ve sonucu döndürür.

# Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `prompt` | STRING | Evet | Yok | Görüntüyü oluşturmak için kullanılan metin istemi. Boşluklar temizlendikten sonra en az 1 karakter uzunluğunda olmalıdır. |
| `model` | MODEL | Evet | Açıklamaya Bakın | Kullanılacak Grok görüntü modeli. Bu parametre, bir model seçildikten sonra görünen birden çok alt seçeneğe sahiptir. Mevcut modeller: `grok-imagine-image-quality`, `grok-imagine-image-pro`, `grok-imagine-image`. Her modelin farklı yetenekleri vardır (aşağıdaki nota bakın). |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) |

**`model` parametre kısıtlamaları hakkında not:**
- `model` parametresi, `resolution`, `number_of_images`, `images` ve `aspect_ratio` için alt seçenekler içeren dinamik bir birleşik kutudur.
- **`grok-imagine-image-quality`**: En fazla 3 giriş görselini destekler ve özel en boy oranına izin verir.
- **`grok-imagine-image-pro`**: Yalnızca 1 giriş görselini destekler ve özel en boy oranına izin vermez.
- **`grok-imagine-image`**: En fazla 3 giriş görselini destekler ve özel en boy oranına izin verir.
- **Düzenleme için en az bir giriş görseli gereklidir**. Hiçbir görsel sağlanmazsa düğüm bir hata verecektir.
- **Özel en boy oranı** (`aspect_ratio` alt seçeneği) yalnızca görsel girişine birden çok görsel bağlandığında izin verilir. Yalnızca bir görsel sağlanırsa, en boy oranı "auto" olarak ayarlanmalıdır.

# Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `IMAGE` | IMAGE | Grok API'si tarafından döndürülen düzenlenmiş görsel(ler). Tek bir görsel oluşturulursa doğrudan döndürülür. Birden çok görsel oluşturulursa, tek bir toplu tensör halinde birleştirilir. |

---
**Source fingerprint (SHA-256):** `b041b40bb5712a67b09dcb0c841f00cbdd9ef77b9e4f3fdc6b2c4038be447ba5`
