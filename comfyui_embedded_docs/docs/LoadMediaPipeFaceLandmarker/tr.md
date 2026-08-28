# MediaPipe Yüz İşaretleyicisini Yükle

## Genel Bakış

Bu düğüm, görüntülerde yüzleri ve yüz hatlarını (gözler, burun ve ağız gibi) algılayabilen bir MediaPipe Face Landmarker v2 modeli yükler. Yüz analizi için iki algılama varyantı (yakın menzil ve tam menzil) ile birlikte paylaşılan ağ verilerini, karışım şekillerini (blendshapes) ve kanonik geometriyi içerir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | `models/detection/` dizininden yüz algılama modeli. | COMBO | Evet | `models/detection/` dizininde bulunan mevcut modellerin listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | Yüklü bir FaceLandmarker model nesnesi; hem kısa/tam algılama varyantlarını, yüz topolojisi için bağlantı kümelerini, kanonik verileri ve GPU yönetimi için model yamalarını içerir. | FACE_DETECTION_MODEL |

**Not:** Çıktı, diğer düğümler tarafından yüz algılama ve yüz hatlarını çıkarma görevleri için kullanılabilen karmaşık bir nesnedir. İki algılama varyantı içerir: yakın menzil algılama için "short" (kısa) ve tam menzil algılama için "full" (tam).

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/tr.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
