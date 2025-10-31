> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/tr.md)

LTXVPreprocess düğümü, görüntülere sıkıştırma ön işleme uygular. Girdi görüntülerini alır ve belirtilen bir sıkıştırma seviyesi ile işleyerek, uygulanan sıkıştırma ayarlarıyla işlenmiş görüntüleri çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | İşlenecek girdi görüntüsü |
| `img_compression` | INT | Hayır | 0-100 | Görüntüye uygulanacak sıkıştırma miktarı (varsayılan: 35) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_image` | IMAGE | Uygulanan sıkıştırma ile işlenmiş çıktı görüntüsü |