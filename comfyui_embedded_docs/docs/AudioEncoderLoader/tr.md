AudioEncoderLoader düğümü, ses kodlayıcılar klasörünüzdeki bir dosyadan ses kodlayıcı modeli yükler. Girdi olarak bir ses kodlayıcı modelinin dosya adını alır ve yüklenen modeli döndürür; bu model daha sonra iş akışınızda ses işleme görevleri için kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses_kodlayıcı_adı` | Hangi ses kodlayıcı model dosyasının yükleneceğini seçer | STRING | Evet | audio_encoders klasöründeki mevcut ses kodlayıcı dosyalarının listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio_encoder` | Yüklenen ses kodlayıcı modeli, ses işleme iş akışlarında kullanıma hazırdır | AUDIO_ENCODER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/tr.md)

---
**Source fingerprint (SHA-256):** `24cbd45198db7d950633358c29de57f56c999bc33534fabe80404528d194163c`
