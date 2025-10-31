> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/tr.md)

RandomNoise düğümü, bir seed değerine dayalı olarak rastgele gürültü desenleri oluşturur. Yeniden üretilebilir gürültü oluşturur ve bu, çeşitli görüntü işleme ve oluşturma görevleri için kullanılabilir. Aynı seed değeri her zaman aynı gürültü desenini üretecektir, bu da birden fazla çalıştırma arasında tutarlı sonuçlar elde edilmesini sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `noise_seed` | INT | Evet | 0 ile 18446744073709551615 | Rastgele gürültü desenini oluşturmak için kullanılan seed değeri (varsayılan: 0). Aynı seed değeri her zaman aynı gürültü çıktısını üretecektir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `noise` | NOISE | Sağlanan seed değerine dayalı olarak oluşturulan rastgele gürültü deseni. |