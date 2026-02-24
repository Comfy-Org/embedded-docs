> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/tr.md)

WanMoveTrackToVideo düğümü, video oluşturma için koşullandırma ve gizli uzay verilerini hazırlar ve isteğe bağlı hareket izleme bilgilerini dahil eder. Bir başlangıç görüntü dizisini gizli bir temsile kodlar ve oluşturulan videodaki hareketi yönlendirmek için nesne izlerinden konumsal verileri harmanlayabilir. Düğüm, değiştirilmiş pozitif ve negatif koşullandırmanın yanı sıra bir video modeli için hazır boş bir gizli tensör çıktısı verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Değiştirilecek pozitif koşullandırma girişi. |
| `negative` | CONDITIONING | Evet | - | Değiştirilecek negatif koşullandırma girişi. |
| `vae` | VAE | Evet | - | Başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. |
| `tracks` | TRACKS | Hayır | - | İsteğe bağlı nesne yollarını içeren hareket izleme verileri. |
| `strength` | FLOAT | Hayır | 0.0 - 100.0 | İz koşullandırmanın gücü. (varsayılan: 1.0) |
| `width` | INT | Hayır | 16 - MAX_RESOLUTION | Çıktı videosunun genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 832) |
| `height` | INT | Hayır | 16 - MAX_RESOLUTION | Çıktı videosunun yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) |
| `length` | INT | Hayır | 1 - MAX_RESOLUTION | Video dizisindeki kare sayısı. (varsayılan: 81) |
| `batch_size` | INT | Hayır | 1 - 4096 | Gizli çıktı için toplu iş boyutu. (varsayılan: 1) |
| `start_image` | IMAGE | Evet | - | Kodlanacak başlangıç görüntüsü veya görüntü dizisi. |
| `clip_vision_output` | CLIPVISIONOUTPUT | Hayır | - | Koşullandırmaya eklemek için isteğe bağlı CLIP görüntü modeli çıktısı. |

**Not:** `strength` parametresi yalnızca `tracks` sağlandığında etki gösterir. Eğer `tracks` sağlanmazsa veya `strength` 0.0 ise, iz koşullandırma uygulanmaz. `start_image`, koşullandırma için bir gizli görüntü ve maske oluşturmak için kullanılır; sağlanmazsa, düğüm yalnızca koşullandırmayı geçirir ve boş bir gizli çıktı verir.

## Çıkışlar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Değiştirilmiş pozitif koşullandırma, potansiyel olarak `concat_latent_image`, `concat_mask` ve `clip_vision_output` içerir. |
| `negative` | CONDITIONING | Değiştirilmiş negatif koşullandırma, potansiyel olarak `concat_latent_image`, `concat_mask` ve `clip_vision_output` içerir. |
| `latent` | LATENT | `batch_size`, `length`, `height` ve `width` girişleri tarafından şekillendirilen boyutlara sahip boş bir gizli tensör. |
