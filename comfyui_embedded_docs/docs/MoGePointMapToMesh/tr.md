> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/tr.md)

## Genel Bakış

Bu düğüm, bir MoGe nokta haritasını 3B bir ağa dönüştürür. Bir MoGe derinlik tahmin düğümü tarafından üretilen geometri verilerini alır ve bunu UV koordinatları ve isteğe bağlı bir doku içeren bir ağ halinde üçgenler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `moge_geometry` | MOGE_GEOMETRY | Evet | Yok | Nokta haritaları, derinlik ve isteğe bağlı olarak kaynak görüntüyü içeren MoGe geometri verisi. |
| `batch_index` | INT | Evet | 0 ila 4096 | Bir toplu MoGe geometrisindeki hangi görüntünün ağ haline getirileceği. Görüntü başına köşe sayıları farklılık gösterir, bu nedenle toplu işler tek bir MESH içinde birleştirilemez (varsayılan: 0). |
| `decimation` | INT | Evet | 1 ila 8 | Köşe adımı; 1 = tam çözünürlük (varsayılan: 1). |
| `discontinuity_threshold` | FLOAT | Evet | 0.0 ila 1.0 | 3x3 derinlik aralığı bu oranı aşan pikselleri atar. 0 = kapalı (varsayılan: 0.04). |
| `texture` | BOOLEAN | Evet | Doğru/Yanlış | Kaynak görüntüyü baseColor dokusu olarak taşır (varsayılan: Doğru). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `MESH` | MESH | Köşeler, yüzeyler, UV koordinatları ve kaynak görüntüden alınan isteğe bağlı bir doku içeren 3B bir ağ. |

---
**Source fingerprint (SHA-256):** `65c43d64050d1c63d9efbb6c2bb96123f94c6d356d6341f2975537ac24ace29f`
