# BriaReplaceImageBackground

Bu düğüm, bir görüntünün arka planını Bria tarafından oluşturulan yeni bir arka planla değiştirir. Yeni arka plan bir metin promptu ile tanımlanabilir veya referans görüntülerle yönlendirilebilir. Arka plan öznenin etrafında oluşturulurken öznenin pikselleri korunur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Arka planı değiştirilecek girdi görüntüsü. | IMAGE | Evet | |
| `background` | Yeni arka planı bir prompt ile tanımlayın veya referans görüntülerle yönlendirin. | DYNAMIC_COMBO | Evet | `"prompt"`<br>`"reference images"` |
| `original_quality` | Sonucu yaklaşık 1 megapiksele ölçeklendirmek yerine girdinin tam piksel boyutunu döndürür. Büyük bir girdi bu durumda büyük bir görüntü döndürür. (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |
| `seed` | Aynı seed genellikle aynı arka planı döndürür; otomatik prompt iyileştirmesi yine de bunu değiştirebilir. (varsayılan: 42) | INT | Hayır | 0 - 2147483647 |
| `moderation` | Moderasyon ayarları. (varsayılan: "false") | DYNAMIC_COMBO | Hayır | `"false"`<br>`"true"` |

### Prompt Girdileri

`background` `"prompt"` olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Yeni arka planın açıklaması. #FF5733 gibi bir hex renk kodu düz renkli bir arka plan üretir. En az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | |
| `mode` | `high_control` promptu en yakından takip eder, `base` dengeli varsayılandır ve `fast` hız için ayrıntıdan ödün verir. | COMBO | Evet | `"high_control"`<br>`"base"`<br>`"fast"` |
| `refine_prompt` | Daha iyi sonuçlar için promptu yeniden yazar; bu ayrıca İngilizce olmayan promptları çevirir. Yazıldığı şekilde göndermek için kapatın. (varsayılan: true) | BOOLEAN | Hayır | `true`<br>`false` |

### Referans Görüntü Girdileri

`background` `"reference images"` olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ref_images` | Genişletilebilir yuva: yeni arka planı yönlendiren 1 ile 10 görüntü bağlayın; aynı boyutta olmaları gerekmez. Her referans sonucu değiştirir, bu yüzden birkaç tutarlı referans birçok çelişkili olandan daha iyidir. Toplu bir girdi, her görüntü için bir kez sayılır. | IMAGE | Evet | 1 - 10 görüntü |
| `enhance_ref_images` | Daha iyi sonuçlar için referans görüntülerin ek işlenmesi. (varsayılan: true) | BOOLEAN | Hayır | `true`<br>`false` |

### Moderasyon Girdileri

`moderation` `"true"` olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Prompt içeriği için moderasyonu etkinleştirir. (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_input_moderation` | Görsel girdi için moderasyonu etkinleştirir. (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_output_moderation` | Görsel çıktı için moderasyonu etkinleştirir. (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |

**Not:** `ref_images` girdisi en fazla 10 görüntü kabul eder; 10'dan fazlasının sağlanması bir hata döndürür. `prompt` alanı en az 1 karakter içermelidir. `original_quality` false olduğunda, girdi görüntüsü işlenmeden önce yaklaşık 1 megapiksele küçültülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Yeni arka plana sahip görüntü. | IMAGE |
| `refined_prompt` | Bria'nın ürettiği prompt; referans görüntü yolunda boştur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceImageBackground/tr.md)

---
**Source fingerprint (SHA-256):** `62c29d61983c9656d2ea2954518404c62d76961c3deba0e10d63e787d0b0b106`
