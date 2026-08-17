# MediaPipe Yüz İşaretleyicisini Yükle

Bu düğüm, görüntülerde yüzleri ve yüz işaret noktalarını (gözler, burun ve ağız gibi) algılayabilen bir MediaPipe Face Landmarker v2 modeli yükler. Yüklenen model, yüz analizi için ortak ağ verisi, karışım şekilleri (blendshapes) ve kanonik geometrinin yanı sıra iki algılama varyantı (kısa ve tam) içerir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | models/detection/ dizinindeki yüz algılama modeli. | COMBO | Evet | `models/detection/` dizinindeki mevcut modellerin listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | Yüklenmiş MediaPipe Face Landmarker model nesnesi; hem algılama varyantlarını (kısa/tam), ortak ağ ve karışım şekli verilerini, kanonik geometriyi, yüz topolojisi bağlantı kümelerini ve GPU yönetimi için model yamalayıcılarını içerir. | FACE_DETECTION_MODEL |

**Not:** Çıktı, diğer düğümler tarafından yüz algılama ve işaret noktası çıkarımı görevleri için kullanılabilen karmaşık bir nesnedir. İki algılama varyantı içerir: yakın mesafe algılama için "short" ve tam mesafe algılama için "full".

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/tr.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
