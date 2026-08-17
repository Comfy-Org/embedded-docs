# Kling Görüntüden Videoya

Kling Image to Video Düğümü, metin istemleri kullanarak bir başlangıç referans görüntüsünden video üretir. Görüntüyü ilk kare olarak kullanır ve pozitif ile negatif metin açıklamalarına dayalı olarak, model, süre, üretim modu ve en-boy oranı için yapılandırılabilir seçeneklerle bir video dizisi oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Videoyu üretmek için kullanılan referans görüntü. En az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. | IMAGE | Evet | - |
| `prompt` | Pozitif metin istemi. En fazla 500 karakter. | STRING | Evet | - |
| `negative_prompt` | Negatif metin istemi. En fazla 500 karakter. Boş bırakılabilir. | STRING | Evet | - |
| `model_name` | Video üretimi için kullanılan model (varsayılan: `"kling-v2-5-turbo"`). | COMBO | Evet | `"kling-v2-5-turbo"` |
| `cfg_scale` | Videonun istemi ne kadar yakından takip edeceğini kontrol eder. Daha yüksek değerler daha güçlü bağlılık anlamına gelir (varsayılan: 0.8). | FLOAT | Evet | 0.0 ile 1.0 |
| `mode` | Üretim modu (varsayılan: `"pro"`). | COMBO | Evet | `"pro"` |
| `aspect_ratio` | Üretilen videonun en-boy oranı (varsayılan: `"16:9"`). | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Üretilen videonun saniye cinsinden süresi (varsayılan: `"5"`). | COMBO | Evet | `"5"`<br>`"10"` |

Not: Pozitif istem boş olmamalıdır. Hem pozitif hem de negatif istemler 500 karakterle sınırlıdır. Giriş görüntüsü en az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında bulunmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen video. | VIDEO |
| `video_id` | Üretilen video için benzersiz tanımlayıcı. | STRING |
| `duration` | Üretilen videonun süresi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
