> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/tr.md)

AudioEncoderLoader düğümü, ses kodlayıcılar klasörünüzdeki bir dosyadan ses kodlayıcı modeli yükler. Girdi olarak bir ses kodlayıcı modelinin dosya adını alır ve yüklenen modeli döndürür; bu model daha sonra iş akışınızda ses işleme görevleri için kullanılabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses_kodlayıcı_adı` | STRING | Evet | audio_encoders klasöründeki mevcut ses kodlayıcı dosyalarının listesi | Hangi ses kodlayıcı model dosyasının yükleneceğini seçer |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Yüklenen ses kodlayıcı modeli, ses işleme iş akışlarında kullanıma hazırdır |

---
**Source fingerprint (SHA-256):** `24cbd45198db7d950633358c29de57f56c999bc33534fabe80404528d194163c`
