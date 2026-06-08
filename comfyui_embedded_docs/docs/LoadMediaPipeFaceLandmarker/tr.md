# MediaPipe Yüz İşaretçisi Yükleme Düğümü

## Genel Bakış

Bu düğüm, görüntülerdeki yüzleri ve yüz işaretlerini (gözler, burun ve ağız gibi) tespit edebilen bir MediaPipe Yüz İşaretçisi v2 modelini yükler. Yüz analizi için iki algılama varyantı (kısa menzil ve tam menzil) ile paylaşılan ağ verileri, şekil karıştırma verileri ve kanonik geometri içerir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | `models/detection/` dizininden yüz algılama modeli. | STRING | Evet | `models/detection/` dizinindeki mevcut modellerin listesi |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `FACE_DETECTION_MODEL` | Her iki algılama varyantını (kısa/tam), yüz topolojisi için bağlantı kümelerini, kanonik verileri ve GPU yönetimi için model yamaçlarını içeren yüklenmiş bir FaceLandmarker model nesnesi. | FACE_DETECTION_MODEL |

**Not:** Çıkış, diğer düğümler tarafından yüz algılama ve işaret çıkarma görevleri için kullanılabilen karmaşık bir nesnedir. "short" (yakın mesafe algılama) ve "full" (tam mesafe algılama) olmak üzere iki algılama varyantı içerir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/tr.md)

---
**Source fingerprint (SHA-256):** `b30bf4d04aa06a227f3661c0e1346d3dab3ea1e25d6627fce5b6480198203c26`
