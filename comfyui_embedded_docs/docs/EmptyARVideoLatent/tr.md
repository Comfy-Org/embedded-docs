> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/tr.md)

# Genel Bakış

EmptyARVideoLatent düğümü, video üretimi için boş, içeriksiz bir latent temsil oluşturur. Belirtilen boyutlar, en-boy oranı ve uzunlukta sıfırlardan oluşan bir tensör sağlayarak video üretim sürecini başlatmak için kullanılır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `width` | INT | Evet | 16 ila 8192 (adım: 16) | Video karelerinin piksel cinsinden genişliği (varsayılan: 832) |
| `height` | INT | Evet | 16 ila 8192 (adım: 16) | Video karelerinin piksel cinsinden yüksekliği (varsayılan: 480) |
| `length` | INT | Evet | 1 ila 1024 (adım: 4) | Videodaki kare sayısı (varsayılan: 81) |
| `batch_size` | INT | Evet | 1 ila 64 | Tek bir grupta oluşturulacak video sayısı (varsayılan: 1) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `LATENT` | LATENT | Belirtilen boyutlar, uzunluk ve grup boyutuyla boş bir video latent alanını temsil eden, sıfırlarla doldurulmuş bir latent tensör. Tensör şekli [batch_size, 16, lat_t, height/8, width/8] şeklindedir; burada lat_t, uzunluk değerinden hesaplanır. |