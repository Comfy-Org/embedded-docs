# WanEğlenceİçBoyamadanVideoya

WanFunInpaintToVideo düğümü, isteğe bağlı bir başlangıç görüntüsü ve bitiş görüntüsü kullanarak sonucu yönlendiren inpainting tarzı video oluşturma için koşullandırma ve latent verilerini hazırlar. Sağlanan koşullandırma, VAE ve görüntü karelerini, ilk ve son kare video oluşturmada kullanılan aynı mantıktan geçirerek çalışır ve örnekleme için güncellenmiş koşullandırma ile boş bir latent döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturma için pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negatif` | Video oluşturmada kaçınılacak negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Video karelerini kodlamak ve kodunu çözmek için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı video genişliği piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Çıktı video yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_boyut` | Bir toplu işte oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `clip_görü_çıktısı` | Başlangıç görüntüsü için koşullandırma olarak kullanılan isteğe bağlı CLIP vision çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video oluşturma için isteğe bağlı başlangıç kare görüntüsü | IMAGE | Hayır | - |
| `bitiş_görüntüsü` | Video oluşturma için isteğe bağlı bitiş kare görüntüsü | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | İşlenmiş pozitif koşullandırma çıktısı | CONDITIONING |
| `negative` | İşlenmiş negatif koşullandırma çıktısı | CONDITIONING |
| `latent` | Oluşturulan video latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
