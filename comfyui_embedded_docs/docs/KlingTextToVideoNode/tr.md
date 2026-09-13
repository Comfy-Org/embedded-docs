# Kling Metinden Videoya

Kling Text to Video düğümü, Kling video oluşturma API'sini kullanarak metin açıklamalarından videolar oluşturur. İstemi ve ayarları (en-boy oranı, oluşturma modu ve CFG ölçeği) API'ye gönderir, oluşturma görevinin tamamlanmasını bekler ve ardından elde edilen videoyu kimliği ve süresiyle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Pozitif metin istemi | STRING | Evet | Maksimum 2500 karakter |
| `negative_prompt` | Negatif metin istemi | STRING | Hayır | Maksimum 2500 karakter |
| `cfg_scale` | Videonun istemi ne kadar yakından takip edeceğini kontrol eden yapılandırma ölçeği değeri (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ile 1.0 |
| `aspect_ratio` | Video en-boy oranı ayarı (varsayılan: "16:9") | COMBO | Hayır | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | Video oluşturma için kullanılacak yapılandırma, şu biçime göre: mode / duration / model_name (varsayılan: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Hayır | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

Not: `prompt` parametresi gereklidir ve boş olmamalıdır. Hem `prompt` hem de `negative_prompt` en fazla 2500 karakterle sınırlıdır. 10 saniyelik `mode` seçeneği, 5 saniyelik seçenekten daha pahalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video çıktısı | VIDEO |
| `video_id` | Oluşturulan videonun benzersiz tanımlayıcısı | STRING |
| `duration` | Oluşturulan videonun süre bilgisi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
