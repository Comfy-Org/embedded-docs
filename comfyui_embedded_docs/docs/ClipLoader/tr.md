> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/tr.md)

Bu düğüm temel olarak CLIP metin kodlayıcı modellerini bağımsız olarak yüklemek için kullanılır.
Model dosyaları şu yollarda tespit edilebilir:

- "ComfyUI/models/text_encoders/"
- "ComfyUI/models/clip/"

> ComfyUI başladıktan sonra bir model kaydederseniz, en son model dosyası yol listesini almak için ComfyUI önyüzünü yenilemeniz gerekecektir

Desteklenen model formatları:

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

En son model dosyası yükleme hakkında daha fazla ayrıntı için lütfen [folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py) sayfasına bakın

## Girişler

| Parametre     | Veri Tipi     | Açıklama |
|---------------|---------------|-------------|
| `clip_adı`   | COMBO[STRING] | Yüklenecek CLIP modelinin adını belirtir. Bu ad, model dosyasını önceden tanımlanmış bir dizin yapısı içinde bulmak için kullanılır. |
| `tür`        | COMBO[STRING] | Yüklenecek CLIP modelinin türünü belirler. ComfyUI daha fazla modeli destekledikçe, buraya yeni türler eklenecektir. Ayrıntılar için lütfen [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py) dosyasındaki `CLIPLoader` sınıf tanımına bakın. |
| `cihaz`      | COMBO[STRING] | CLIP modelini yüklemek için kullanılacak cihazı seçin. `default` modeli GPU üzerinde çalıştırır, `CPU` seçmek ise modelin CPU üzerinde yüklenmesini zorlar. |

### Cihaz Seçenekleri Açıklaması

**"default" ne zaman seçilmeli:**

- Yeterli GPU belleğiniz varsa
- En iyi performansı istiyorsanız
- Sistemin bellek kullanımını otomatik olarak optimize etmesine izin vermek istiyorsanız

**"cpu" ne zaman seçilmeli:**

- Yetersiz GPU belleği durumunda
- GPU belleğini diğer modeller (UNet gibi) için ayırmak gerektiğinde
- Düşük VRAM ortamında çalışırken
- Hata ayıklama veya özel amaçlı ihtiyaçlar için

**Performans Etkisi**

CPU üzerinde çalıştırmak GPU'dan çok daha yavaş olacaktır, ancak diğer daha önemli model bileşenleri için değerli GPU belleğini koruyabilir. Bellek kısıtlı ortamlarda, CLIP modelini CPU'ya koymak yaygın bir optimizasyon stratejisidir.

### Desteklenen Kombinasyonlar

| Model Türü | Karşılık Gelen Kodlayıcı |
|------------|---------------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

ComfyUI güncellendikçe, bu kombinasyonlar genişleyebilir. Ayrıntılar için lütfen [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py) dosyasındaki `CLIPLoader` sınıf tanımına bakın

## Çıkışlar

| Parametre | Veri Tipi | Açıklama |
|-----------|-----------|-------------|
| `clip`    | CLIP      | Yüklenen CLIP modeli, aşağı akış görevlerinde kullanıma veya daha fazla işleme hazır. |

## Ek Notlar

CLIP modelleri, ComfyUI'da metin kodlayıcılar olarak çekirdek bir rol oynar ve metin istemlerini difüzyon modellerinin anlayabileceği sayısal temsillere dönüştürmekten sorumludur. Onları birer çevirmen olarak düşünebilirsiniz; metninizi büyük modellerin anlayabileceği bir dile çevirmekle görevlidirler. Tabii ki, farklı modellerin kendi "lehçeleri" olduğundan, metin kodlama sürecini tamamlamak için farklı mimariler arasında farklı CLIP kodlayıcılarına ihtiyaç duyulur.