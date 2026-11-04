# Pika Music

Bu düğüm, Pika ile bir metin açıklamasından ve isteğe bağlı şarkı sözlerinden müzik üretir veya sağladığınız bir şarkının cover'ını oluşturur. Belirlediğiniz uzunlukta yeni bir şarkı yazmak için `"text to music"` seçeneğini, bir şarkıyı yeniden kaydedip uzunluğunu korumak için `"cover"` seçeneğini kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mode` | Düğümün ne yaptığı: `"text to music"` yeni bir şarkı yazar, `"cover"` sağlanan bir şarkıyı yeniden kaydeder. Her mod aşağıda kendi girdilerini gösterir. Varsayılan: `"text to music"`. | DYNAMIC_COMBO | Evet | `"text to music"`<br>`"cover"` |

### Metinden Müziğe Girdileri

Bu girdiler `mode` değeri `"text to music"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Müziğin nasıl kulağa gelmesi gerektiği. Boş olamaz. Varsayılan: "" (boş dize). | STRING | Evet | 1 ile 4000 karakter arası |
| `lyrics` | İsteğe bağlı şarkı sözleri. `[Verse]` ve `[Chorus]` gibi bölüm etiketlerine izin verilir. Varsayılan: "" (boş dize). | STRING | Evet | 0 ile 8000 karakter arası |
| `duration` | Şarkının saniye cinsinden uzunluğu. Varsayılan: 30.0. | FLOAT | Evet | 10.0 ile 360.0 arası (adım: 0.1) |
| `rewrite_prompt` | Üretimden önce kısa veya belirsiz bir istemi bir modelle genişletin. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `seed` | Örnekleme için tohum. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

### Cover Girdileri

Bu girdiler `mode` değeri `"cover"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `source_audio` | Cover'ı oluşturulacak şarkı. Sonuç aynı uzunluğa sahiptir ve 5 ile 360 saniye aralığına sınırlandırılır. | AUDIO | Evet | - |
| `prompt` | Cover'ın nasıl kulağa gelmesi gerektiği. Boş olamaz. Varsayılan: "" (boş dize). | STRING | Evet | 1 ile 4000 karakter arası |
| `lyrics` | İsteğe bağlı şarkı sözleri. `[Verse]` ve `[Chorus]` gibi bölüm etiketlerine izin verilir. Varsayılan: "" (boş dize). | STRING | Evet | 0 ile 8000 karakter arası |
| `rewrite_prompt` | Üretimden önce kısa veya belirsiz bir istemi bir modelle genişletin. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `seed` | Örnekleme için tohum. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlar:**

* İstem 1 ile 4000 karakter arasında olmalı ve şarkı sözleri 8000 karakter veya daha az olmalıdır.
* Cover modu `duration` değerini yok sayar: çıktı, `source_audio` uzunluğuyla eşleşir ve 5 ile 360 saniye aralığına sınırlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `AUDIO` | Üretilen şarkı veya sağlanan parçanın cover'ı. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaMusicNode/tr.md)

---
**Source fingerprint (SHA-256):** `e3051b2d0cfff72cf7e359d7383f4e0d133df0338ff42a00f0649387f504ec28`
