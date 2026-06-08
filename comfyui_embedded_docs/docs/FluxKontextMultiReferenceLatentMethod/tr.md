FluxKontextMultiReferenceLatentMethod düğümü, belirli bir referans gizli değişken yöntemini ayarlayarak koşullandırma verilerini değiştirir. Seçilen yöntemi koşullandırma girişine ekler; bu, sonraki üretim adımlarında referans gizli değişkenlerinin nasıl işleneceğini etkiler. Bu düğüm deneysel olarak işaretlenmiştir ve Flux koşullandırma sisteminin bir parçasıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `koşullandırma` | Referans gizli değişken yöntemiyle değiştirilecek koşullandırma verileri | CONDITIONING | Evet | - |
| `referans_gizli_yöntemi` | Referans gizli değişken işleme için kullanılacak yöntem. "uxo" veya "uso" seçilirse "uxo"ya dönüştürülür. Bu parametre gelişmiş olarak işaretlenmiştir. | STRING | Evet | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `koşullandırma` | Referans gizli değişken yöntemi uygulanmış, değiştirilmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/tr.md)

---
**Source fingerprint (SHA-256):** `9d39a8fee08ae347a745b20b3dc39051ee2f4645392e769247ae32be35491048`
