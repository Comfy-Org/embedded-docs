> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/tr.md)

ComfyUI Kling Metinden Videoya Düğümü, metin açıklamalarını video içeriğine dönüştürür. Metin istemlerini alır ve belirtilen yapılandırma ayarlarına göre karşılık gelen video dizilerini oluşturur. Düğüm, farklı en boy oranlarını ve üretim modlarını destekleyerek çeşitli süre ve kalitede videolar üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Olumlu metin istemi |
| `negative_prompt` | STRING | Evet | - | Olumsuz metin istemi |
| `cfg_scale` | FLOAT | Hayır | 0.0 ile 1.0 arası | Yapılandırma ölçek değeri (varsayılan: 1.0) |
| `aspect_ratio` | COMBO | Hayır | KlingVideoGenAspectRatio seçenekleri | Video en boy oranı ayarı (varsayılan: "16:9") |
| `mode` | COMBO | Hayır | Birden çok seçenek mevcut | Video oluşturma için kullanılacak yapılandırma. Biçim: mod / süre / model_adı. (varsayılan: modes[8]) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video çıktısı |
| `video_id` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan videonun süre bilgisi |

---
**Source fingerprint (SHA-256):** `467f89a47890bfbfe6cebac8897fef3bce37d888d3419b248d13be89bed442f3`
