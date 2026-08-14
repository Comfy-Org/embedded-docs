# LtxApi25ImageToVideo

Bu düğüm, bir başlangıç görüntüsüne dayalı olarak profesyonel kalitede bir video üretir. LTX 2.5 model çeşidini seçebilir, videoyu bir metin istemiyle tanımlayabilir, süreyi, çözünürlüğü, kare hızını ve ses üretimini ayarlayabilir ve isteğe bağlı olarak bir son kare sağlayabilirsiniz. Çıktı, sağlanan görüntüden başlayan bir videodur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Video için kullanılacak ilk kare. | IMAGE | Evet | Tam olarak bir görüntü |
| `model` | Model ayarları grubu. Kullanılacak LTX 2.5 model çeşidini seçer. | COMBO | Evet | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `model.duration` | Üretilen videonun saniye cinsinden süresi. | INT | Evet | Tam sayı |
| `model.resolution` | Üretilen videonun çözünürlüğü. Kullanılabilir seçenekler seçilen modele bağlı olabilir. | COMBO | Evet | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `model.fps` | Üretilen videonun kare hızı. | INT | Evet | Tam sayı (varsayılan: 25) |
| `model.generate_audio` | Video için ses üretilip üretilmeyeceği. | BOOLEAN | Evet | True<br>False |
| `prompt` | Üretilecek video içeriğinin metin açıklaması. 1 ile 10000 karakter arasında olmalıdır. | STRING | Evet | 1 ila 10000 karakter |
| `seed` | Tekrarlanabilir üretim için tohum değeri. Aynı tohumu aynı ayarlarla kullanmak aynı sonucu üretir. | INT | Evet | Tam sayı (varsayılan: 42) |
| `last_frame` | Video için kullanılacak son kare. | IMAGE | Hayır | Tam olarak bir görüntü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Sağlanan başlangıç görüntüsüne ve üretim ayarlarına dayalı olarak üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`
