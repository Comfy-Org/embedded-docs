> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/tr.md)

EmptyLatentHunyuan3Dv2 düğümü, Hunyuan3Dv2 3B üretim modelleri için özel olarak biçimlendirilmiş boş latent tensörler oluşturur. Hunyuan3Dv2 mimarisi tarafından gereken doğru boyutlar ve yapıya sahip boş latent uzayları üreterek, 3B üretim iş akışlarını sıfırdan başlatmanıza olanak tanır. Düğüm, sonraki 3B üretim süreçleri için temel oluşturan, sıfırlarla doldurulmuş latent tensörler üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `çözünürlük` | INT | Evet | 1 - 8192 | Latent uzay için çözünürlük boyutu (varsayılan: 3072) |
| `toplu_boyut` | INT | Evet | 1 - 4096 | Toplu işteki latent görüntü sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Hunyuan3Dv2 3B üretimi için biçimlendirilmiş boş örnekler içeren bir latent tensör döndürür |