> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/tr.md)

SVD_img2vid_Conditioning düğümü, Stable Video Diffusion kullanarak video oluşturma için koşullandırma verilerini hazırlar. Bir başlangıç görüntüsünü alır ve CLIP vision ile VAE kodlayıcıları aracılığıyla işleyerek pozitif ve negatif koşullandırma çiftleri ile video oluşturma için boş bir gizli uzay oluşturur. Bu düğüm, oluşturulan videoda hareket, kare hızı ve artırma seviyelerini kontrol etmek için gerekli parametreleri ayarlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_görü` | CLIP_VISION | Evet | - | Giriş görüntüsünü kodlamak için CLIP vision modeli |
| `başlangıç_görüntüsü` | IMAGE | Evet | - | Video oluşturma için başlangıç noktası olarak kullanılacak başlangıç görüntüsü |
| `vae` | VAE | Evet | - | Görüntüyü gizli uzaya kodlamak için VAE modeli |
| `genişlik` | INT | Evet | 16 ile MAKS_ÇÖZÜNÜRLÜK | Çıkış videosu genişliği (varsayılan: 1024, adım: 8) |
| `yükseklik` | INT | Evet | 16 ile MAKS_ÇÖZÜNÜRLÜK | Çıkış videosu yüksekliği (varsayılan: 576, adım: 8) |
| `video_kareleri` | INT | Evet | 1 ile 4096 | Videoda oluşturulacak kare sayısı (varsayılan: 14) |
| `hareket_kovası_kimliği` | INT | Evet | 1 ile 1023 | Oluşturulan videodaki hareket miktarını kontrol eder (varsayılan: 127) |
| `fps` | INT | Evet | 1 ile 1024 | Oluşturulan video için saniyedeki kare sayısı (varsayılan: 6) |
| `artırma_seviyesi` | FLOAT | Evet | 0,0 ile 10,0 | Giriş görüntüsüne uygulanacak gürültü artırma seviyesi (varsayılan: 0,0, adım: 0,01) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `positive` | CONDITIONING | Görüntü gömmeleri ve video parametrelerini içeren pozitif koşullandırma verileri |
| `negative` | CONDITIONING | Sıfırlanmış gömmeler ve video parametreleri ile negatif koşullandırma verileri |
| `latent` | LATENT | Video oluşturma için hazır boş gizli uzay tensörü |

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
