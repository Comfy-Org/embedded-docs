# Kare Enterpolasyon Modeli Yükle

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek bir kare interpolasyon modeli seçin. Modeller 'frame_interpolation' klasörüne yerleştirilmelidir. | COMBO | Evet | `frame_interpolation` klasöründeki model dosyalarının listesi |

Not: Düğüm, FILM ve RIFE model biçimlerini destekler. Seçilen dosya tanınan bir biçim değilse bir hata oluşturulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | Yüklenen ve yapılandırılan kare interpolasyon modeli, diğer düğümlerde kullanıma hazırdır. | INTERP_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/tr.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
