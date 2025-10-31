> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/tr.md)

LoadImageOutput düğümü, çıktı klasöründen görüntüleri yükler. Yenile düğmesine tıkladığınızda, kullanılabilir görüntülerin listesini günceller ve otomatik olarak ilk görüntüyü seçer, böylece oluşturduğunuz görüntüler arasında kolayca geçiş yapabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | COMBO | Evet | Birden fazla seçenek mevcut | Çıktı klasöründen bir görüntü yükleyin. Görüntü listesini güncellemek için bir yükleme seçeneği ve yenileme düğmesi içerir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | Çıktı klasöründen yüklenen görüntü |
| `mask` | MASK | Yüklenen görüntüyle ilişkili maske |