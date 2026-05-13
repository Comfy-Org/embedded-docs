> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/tr.md)

DisableNoise düğümü, örnekleme süreçlerinde gürültü oluşumunu devre dışı bırakmak için kullanılabilecek boş bir gürültü yapılandırması sağlar. Hiçbir gürültü verisi içermeyen özel bir gürültü nesnesi döndürür ve bu çıktıya bağlandığında diğer düğümlerin gürültüyle ilgili işlemleri atlamasına olanak tanır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| *Giriş parametresi yok* | - | - | - | Bu düğüm herhangi bir giriş parametresi gerektirmez. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `NOISE` | NOISE | Örnekleme süreçlerinde gürültü oluşumunu devre dışı bırakmak için kullanılabilecek boş bir gürültü yapılandırması döndürür. |

---
**Source fingerprint (SHA-256):** `527152dff69bd5c55c622c634b87e625eb16708f8595fa02d69cf38f1125c5eb`
