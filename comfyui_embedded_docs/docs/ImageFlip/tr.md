> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/tr.md)

ImageFlip düğümü, görüntüleri farklı eksenler boyunca çevirir. Görüntüleri x ekseni boyunca dikey olarak veya y ekseni boyunca yatay olarak çevirebilir. Düğüm, seçilen yönteme bağlı olarak çevirme işlemini gerçekleştirmek için torch.flip işlemlerini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Çevrilecek giriş görüntüsü |
| `flip_method` | STRING | Evet | "x-axis: vertically"<br>"y-axis: horizontally" | Uygulanacak çevirme yönü |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Çevrilmiş çıkış görüntüsü |