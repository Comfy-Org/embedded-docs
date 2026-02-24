> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/tr.md)

Resize Images by Longer Edge düğümü, bir veya daha fazla görüntüyü, en uzun kenarları belirtilen bir hedef uzunluğa denk gelecek şekilde yeniden boyutlandırır. Genişlik veya yüksekliğin hangisinin daha uzun olduğunu otomatik olarak belirler ve orijinal en-boy oranını korumak için diğer boyutu orantılı olarak ölçeklendirir. Bu, görüntü boyutlarını en büyük boyutlarına göre standartlaştırmak için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Yeniden boyutlandırılacak giriş görüntüsü veya görüntü grubu. |
| `longer_edge` | INT | Hayır | 1 - 8192 | En uzun kenar için hedef uzunluk. Daha kısa kenar orantılı olarak ölçeklendirilecektir. (varsayılan: 1024) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Yeniden boyutlandırılmış görüntü veya görüntü grubu. Çıktı, girdiyle aynı sayıda görüntü içerecek ve her birinin en uzun kenarı belirtilen `longer_edge` uzunluğuyla eşleşecektir. |
