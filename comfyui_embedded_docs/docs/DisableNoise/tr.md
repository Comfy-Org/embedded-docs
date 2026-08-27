# Gürültüyü Devre Dışı Bırak

DisableNoise düğümü, örnekleme süreçlerinde gürültü üretimini devre dışı bırakmak için kullanılabilen boş bir gürültü yapılandırması sağlar. Hiçbir gürültü verisi içermeyen özel bir gürültü nesnesi döndürür; bu sayede bu çıktıya bağlanan diğer düğümler gürültüyle ilgili işlemleri atlayabilir. Düğüm ayrıca "sıfır gürültü" takma adıyla da aranabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| *Girdi parametresi yok* | Bu düğüm herhangi bir girdi parametresi gerektirmez. | - | - | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `NOISE` | Örnekleme süreçlerinde gürültü üretimini devre dışı bırakmak için kullanılabilen boş bir gürültü yapılandırması döndürür. | NOISE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/tr.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`
