# WanAnimate2Cache

Poz videosuna ait blok başına aktivasyonları bir kez önbelleğe alır, böylece her örnekleme adımında yeniden hesaplanmaları gerekmez; bu da üretim süresini yaklaşık olarak yarıya indirir. Bunun bedeli ek bellek kullanımıdır: 480x832 çözünürlük ve bf16'da 81 kare ile yaklaşık 12,5 GB sistem RAM'i kullanır; bu değer çözünürlük ve video uzunluğuyla ölçeklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Önbelleğin ekleneceği Wan Animate2 modeli. | MODEL | Evet | |
| `cihaz` | Önbelleğin nerede tutulacağı. cpu (RAM) güvenli seçimdir; önbellek, tipik boyutlarda modelle birlikte VRAM'e sığmaz. gpu (VRAM), sığdığı takdirde daha hızlı olabilir. (varsayılan: "cpu") | STRING | Evet | "cpu"<br>"gpu" |
| `dtype` | Depolama hassasiyeti. default, aktivasyonları modelin hesaplama dtype'ında saklar. int8 önbelleği yarıya, int4 dörtte birine indirir; convrot ise doğruluğu korumak için kullanılır. (varsayılan: "default") | STRING | Evet | "default"<br>"int8"<br>"int4" |

Not: Bağlam pencereleri kullanıldığında, her pencere ayrı ayrı önbelleğe alınır; bu nedenle bellek kullanımı pencere sayısıyla ölçeklenir. static_standard zamanlaması kullanılmalıdır, çünkü tekdüze zamanlamalar pencereleri her adımda kaydırır ve önbellek asla yeniden kullanılmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Poz videosu aktivasyon önbelleği eklenmiş kopyalanmış model. Üretim bittiğinde önbellek otomatik olarak serbest bırakılır. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2Cache/tr.md)

---
**Source fingerprint (SHA-256):** `06305432601afd7c797ef29ef4be3f2bb1aa660e05edde270499e94ccdd54f84`
