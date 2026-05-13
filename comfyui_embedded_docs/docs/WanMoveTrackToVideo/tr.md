> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/tr.md)

WanMoveTrackToVideo düğümü, video oluşturma için koşullandırma ve gizli uzay verilerini hazırlar ve isteğe bağlı hareket takip bilgilerini entegre eder. Bir başlangıç görüntü dizisini gizli bir temsile kodlar ve oluşturulan videodaki hareketi yönlendirmek için nesne takiplerinden gelen konumsal verileri harmanlayabilir. Düğüm, değiştirilmiş pozitif ve negatif koşullandırmayı ve bir video modeli için hazır boş bir gizli tensörü çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `positive` | CONDITIONING | Evet | - | Değiştirilecek pozitif koşullandırma girişi. |
| `negative` | CONDITIONING | Evet | - | Değiştirilecek negatif koşullandırma girişi. |
| `vae` | VAE | Evet | - | Başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. |
| `tracks` | TRACKS | Hayır | - | Nesne yollarını içeren isteğe bağlı hareket takip verileri. |
| `strength` | FLOAT | Hayır | 0.0 - 100.0 | Takip koşullandırmasının gücü. (varsayılan: 1.0) |
| `width` | INT | Hayır | 16 - MAX_RESOLUTION | Çıktı videosunun genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 832) |
| `height` | INT | Hayır | 16 - MAX_RESOLUTION | Çıktı videosunun yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) |
| `length` | INT | Hayır | 1 - MAX_RESOLUTION | Video dizisindeki kare sayısı. (varsayılan: 81) |
| `batch_size` | INT | Hayır | 1 - 4096 | Gizli çıktı için grup boyutu. (varsayılan: 1) |
| `start_image` | IMAGE | Evet | - | Kodlanacak başlangıç görüntüsü veya görüntü dizisi. |
| `clip_vision_output` | CLIPVISIONOUTPUT | Hayır | - | Koşullandırmaya eklenecek isteğe bağlı CLIP görüş modeli çıktısı. |

**Not:** `strength` parametresi yalnızca `tracks` sağlandığında etkilidir. Eğer `tracks` sağlanmazsa veya `strength` 0.0 ise, takip koşullandırması uygulanmaz. `start_image`, koşullandırma için bir gizli görüntü ve maske oluşturmak amacıyla kullanılır; sağlanmazsa, düğüm yalnızca koşullandırmayı iletir ve boş bir gizli çıktı verir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `positive` | CONDITIONING | Potansiyel olarak `concat_latent_image`, `concat_mask` ve `clip_vision_output` içeren değiştirilmiş pozitif koşullandırma. |
| `negative` | CONDITIONING | Potansiyel olarak `concat_latent_image`, `concat_mask` ve `clip_vision_output` içeren değiştirilmiş negatif koşullandırma. |
| `latent` | LATENT | Boyutları `batch_size`, `length`, `height` ve `width` girişleri tarafından şekillendirilen boş bir gizli tensör. |

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
