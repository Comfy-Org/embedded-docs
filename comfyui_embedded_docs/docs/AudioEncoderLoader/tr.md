# SesKodlayıcıYükleyici

AudioEncoderLoader düğümü, ses kodlayıcılar klasörünüzdeki bir dosyadan bir ses kodlayıcı modeli yükler. Girdi olarak ses kodlayıcı modelinin dosya adını alır ve yüklenen modeli döndürür; bu model daha sonra iş akışınızda ses işleme görevleri için kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ses_kodlayıcı_adı` | Yüklenecek ses kodlayıcı model dosyasını seçer | COMBO | Evet | audio_encoders klasöründe bulunan mevcut ses kodlayıcı dosyalarının listesi |

Not: Seçilen dosya geçerli bir ses kodlayıcı modeli içermiyorsa, düğüm bir hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio_encoder` | Ses işleme iş akışlarında kullanıma hazır, yüklenmiş ses kodlayıcı modeli | AUDIO_ENCODER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/tr.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`
