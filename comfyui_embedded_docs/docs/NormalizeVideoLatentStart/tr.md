> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/tr.md)

Bu düğüm, bir video gizilinin (latent) ilk birkaç karesini, sonraki karelere daha çok benzeyecek şekilde ayarlar. Videoda daha sonraki bir dizi referans karesinden ortalama ve varyansı hesaplar ve bu özellikleri başlangıç karelerine uygular. Bu, videonun başlangıcında daha yumuşak ve tutarlı bir görsel geçiş oluşturmaya yardımcı olur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `latent` | LATENT | Evet | - | İşlenecek video gizil temsili. |
| `start_frame_count` | INT | Evet | 1 ila 16384 | Başlangıçtan itibaren sayılarak normalleştirilecek gizil kare sayısı (varsayılan: 4). |
| `reference_frame_count` | INT | Evet | 1 ila 16384 | Başlangıç karelerinden sonra referans olarak kullanılacak gizil kare sayısı (varsayılan: 5). |

**Not:** `reference_frame_count` değeri, başlangıç karelerinden sonra kullanılabilir kare sayısıyla otomatik olarak sınırlanır. Video gizili yalnızca 1 kare uzunluğundaysa, herhangi bir normalleştirme yapılmaz ve orijinal gizil değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `latent` | LATENT | Başlangıç kareleri normalleştirilmiş, işlenmiş video gizili. |

---
**Source fingerprint (SHA-256):** `64844f3bf1735952334dcca3a829e8f666fd89e817ab66cf3c2dc04ecbbdff56`
