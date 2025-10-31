> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/tr.md)

ImageRotate düğümü, bir giriş görüntüsünü belirtilen açılarla döndürür. Dört döndürme seçeneğini destekler: döndürme yok, 90 derece saat yönünde, 180 derece ve 270 derece saat yönünde. Döndürme işlemi, görüntü veri bütünlüğünü koruyan verimli tensör işlemleri kullanılarak gerçekleştirilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Döndürülecek giriş görüntüsü |
| `rotation` | STRING | Evet | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" | Görüntüye uygulanacak döndürme açısı |

## Çıkışlar

| Çıkış Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Döndürülmüş çıkış görüntüsü |