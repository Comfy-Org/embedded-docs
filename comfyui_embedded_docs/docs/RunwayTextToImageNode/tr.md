> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/tr.md)

Runway Metinden Görüntüye düğümü, Runway'nin Gen 4 modelini kullanarak metin istemlerinden görüntüler oluşturur. Bir metin açıklaması sağlayabilir ve isteğe bağlı olarak görüntü oluşturma sürecine rehberlik etmesi için bir referans görseli ekleyebilirsiniz. Düğüm, API iletişimini halleder ve oluşturulan görseli döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Oluşturma için metin istemi (varsayılan: "") |
| `ratio` | COMBO | Evet | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" | Oluşturulan görsel için en-boy oranı |
| `reference_image` | IMAGE | Hayır | - | Oluşturma sürecine rehberlik etmesi için isteğe bağlı referans görseli |

**Not:** Referans görselinin boyutları 7999x7999 pikseli aşmamalı ve en-boy oranı 0.5 ile 2.0 arasında olmalıdır. Bir referans görseli sağlandığında, görüntü oluşturma sürecine rehberlik eder.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Metin istemi ve isteğe bağlı referans görseline dayalı olarak oluşturulan görsel |