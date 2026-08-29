# SAM3D Body Modelini Yükle

SAM3D Body modelini, algılama klasöründe saklanan bir checkpoint dosyasından yükler ve 3D gövde algılama kullanımına hazırlar. Düğüm, model ağırlıklarını yükler, varsa niceleme ayarlarını algılar ve uygular, ardından otomatik bellek yönetimi için modeli sarar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_file` | Yüklenecek SAM3D Body checkpoint dosyası. Dosya, algılama klasörüne yerleştirilmelidir. | COMBO | Evet | Algılama klasöründe bulunan tüm model dosyaları |

Not: Model dosyası algılama klasöründe bulunmalıdır. Checkpoint'in durum sözlüğü anahtarları SAM3D Body model yapısıyla eşleşmezse yükleme bir hatayla başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `sam3d_body_model` | Yüklenen SAM3D Body modeli; GPU ve CPU arasında otomatik bellek yönetimi için sarılmıştır. El algılama ağırlıkları kaldırılmıştır, bu nedenle model yalnızca gövde algılamaya özelleşmiştir. | SAM3D_BODY_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Loader/tr.md)

---
**Source fingerprint (SHA-256):** `c66a1639b5f19dafcfb1466d68908969a4d33ab0d01c30e8b31d1f1ce41fd782`
