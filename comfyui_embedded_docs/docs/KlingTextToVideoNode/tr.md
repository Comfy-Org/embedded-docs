# Kling Metinden Videoya

Kling Metinden Video düğümü, Kling video üretim API'sini kullanarak metin açıklamalarından videolar üretir. İstemi (prompt) ve ayarları (en-boy oranı, üretim modu ve CFG ölçeği) API'ye gönderir, üretim görevinin tamamlanmasını bekler ve ardından oluşan videoyu kimliği ve süresiyle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | İstenen video içeriğini tanımlayan olumlu metin istemi | STRING | Evet | Maksimum 2500 karakter |
| `negatif_istem` | Videoda kaçınılması gerekenleri tanımlayan olumsuz metin istemi | STRING | Hayır | Maksimum 2500 karakter |
| `cfg_ölçeği` | Videonun istemi ne kadar yakından takip ettiğini kontrol eden yapılandırma ölçeği değeri (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ile 1.0 arası |
| `en_boy_oranı` | Video en-boy oranı ayarı (varsayılan: "16:9") | COMBO | Hayır | "16:9"<br>"9:16"<br>"1:1" |
| `mod` | Şu biçimi izleyen video üretimi için kullanılacak yapılandırma: mode / duration / model_name (varsayılan: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Hayır | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

Not: `prompt` parametresi gereklidir ve boş bırakılmamalıdır. Hem `prompt` hem de `negative_prompt` en fazla 2500 karakterle sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `output` | Üretilen video çıktısı | VIDEO |
| `video_kimliği` | Üretilen video için benzersiz tanımlayıcı | STRING |
| `süre` | Üretilen videonun süre bilgisi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
