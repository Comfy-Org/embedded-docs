WanMoveTrackToVideo düğümü, video oluşturma için koşullandırma ve gizli uzay verilerini hazırlar ve isteğe bağlı hareket takip bilgilerini entegre eder. Bir başlangıç görüntü dizisini gizli bir temsile kodlar ve oluşturulan videodaki hareketi yönlendirmek için nesne takiplerinden gelen konumsal verileri harmanlayabilir. Düğüm, değiştirilmiş pozitif ve negatif koşullandırmayı ve bir video modeli için hazır boş bir gizli tensörü çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Değiştirilecek pozitif koşullandırma girişi. | CONDITIONING | Evet | - |
| `negatif` | Değiştirilecek negatif koşullandırma girişi. | CONDITIONING | Evet | - |
| `vae` | Başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `izler` | Nesne yollarını içeren isteğe bağlı hareket takip verileri. | TRACKS | Hayır | - |
| `güç` | Takip koşullandırmasının gücü. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 100.0 |
| `genişlik` | Çıktı videosunun genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 832) | INT | Hayır | 16 - MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) | INT | Hayır | 16 - MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı. (varsayılan: 81) | INT | Hayır | 1 - MAX_RESOLUTION |
| `toplu_boyutu` | Gizli çıktı için grup boyutu. (varsayılan: 1) | INT | Hayır | 1 - 4096 |
| `başlangıç_görseli` | Kodlanacak başlangıç görüntüsü veya görüntü dizisi. | IMAGE | Evet | - |
| `clip_vision_output` | Koşullandırmaya eklenecek isteğe bağlı CLIP görüş modeli çıktısı. | CLIPVISIONOUTPUT | Hayır | - |

**Not:** `strength` parametresi yalnızca `tracks` sağlandığında etkilidir. Eğer `tracks` sağlanmazsa veya `strength` 0.0 ise, takip koşullandırması uygulanmaz. `start_image`, koşullandırma için bir gizli görüntü ve maske oluşturmak amacıyla kullanılır; sağlanmazsa, düğüm yalnızca koşullandırmayı iletir ve boş bir gizli çıktı verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Potansiyel olarak `concat_latent_image`, `concat_mask` ve `clip_vision_output` içeren değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `latent` | Potansiyel olarak `concat_latent_image`, `concat_mask` ve `clip_vision_output` içeren değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Boyutları `toplu_boyutu`, `uzunluk`, `yükseklik` ve `genişlik` girişleri tarafından şekillendirilen boş bir gizli tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
