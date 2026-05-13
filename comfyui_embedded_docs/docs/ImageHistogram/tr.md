> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/tr.md)

ImageHistogram düğümü, bir giriş görüntüsünün renk dağılımını analiz eder. Görüntüdeki her olası yoğunluk değerine sahip kaç piksel olduğunu gösteren grafikler olan birden fazla histogramı hesaplar ve çıktı olarak verir. Kırmızı, yeşil ve mavi renk kanalları için ayrı ayrı histogramlar, birleşik bir RGB histogramı ve standart bir parlaklık formülüne dayalı bir parlaklık histogramı oluşturur.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | Yok | Analiz edilecek giriş görüntüsü. Düğüm, topluluktaki ilk görüntüyü işler. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `rgb` | HISTOGRAM | Kırmızı, yeşil ve mavi kanallardaki ortalama piksel yoğunluğunu temsil eden birleşik bir histogram. |
| `luminance` | HISTOGRAM | ITU-R BT.709 standart parlaklık formülü kullanılarak hesaplanan, görüntünün algılanan parlaklığının histogramı. |
| `red` | HISTOGRAM | Kırmızı renk kanalındaki piksel yoğunluklarının dağılımını gösteren bir histogram. |
| `green` | HISTOGRAM | Yeşil renk kanalındaki piksel yoğunluklarının dağılımını gösteren bir histogram. |
| `blue` | HISTOGRAM | Mavi renk kanalındaki piksel yoğunluklarının dağılımını gösteren bir histogram. |

---
**Source fingerprint (SHA-256):** `9bfcdb2907ab1e5cb2a9a736671fb9286b0e6ce6439fab95187f691b969ea53d`
