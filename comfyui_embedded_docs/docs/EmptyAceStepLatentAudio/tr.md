# BoşAceAdımGizliSes

Empty Ace Step 1.0 Latent Audio düğümü, seçilen süre için boş latent ses örnekleri oluşturur. Bir grup sessiz (tamamen sıfır) ses latentini doldurur; uzunluk, ses işleme parametreleri kullanılarak `seconds` girdisinden hesaplanır. Bu genellikle başlangıç noktası olarak bir latent gösterimine ihtiyaç duyan ses iş akışlarını başlatmak için kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `seconds` | Sesin saniye cinsinden süresi (varsayılan: 120.0, adım: 0.1) | FLOAT | Evet | 1.0 - 1000.0 |
| `batch_size` | Gruptaki latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Sıfırlarla doldurulmuş boş latent ses örneklerini döndürür. Çıktı, bir `samples` tensörü ve "audio" olarak ayarlanmış bir `type` alanı içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
