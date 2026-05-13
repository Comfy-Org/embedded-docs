> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/tr.md)

SD_4XUpscale_Conditioning düğümü, difüzyon modelleri kullanarak görüntüleri büyütmek için koşullandırma verilerini hazırlar. Giriş görüntülerini ve koşullandırma verilerini alır, ardından büyütme işlemini yönlendirmek için ölçeklendirme ve gürültü artırımı uygulayarak değiştirilmiş koşullandırma oluşturur. Düğüm, büyütülmüş boyutlar için hem pozitif hem de negatif koşullandırmayı gizli temsillerle birlikte çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Büyütülecek giriş görüntüleri |
| `positive` | CONDITIONING | Evet | - | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma verileri |
| `negative` | CONDITIONING | Evet | - | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma verileri |
| `scale_ratio` | FLOAT | Hayır | 0.0 - 10.0 | Giriş görüntülerine uygulanan ölçeklendirme faktörü (varsayılan: 4.0) |
| `noise_augmentation` | FLOAT | Hayır | 0.0 - 1.0 | Büyütme işlemi sırasında eklenecek gürültü miktarı (varsayılan: 0.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `positive` | CONDITIONING | Büyütme bilgisi uygulanmış değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Büyütme bilgisi uygulanmış değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Büyütülmüş boyutlarla eşleşen boş gizli temsil |

---
**Source fingerprint (SHA-256):** `ede1ea8f5a95e7f9e52070b5132a4ed3e87f92230d14a74b9d713f547c74d785`
