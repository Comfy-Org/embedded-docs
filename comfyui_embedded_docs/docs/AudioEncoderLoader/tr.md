# SesKodlayıcıYükleyici

## Genel Bakış

AudioEncoderLoader düğümü, `audio_encoders` klasöründe depolanan bir dosyadan ses kodlayıcı modeli yükler. Girdi olarak bir ses kodlayıcı modeli dosya adını alır ve yüklenen modeli döndürür; bu model daha sonra iş akışınızdaki ses işleme görevleri için kullanılabilir. Seçilen dosya geçerli bir ses kodlayıcı modeli içermiyorsa düğüm bir hata verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | Ses kodlayıcıları klasöründen hangi ses kodlayıcı modeli dosyasının yükleneceğini seçer | COMBO | Evet | `audio_encoders` klasöründeki kullanılabilir ses kodlayıcı dosyalarının listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio_encoder` | Yüklenen ses kodlayıcı modeli; ses işleme iş akışlarında kullanıma hazırdır | AUDIO_ENCODER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/tr.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`
