# Wan 3.0 Referanstan Videoya

Bu düğüm, Wan 3.0 modelini kullanarak bir metin isteminden ve isteğe bağlı referans görüntülerden, videolardan ve seslerden bir video oluşturur. Referans medyalar serbestçe birleştirilebilir ve istemde @Image1, @Video1 ve @Audio1 olarak belirtilebilir. Düğüm, üretim isteğini Wan API'sine gönderir ve tamamlanmış videoyu döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak Wan 3.0 model çeşidini seçer. | DYNAMIC_COMBO | Evet | `wan3.0-video`<br>`wan3.0-video-prime` |
| `seed` | Üretim için kullanılacak tohum (seed). Varsayılan: 42. | INT | Evet | 0 ila 2147483647 |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği. Varsayılan: false. | BOOLEAN | Evet | true<br>false |

### wan3.0-video ve wan3.0-video-prime Girdileri

Her iki model seçeneği de aynı parametre kümesini paylaşır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince desteklenir. Bağlı referans medyaları istemde @Image1, @Video1 ve @Audio1 olarak belirtin; her tür için girdi sırasına göre numaralandırılır. Varsayılan: boş. | STRING | Evet | 20.000 karaktere kadar |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Çıktı videosunun en-boy oranı. "adaptive" ile çıktı boyutları girdi medyasından türetilir. | COMBO | Evet | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Çıktı süresi saniye cinsinden. "auto" ile model, isteme ve referans medyaya uygun bir süre seçer. Referans videoların ve çıktının toplam süresi 30 saniyeyi aşmamalıdır. | COMBO | Evet | "auto"<br>"2" ila "30" (tam sayı saniye) |
| `audio` | Çıktı videosunun bir ses parçası içerip içermediği. Varsayılan: true. | BOOLEAN | Evet | true<br>false |
| `prompt_extend` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği. Varsayılan: true. | BOOLEAN | Evet | true<br>false |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: 1 ila 10 referans görüntü bağlayın. Referanslar girdi sırasına göre image1'den image10'a kadar numaralandırılır. | IMAGE | Hayır | 0 ila 10 görüntü |
| `reference_videos` | Genişletilebilir yuva: 1 ila 5 referans video bağlayın. Referanslar girdi sırasına göre video1'den video5'e kadar numaralandırılır. | VIDEO | Hayır | 0 ila 5 video |
| `reference_audios` | Genişletilebilir yuva: 1 ila 5 referans ses klibi bağlayın. Referanslar girdi sırasına göre audio1'den audio5'e kadar numaralandırılır. | AUDIO | Hayır | 0 ila 5 ses klibi |

**Kısıtlamalar:**

- İstem en az bir boş olmayan karakter içermeli veya en az bir referans görüntü, video ya da ses girdisi bağlanmış olmalıdır.
- İstemdeki referans etiketleri bağlı girdilerle eşleşmelidir. Örneğin, @Image1 bağlanan ilk referans görüntüyü, @Video2 bağlanan ikinci referans videoyu ve @Audio1 bağlanan ilk referans sesi ifade eder. Etiketler her tür için girdi sırasına göre ayrı ayrı numaralandırılır.
- Bağlanan her referans görüntü, bir yığın (batch) değil, tam olarak tek bir görüntü içermelidir.
- Her referans video 15 saniye veya daha kısa olmalıdır. Tüm referans videoların toplam süresi 15 saniyeyi aşmamalıdır.
- Her referans ses 15 saniye veya daha kısa olmalıdır. Tüm referans seslerin toplam süresi 15 saniyeyi aşmamalıdır.
- `duration` "auto" olmadığında, tüm referans videoların toplam süresi artı seçilen çıktı süresi 30 saniyeyi aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. `audio` parametresi etkinleştirildiğinde bir ses parçası içerir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ReferenceToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `09caa8142d71235417a3dfc5676c5f6accc2af1287fad3b7050844dd9453cc64`
