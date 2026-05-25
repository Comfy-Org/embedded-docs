> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/tr.md)

# MediaPipe Yüz İşaretçisi Yükleme Düğümü

## Genel Bakış

Bu düğüm, görüntülerdeki yüzleri ve yüz işaretlerini (gözler, burun ve ağız gibi) tespit edebilen bir MediaPipe Yüz İşaretçisi v2 modelini yükler. Yüz analizi için iki algılama varyantı (kısa menzil ve tam menzil) ile paylaşılan ağ verileri, şekil karıştırma verileri ve kanonik geometri içerir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model_name` | STRING | Evet | `models/detection/` dizinindeki mevcut modellerin listesi | `models/detection/` dizininden yüz algılama modeli. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `FACE_DETECTION_MODEL` | FACE_DETECTION_MODEL | Her iki algılama varyantını (kısa/tam), yüz topolojisi için bağlantı kümelerini, kanonik verileri ve GPU yönetimi için model yamaçlarını içeren yüklenmiş bir FaceLandmarker model nesnesi. |

**Not:** Çıkış, diğer düğümler tarafından yüz algılama ve işaret çıkarma görevleri için kullanılabilen karmaşık bir nesnedir. "short" (yakın mesafe algılama) ve "full" (tam mesafe algılama) olmak üzere iki algılama varyantı içerir.

---
**Source fingerprint (SHA-256):** `b30bf4d04aa06a227f3661c0e1346d3dab3ea1e25d6627fce5b6480198203c26`
