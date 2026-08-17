# Kling Metinden Videoya

Kling Text to Video Düğümü, Kling video oluşturma hizmetini kullanarak metin istemlerini kısa video kliplerine dönüştürür. Pozitif ve negatif istemlerin yanı sıra en boy oranı, yapılandırma ölçeği ve oluşturma modu gibi ayarları sağlarsınız; düğüm, oluşturulan videoyu tanımlayıcısı ve süresiyle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | İstenen video içeriğini tanımlayan pozitif metin istemi. Çok satırlı giriş. Boş olamaz. | STRING | Evet | Maximum 2500 characters |
| `negative_prompt` | Videoda kaçınılması gerekenleri tanımlayan negatif metin istemi. Çok satırlı giriş. Boş bırakılabilir. | STRING | Evet | Maximum 2500 characters |
| `cfg_scale` | Videonun istemi ne kadar yakından takip edeceğini kontrol eden yapılandırma ölçeği değeri (varsayılan: 1.0). | FLOAT | Hayır | 0.0 to 1.0 |
| `aspect_ratio` | Video en boy oranı ayarı (varsayılan: "16:9"). | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `mode` | Video oluşturma için kullanılacak yapılandırma; format: mod / süre / model_adı (varsayılan: "pro mode / 5s duration / kling-v2-5-turbo"). 5s modunun maliyeti 0,35 USD, 10s modunun maliyeti 0,70 USD. | COMBO | Hayır | `"pro mode / 5s duration / kling-v2-5-turbo"`<br>`"pro mode / 10s duration / kling-v2-5-turbo"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video çıktısı. | VIDEO |
| `video_id` | Oluşturulan videonun benzersiz tanımlayıcısı. | STRING |
| `duration` | Oluşturulan videonun süre bilgisi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
