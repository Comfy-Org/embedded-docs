# Wan22FunControlToVideo

Wan22FunControlToVideo düğümü, Wan video model mimarisini kullanarak video üretimi için koşullama (conditioning) ve gizil (latent) temsilleri hazırlar. Pozitif ve negatif koşullama girdilerini, isteğe bağlı referans görüntüleri ve kontrol videolarıyla birlikte işleyerek video sentezi için gerekli gizil uzay temsillerini oluşturur. Düğüm, video modelleri için uygun koşullama verileri üretmek amacıyla uzamsal ölçekleme ve zamansal boyutları yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini yönlendirmek için pozitif koşullama girdisi | CONDITIONING | Evet | - |
| `negative` | Video üretimini yönlendirmek için negatif koşullama girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosu genişliği piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 - MAX_RESOLUTION |
| `height` | Çıktı videosu yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 - MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 - MAX_RESOLUTION |
| `batch_size` | Oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `ref_image` | Görsel rehberlik sağlamak için isteğe bağlı referans görüntüsü | IMAGE | Hayır | - |
| `control_video` | Üretim sürecini yönlendirmek için isteğe bağlı kontrol videosu | IMAGE | Hayır | - |

**Not:** `length` parametresi 4 karelik parçalar halinde işlenir ve düğüm, gizil uzay için zamansal ölçeklemeyi otomatik olarak yönetir. `ref_image` sağlandığında, referans gizil değerleri aracılığıyla koşullamayı etkiler. `control_video` sağlandığında, koşullamada kullanılan birleştirme (concat) gizil temsilini doğrudan etkiler. `start_image` parametresi bu düğümün şemasında bir girdi olarak sunulmamıştır ancak yürütme mantığında referans alınmıştır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Birleştirme gizili, maske ve isteğe bağlı referans gizillerini içeren, videoya özgü gizil verilerle değiştirilmiş pozitif koşullama | CONDITIONING |
| `negative` | Birleştirme gizili, maske ve isteğe bağlı referans gizillerini içeren, videoya özgü gizil verilerle değiştirilmiş negatif koşullama | CONDITIONING |
| `latent` | Toplu iş boyutu, gizil kanallar ve uzamsal/zamansal ölçeklemeye bağlı olarak video üretimi için uygun boyutlara sahip boş gizil tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `8b24058f06aa9f779371a402c41cffc95d13ad0131d23d1438067d77755c73e2`
