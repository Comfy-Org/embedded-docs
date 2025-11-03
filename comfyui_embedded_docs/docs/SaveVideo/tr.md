> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/tr.md)

SaveVideo düğümü, giriş video içeriğini ComfyUI çıktı dizininize kaydeder. Kaydedilen dosya için dosya adı önekini, video formatını ve codec'i belirtmenize olanak tanır. Düğüm, sayaç artışlarıyla dosya adlandırmayı otomatik olarak halleder ve kaydedilen videoya iş akışı meta verilerini dahil edebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Kaydedilecek video. |
| `dosyaadı_öneki` | STRING | Hayır | - | Kaydedilecek dosya için önek. Bu, düğümlerden gelen değerleri dahil etmek için %date:yyyy-MM-dd% veya %Empty Latent Image.width% gibi biçimlendirme bilgileri içerebilir (varsayılan: "video/ComfyUI"). |
| `format` | COMBO | Hayır | Birden fazla seçenek mevcut | Videoyu kaydetmek için kullanılacak format (varsayılan: "auto"). |
| `codec` | COMBO | Hayır | Birden fazla seçenek mevcut | Video için kullanılacak codec (varsayılan: "auto"). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *Çıktı yok* | - | Bu düğüm herhangi bir çıktı verisi döndürmez. |