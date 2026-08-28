# WanDancerEncodeAudio

Bu düğüm, bir video üretim modelini yönlendirmek için kullanılabilecek özellikleri çıkarmak amacıyla bir ses girdisini işler. Sesi analiz ederek tempo, ritim ve diğer müzikal özellikleri tespit eder ve bu bilgiyi bir video modelini koşullandırmaya uygun bir biçime paketler; böylece üretilen videonun ses ile senkronize edilmesini sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Analiz edilecek ve kodlanacak ses girdisi. Seste birden fazla kanal varsa, özellik çıkarımından önce kanallar monoya indirgenerek ortalaması alınır. | AUDIO | Evet | - |
| `video_kareleri` | Hedef videodaki kare sayısı. Senkronizasyon için kare hızının hesaplanmasında kullanılır (varsayılan: 149). | INT | Evet | Min: 1, Max: 268435456 (MAX_RESOLUTION), Step: 4 |
| `ses_enjeksiyon_ölçeği` | Ses özelliklerinin video modeline enjekte edilirken kullanılan ölçeği (varsayılan: 1.0). | FLOAT | Evet | Min: 0.0, Max: 10.0, Step: 0.01 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ses_kodlayıcı_çıktısı` | İşlenmiş ses özelliklerini, hesaplanan kare hızını (fps) ve ses enjeksiyon ölçeğini içeren bir sözlük. Bu çıktı, video üretim modelini koşullandırmak için kullanılır. | AUDIO_ENCODER_OUTPUT |
| `fps_dizgesi` | Ses uzunluğuna ve video kare sayısına göre hesaplanan kare hızını (fps) açıklayan bir metin dizesi. Bu dize, video modeli için istemde kullanılmak üzere tasarlanmıştır. Referans işlem hattına uyum sağlamak için Çince biçimlendirilmiştir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
