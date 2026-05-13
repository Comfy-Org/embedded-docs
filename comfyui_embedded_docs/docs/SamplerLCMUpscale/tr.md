> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/tr.md)

SamplerLCMUpscale düğümü, Gizli Tutarlılık Modeli (LCM) örneklemesini görüntü büyütme yetenekleriyle birleştiren özel bir örnekleme yöntemi sunar. Çeşitli enterpolasyon yöntemleri kullanarak örnekleme işlemi sırasında görüntüleri büyütmenize olanak tanır; bu da görüntü kalitesini korurken daha yüksek çözünürlüklü çıktılar üretmek için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ölçek_oranı` | FLOAT | Hayır | 0.1 - 20.0 | Büyütme sırasında uygulanacak ölçekleme faktörü (varsayılan: 1.0) |
| `ölçek_adımları` | INT | Hayır | -1 - 1000 | Büyütme işlemi için kullanılacak adım sayısı. Otomatik hesaplama için -1 kullanın (varsayılan: -1) |
| `büyütme_yöntemi` | COMBO | Evet | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" | Görüntüyü büyütmek için kullanılan enterpolasyon yöntemi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme hattında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi döndürür |

---
**Source fingerprint (SHA-256):** `fe0d4c8676454a9e8ecf4bb4e149c9b5e22083322447749116d624984d75e73c`
