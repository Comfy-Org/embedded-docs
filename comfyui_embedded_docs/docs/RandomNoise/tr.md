> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/tr.md)

RandomNoise düğümü, bir tohum (seed) değerine dayalı olarak rastgele gürültü desenleri oluşturur. Çeşitli görüntü işleme ve üretim görevlerinde kullanılabilecek, tekrarlanabilir gürültü üretir. Aynı tohum değeri her zaman aynı gürültü desenini üreterek birden çok çalıştırmada tutarlı sonuçlar alınmasını sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `noise_seed` | INT | Evet | 0 ile 18446744073709551615 arası | Rastgele gürültü desenini oluşturmak için kullanılan tohum değeri (varsayılan: 0). Aynı tohum değeri her zaman aynı gürültü çıktısını üretir. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `noise` | NOISE | Sağlanan tohum değerine göre oluşturulan rastgele gürültü deseni. |

---
**Source fingerprint (SHA-256):** `893d3eefdef78592ba3cc403ec1e4bf3a672607abe79f05db1b65078d6b9ea20`
