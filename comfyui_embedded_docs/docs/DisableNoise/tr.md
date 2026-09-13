# Gürültüyü Devre Dışı Bırak

Bu düğüm, örnekleme sırasında gürültü üretimini devre dışı bırakan boş bir gürültü yapılandırması sağlar. İçinde gürültü verisi bulunmayan özel bir gürültü nesnesi çıkarır; böylece ona bağlanan herhangi bir düğüm gürültüyle ilgili işlemleri atlar. Ayrıca "zero noise" takma adıyla da aranabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| *Girdi parametresi yok* | Bu düğüm herhangi bir girdi parametresi gerektirmez. | - | - | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `NOISE` | Örnekleme süreçlerinde gürültü üretimini devre dışı bırakmak için kullanılabilecek boş bir gürültü yapılandırması döndürür. | NOISE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/tr.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`
