# ByteDance Seed

ByteDance'ın Seed 2.0 modellerini kullanarak metin yanıtları oluşturun. Bir metin istemi sağlayın ve isteğe bağlı olarak çok modlu bağlam için görüntü veya videolar ekleyin.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan Seed modeli. | DYNAMIC_COMBO | Evet | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | Modele metin girişi. (varsayılan: "") | STRING | Evet | N/A |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerine bakılmaksızın deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır | N/A |

### Model Girdileri (Seed 2.0 Pro, Seed 2.0 Lite ve Seed 2.0 Mini için ortaktır)

Seçildiklerinde her üç Seed modeli de aynı alt parametreleri kullanıma sunar.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `temperature` | Rastgeleliği kontrol eder. 0.0 deterministiktir, daha yüksek değerler daha rastgeledir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 2.0 (step: 0.01) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Model için bağlam olarak kullanılabilecek isteğe bağlı görüntü(ler). En fazla 20 görüntü. Büyütülebilir yuva: 1..20 öğe bağlayın, örn. `image_1` ile `image_20` arası. | IMAGE | Hayır | 0 ile 20 images |
| `videos` | Model için bağlam olarak kullanılabilecek isteğe bağlı video(lar). En fazla 4 video. Büyütülebilir yuva: 1..4 öğe bağlayın, örn. `video_1` ile `video_4` arası. | VIDEO | Hayır | 0 ile 4 videos |

**Not:** `model` parametresi, bir model seçildiğinde referans ve sıcaklık alt parametrelerini kullanıma sunan dinamik bir açılır listedir. Bu parametreye görüntü ve video girdilerini bağlayarak çok modlu bağlam sağlayabilirsiniz. İstek başına en fazla 20 görüntü ve 4 video desteklenir ve `prompt` zorunludur ve en az bir boşluk olmayan karakter içermelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Seed modelinden oluşturulan metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/tr.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
