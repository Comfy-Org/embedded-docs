SD_4XUpscale_Conditioning düğümü, difüzyon modelleri kullanarak görüntüleri büyütmek için koşullandırma verilerini hazırlar. Giriş görüntülerini ve koşullandırma verilerini alır, ardından büyütme işlemini yönlendirmek için ölçeklendirme ve gürültü artırımı uygulayarak değiştirilmiş koşullandırma oluşturur. Düğüm, büyütülmüş boyutlar için hem pozitif hem de negatif koşullandırmayı gizli temsillerle birlikte çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Büyütülecek giriş görüntüleri | IMAGE | Evet | - |
| `pozitif` | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma verileri | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma verileri | CONDITIONING | Evet | - |
| `ölçek_oranı` | Giriş görüntülerine uygulanan ölçeklendirme faktörü (varsayılan: 4.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `gürültü_artırımı` | Büyütme işlemi sırasında eklenecek gürültü miktarı (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Büyütme bilgisi uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | Büyütme bilgisi uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |
| `gizli` | Büyütülmüş boyutlarla eşleşen boş gizli temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `ede1ea8f5a95e7f9e52070b5132a4ed3e87f92230d14a74b9d713f547c74d785`
