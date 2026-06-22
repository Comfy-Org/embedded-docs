# Magnific Görsel Yeniden Işıklandırma

**Giriş**

Magnific Image Relight düğümü, bir girdi görüntüsünün aydınlatmasını ayarlar. Bir metin istemine dayalı olarak stilistik aydınlatma uygulayabilir veya isteğe bağlı bir referans görüntüden aydınlatma özelliklerini aktarabilir. Düğüm, nihai çıktının parlaklığına, kontrastına ve genel havasına ince ayar yapmak için çeşitli kontroller sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Aydınlatılacak görüntü. Tam olarak bir görüntü gereklidir. Minimum boyutlar 160x160 pikseldir. En-boy oranı 1:3 ile 3:1 arasında olmalıdır. | IMAGE | Evet | Yok |
| `prompt` | Aydınlatma için tanımlayıcı yönlendirme. Vurgu notasyonunu destekler (1-1.4). Varsayılan boş bir dizedir. | STRING | Hayır | Yok |
| `light_transfer_strength` | Işık aktarımı uygulamasının yoğunluğu. Varsayılan: 100. | INT | Evet | 0 ile 100 |
| `style` | Stilistik çıktı tercihi. | COMBO | Evet | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` |
| `interpolate_from_original` | Orijinale daha yakın eşleşmesi için üretim özgürlüğünü kısıtlar. Varsayılan: False. | BOOLEAN | Evet | Yok |
| `change_background` | İstem/referansa göre arka planı değiştirir. Varsayılan: True. | BOOLEAN | Evet | Yok |
| `preserve_details` | Orijinalden doku ve ince ayrıntıları korur. Varsayılan: True. | BOOLEAN | Evet | Yok |
| `advanced_settings` | Gelişmiş aydınlatma kontrolü için ince ayar seçenekleri. `"enabled"` olarak ayarlandığında ek parametreler kullanılabilir hale gelir. | DYNAMICCOMBO | Evet | `"disabled"`<br>`"enabled"` |
| `reference_image` | Aydınlatmanın aktarılacağı isteğe bağlı referans görüntü. Sağlanırsa tam olarak bir görüntü gereklidir. Minimum boyutlar 160x160 pikseldir. En-boy oranı 1:3 ile 3:1 arasında olmalıdır. | IMAGE | Hayır | Yok |

**Gelişmiş Ayarlar Hakkında Not:** `advanced_settings` `"enabled"` olarak ayarlandığında, aşağıdaki iç içe parametreler etkinleşir:

* `whites`: Görüntüdeki en parlak tonları ayarlar. Aralık: 0 ile 100. Varsayılan: 50.
* `blacks`: Görüntüdeki en koyu tonları ayarlar. Aralık: 0 ile 100. Varsayılan: 50.
* `brightness`: Genel parlaklık ayarı. Aralık: 0 ile 100. Varsayılan: 50.
* `contrast`: Kontrast ayarı. Aralık: 0 ile 100. Varsayılan: 50.
* `saturation`: Renk doygunluğu ayarı. Aralık: 0 ile 100. Varsayılan: 50.
* `engine`: İşleme motoru seçimi. Seçenekler: `"automatic"`, `"balanced"`, `"cool"`, `"real"`, `"illusio"`, `"fairy"`, `"colorful_anime"`, `"hard_transform"`, `"softy"`.
* `transfer_light_a`: Işık aktarımının yoğunluğu. Seçenekler: `"automatic"`, `"low"`, `"medium"`, `"normal"`, `"high"`, `"high_on_faces"`.
* `transfer_light_b`: Ayrıca ışık aktarım yoğunluğunu değiştirir. Çeşitli efektler için önceki kontrollerle birleştirilebilir. Seçenekler: `"automatic"`, `"composition"`, `"straight"`, `"smooth_in"`, `"smooth_out"`, `"smooth_both"`, `"reverse_both"`, `"soft_in"`, `"soft_out"`, `"soft_mid"`, `"style_shift"`, `"strong_shift"`.
* `fixed_generation`: Aynı ayarlarla tutarlı çıktı sağlar. Varsayılan: True.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Yeniden aydınlatılmış görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/tr.md)

---
**Source fingerprint (SHA-256):** `c260b7c88a267a20fdea7f436404fe96ede782bc522ab29da36e94c20f7330cd`
