# BerniniConditioning

BerniniConditioning düğümü, Wan2.2-A14B modeli için video ve görüntü koşullandırma verilerini hazırlar. Kaynak videoları, referans videoları ve referans görüntülerini sağlanan VAE kullanarak kodlar ve bunları bağlam içi token olarak koşullandırma verilerine ekler. Görev, hangi girişlerin bağlı olduğundan otomatik olarak çıkarılır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `pozitif` | Pozitif koşullandırma verileri | CONDITIONING | Evet | - |
| `negatif` | Negatif koşullandırma verileri | CONDITIONING | Evet | - |
| `vae` | Video ve görüntü girişlerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı latenti genişliği (varsayılan: 832) | INT | Evet | 16 ila 8192 (adım: 16) |
| `yükseklik` | Çıktı latenti yüksekliği (varsayılan: 480) | INT | Evet | 16 ila 8192 (adım: 16) |
| `uzunluk` | Çıktı latentindeki kare sayısı (varsayılan: 81) | INT | Evet | 1 ila 8192 (adım: 4) |
| `toplu_boyutu` | Tek bir grupta oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `kaynak_video` | Düzenlenecek veya yeniden stillendirilecek kaynak video (v2v, rv2v). Genişlik/yüksekliğe yeniden boyutlandırılır ve uzunluğa kırpılır. | IMAGE | Hayır | - |
| `referans_video` | Kaynak videoya eklenecek video (ads2v). Uzunluğa göre kırpılır ve en-boy oranı korunarak yeniden boyutlandırılır (uzun kenar ref_max_size ile sınırlanır). | IMAGE | Hayır | - |
| `referans_görüntüler` | Bağlam içi token olarak eklenen referans görüntüleri (r2v, rv2v). Her görüntü kendi doğal en-boy oranında bağımsız olarak kodlanır (uzun kenar ref_max_size ile sınırlanır). En fazla 8 görüntü sağlanabilir. | IMAGE | Hayır | 0 ila 8 görüntü |
| `ref_max_size` | reference_video ve reference_images için uzun kenarın maksimum boyutu. En-boy oranı korunarak yeniden boyutlandırılır ve 16 piksele yuvarlanır (varsayılan: 848). | INT | Hayır | 16 ila 8192 (adım: 16) |

**Not:** Görev, hangi girişlerin bağlı olduğuna göre belirlenir:
- Hiçbir giriş bağlı değil → metinden videoya (t2v)
- Yalnızca `source_video` → videodan videoya (v2v)
- `source_video` + `reference_images` → referans kılavuzlu video düzenleme (rv2v)
- Yalnızca `reference_images` → referanstan videoya (r2v)
- `source_video` + `reference_video` → görüntü/videoyu videoya ekleme (ads2v)
Bağlam akışları sabit bir sırayla eklenir: `source_video` (kaynak ID 1), ardından `reference_video` (kaynak ID 2), ardından her referans görüntüsü (kaynak ID 3, 4, ...). Birden fazla görüntü içeren bir referans görüntü girişi, görüntü başına bir akış sağlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `pozitif` | Bağlam latenteri eklenmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | Bağlam latenteri eklenmiş negatif koşullandırma | CONDITIONING |
| `latent` | Belirtilen genişlik, yükseklik, uzunluk ve batch_size ile eşleşen boyutlara sahip boş latent tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BerniniConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `3535bbe9a1ae007dc579242b44787ab315479a820eb0da680eab9b870ab60699`
