# LTX 2.5 Görselden Videoya

Bu düğüm, bir LTX 2.5 modeli kullanarak başlangıç görüntüsünden profesyonel kalitede bir video üretir. Video içeriğini bir metin istemiyle tanımlar, bir model varyantı seçer ve süre, çözünürlük, kare hızı ve ses üretimini ayarlarsınız. Videonun sonunu tanımlamak için isteğe bağlı bir son kare sağlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görsel` | Video için kullanılacak ilk kare. | IMAGE | Evet | Tam olarak bir görüntü |
| `model` | Model ayarları grubu. Kullanılacak LTX 2.5 model varyantını seçer. | COMBO | Evet | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `süre` | Üretilen videonun saniye cinsinden uzunluğu. | INT | Evet | Tam sayı |
| `çözünürlük` | Üretilen videonun çözünürlüğü. Kullanılabilir seçenekler seçilen modele bağlı olarak değişebilir. | COMBO | Evet | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `fps` | Üretilen videonun kare hızı. | INT | Evet | Tam sayı (varsayılan: 25) |
| `ses_oluştur` | Video için ses üretilip üretilmeyeceği. | BOOLEAN | Evet | True<br>False (varsayılan: True) |
| `prompt` | Üretilecek video içeriğinin metin açıklaması. 1 ile 10000 karakter arasında olmalıdır. | STRING | Evet | 1 ila 10000 karakter |
| `tohum` | Tekrarlanabilir üretim için tohum değeri. Aynı ayarlarla aynı tohumun kullanılması aynı sonucu üretir. | INT | Evet | Tam sayı (varsayılan: 42) |
| `son_kare` | Video için kullanılacak son kare. | IMAGE | Hayır | Tam olarak bir görüntü |

**Not:** `image` için yalnızca bir görüntü desteklenir. `last_frame` sağlanmışsa, o da tam olarak bir görüntü içermelidir. Kullanılabilir `model.resolution` seçenekleri, seçilen `model` varyantına bağlı olarak değişebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Sağlanan başlangıç görüntüsüne ve üretim ayarlarına göre üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`
