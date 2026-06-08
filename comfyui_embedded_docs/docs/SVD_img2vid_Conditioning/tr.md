SVD_img2vid_Conditioning düğümü, Stable Video Diffusion kullanarak video oluşturma için koşullandırma verilerini hazırlar. Bir başlangıç görüntüsünü alır ve CLIP vision ile VAE kodlayıcıları aracılığıyla işleyerek pozitif ve negatif koşullandırma çiftleri ile video oluşturma için boş bir gizli uzay oluşturur. Bu düğüm, oluşturulan videoda hareket, kare hızı ve artırma seviyelerini kontrol etmek için gerekli parametreleri ayarlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip_görü` | Giriş görüntüsünü kodlamak için CLIP vision modeli | CLIP_VISION | Evet | - |
| `başlangıç_görüntüsü` | Video oluşturma için başlangıç noktası olarak kullanılacak başlangıç görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntüyü gizli uzaya kodlamak için VAE modeli | VAE | Evet | - |
| `genişlik` | Çıkış videosu genişliği (varsayılan: 1024, adım: 8) | INT | Evet | 16 ile MAKS_ÇÖZÜNÜRLÜK |
| `yükseklik` | Çıkış videosu yüksekliği (varsayılan: 576, adım: 8) | INT | Evet | 16 ile MAKS_ÇÖZÜNÜRLÜK |
| `video_kareleri` | Videoda oluşturulacak kare sayısı (varsayılan: 14) | INT | Evet | 1 ile 4096 |
| `hareket_kovası_kimliği` | Oluşturulan videodaki hareket miktarını kontrol eder (varsayılan: 127) | INT | Evet | 1 ile 1023 |
| `fps` | Oluşturulan video için saniyedeki kare sayısı (varsayılan: 6) | INT | Evet | 1 ile 1024 |
| `artırma_seviyesi` | Giriş görüntüsüne uygulanacak gürültü artırma seviyesi (varsayılan: 0,0, adım: 0,01) | FLOAT | Evet | 0,0 ile 10,0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görüntü gömmeleri ve video parametrelerini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negative` | Sıfırlanmış gömmeler ve video parametreleri ile negatif koşullandırma verileri | CONDITIONING |
| `latent` | Video oluşturma için hazır boş gizli uzay tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
