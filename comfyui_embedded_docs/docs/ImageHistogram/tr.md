# Görüntü Histogramı

ImageHistogram düğümü, bir girdi görüntüsünün renk dağılımını analiz eder. Görüntüdeki her olası yoğunluk değerine sahip kaç piksel olduğunu gösteren grafikler olan birkaç histogram hesaplar ve çıktı olarak verir. Kırmızı, yeşil ve mavi renk kanalları için ayrı histogramlar, bir bileşik RGB histogramı ve standart bir parlaklık formülüne dayalı bir parlaklık histogramı üretir. Her histogram, 0 ile 255 arasındaki yoğunluk seviyelerini kapsayan 256 bölme içerir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Analiz edilecek girdi görüntüsü. Düğüm, kümedeki ilk görüntüyü işler. | IMAGE | Evet | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `rgb` | Kırmızı, yeşil ve mavi kanallar arasındaki ortalama piksel yoğunluğunu temsil eden bileşik bir histogram. | HISTOGRAM |
| `parlaklık` | ITU-R BT.709 standart parlaklık formülü kullanılarak hesaplanan, görüntünün algılanan parlaklığına ait histogram. | HISTOGRAM |
| `kırmızı` | Kırmızı renk kanalındaki piksel yoğunluklarının dağılımını gösteren histogram. | HISTOGRAM |
| `yeşil` | Yeşil renk kanalındaki piksel yoğunluklarının dağılımını gösteren histogram. | HISTOGRAM |
| `mavi` | Mavi renk kanalındaki piksel yoğunluklarının dağılımını gösteren histogram. | HISTOGRAM |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/tr.md)

---
**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`
