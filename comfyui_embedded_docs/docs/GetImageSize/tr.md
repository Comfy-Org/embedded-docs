> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/tr.md)

GetImageSize düğümü, bir giriş görüntüsünden boyut ve toplu işlem bilgilerini çıkarır. Görüntünün genişliğini, yüksekliğini ve toplu işlem boyutunu döndürürken, bu bilgiyi aynı zamanda düğüm arayüzünde ilerleme metni olarak görüntüler. Orijinal görüntü verisi değişmeden geçer.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Boyut bilgisi çıkarılacak giriş görüntüsü |
| `unique_id` | UNIQUE_ID | Hayır | - | İlerleme bilgilerini görüntülemek için kullanılan dahili tanımlayıcı |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `width` | INT | Giriş görüntüsünün piksel cinsinden genişliği |
| `height` | INT | Giriş görüntüsünün piksel cinsinden yüksekliği |
| `batch_size` | INT | Toplu işlemdeki görüntü sayısı |