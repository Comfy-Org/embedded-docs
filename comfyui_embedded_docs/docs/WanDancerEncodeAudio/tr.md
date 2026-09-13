# WanDancerEncodeAudio

Bu düğüm bir ses klibini analiz eder ve onu bir video üretim modeline yön verebilecek bir dizi özelliğe dönüştürür. Tempo ve vuruşları tahmin eder; mel-spektrogram, MFCC, kroma ve onset özelliklerini çıkarır, ardından bunları senkronizasyon için hesaplanan kare hızıyla birlikte paketler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Analiz edilecek ve kodlanacak ses girdisi. Ses birden çok kanala sahipse, özellik çıkarımından önce kanalların ortalaması alınarak mono hale getirilir. | AUDIO | Evet | - |
| `video_kareleri` | Hedef videodaki kare sayısı. Senkronizasyon için kare hızını hesaplamak üzere kullanılır (varsayılan: 149). | INT | Evet | Min: 1, Maks: 16384 (MAX_RESOLUTION), Adım: 4 |
| `ses_enjeksiyon_ölçeği` | Ses özelliklerinin video modeline enjekte edilirken kullanılacak ölçek (varsayılan: 1.0). | FLOAT | Evet | Min: 0.0, Maks: 10.0, Adım: 0.01 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio_encoder_output` | İşlenmiş ses özelliklerini, hesaplanan kare hızını (fps) ve ses enjeksiyon ölçeğini içeren bir sözlük. Bu çıktı, video üretim modelini koşullandırmak için kullanılır. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Ses uzunluğuna ve video kare sayısına göre hesaplanan kare hızını (fps) açıklayan bir metin dizesi. Bu dizenin, video modeli için istemde kullanılması amaçlanmıştır. Referans işlem hattıyla eşleşmesi için Çince biçimlendirilmiştir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
