> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/tr.md)

AudioAdjustVolume düğümü, desibel cinsinden ses ayarlamaları uygulayarak sesin yüksekliğini değiştirir. Bir ses girişi alır ve belirtilen ses seviyesine dayalı olarak bir kazanç faktörü uygular; burada pozitif değerler sesi artırırken negatif değerler azaltır. Düğüm, orijinaliyle aynı örnekleme hızına sahip olarak değiştirilmiş sesi döndürür.

## Girişler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `audio` | AUDIO | gerekli | - | - | İşlenecek ses girişi |
| `volume` | INT | gerekli | 1.0 | -100 ile 100 | Desibel (dB) cinsinden ses ayarı. 0 = değişiklik yok, +6 = iki katına çıkar, -6 = yarıya indirir, vb. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Ses seviyesi ayarlanmış olarak işlenmiş ses |