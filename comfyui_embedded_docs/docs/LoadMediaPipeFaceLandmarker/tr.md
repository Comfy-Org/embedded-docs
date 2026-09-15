# MediaPipe Yüz İşaretleyicisini Yükle

Bu düğüm, görüntülerde yüzleri ve yüz işaret noktalarını (gözler, burun ve ağız gibi) algılayan bir MediaPipe Face Landmarker v2 modeli yükler. Yüklenen model, iki algılama varyantını (kısa menzilli ve tam menzilli) paylaşılan mesh verileri, blendshape'ler ve yüz analizi için kullanılan kanonik geometriyle birlikte paketler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | models/detection/ dizininden yüz algılama modeli. | COMBO | Evet | `models/detection/` dizininde bulunan kullanılabilir model dosya adlarının listesi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | Hem algılama varyantlarını (short/full), yüz topolojisi için bağlantı kümelerini, kanonik verileri ve GPU yönetimi için model patcher'larını içeren yüklenmiş bir FaceLandmarker model nesnesi. | FACE_DETECTION_MODEL |

**Not:** Çıktı, diğer düğümler tarafından yüz algılama ve işaret noktası çıkarma görevleri için kullanılabilecek karmaşık bir nesnedir. İki algılama varyantı içerir: yakın mesafe algılama için "short" ve tam menzilli algılama için "full".

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/tr.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
