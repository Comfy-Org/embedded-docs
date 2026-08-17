# WanDancerEncodeAudio

Bu düğüm, bir video üretim modelini yönlendirmek için kullanılabilecek özellikleri çıkarmak amacıyla bir ses girdisini işler. Tempoyu, vuruşları ve diğer müzikal özellikleri tespit etmek için sesi analiz eder ve ardından bu bilgiyi bir video modelini koşullandırmaya uygun bir biçime paketleyerek üretilen videonun sesle senkronize edilmesini sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `audio` | Analiz edilecek ve kodlanacak ses girdisi. | AUDIO | Evet | - |
| `video_frames` | Hedef videodaki kare sayısı. Senkronizasyon için kare hızını hesaplamak amacıyla kullanılır (varsayılan: 149). | INT | Evet | Min: 1, Max: 268435456 (MAX_RESOLUTION), Step: 4 |
| `audio_inject_scale` | Video modeline enjekte edilirken ses özelliklerinin ölçeği (varsayılan: 1.0). | FLOAT | Evet | Min: 0.0, Max: 10.0, Step: 0.01 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio_encoder_output` | İşlenmiş ses özelliklerini, hesaplanan kare hızını (fps) ve ses enjeksiyon ölçeğini içeren bir sözlük. Bu çıktı, video üretim modelini koşullandırmak için kullanılır. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Ses uzunluğuna ve video karesi sayısına göre hesaplanan kare hızını (fps) tanımlayan bir metin dizesi. Bu dize, video modeli için promptta kullanılmak üzere tasarlanmıştır. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
