> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/tr.md)

FluxKontextMultiReferenceLatentMethod düğümü, belirli bir referans gizli değişken yöntemini ayarlayarak koşullandırma verilerini değiştirir. Seçilen yöntemi koşullandırma girişine ekler; bu, sonraki üretim adımlarında referans gizli değişkenlerinin nasıl işleneceğini etkiler. Bu düğüm deneysel olarak işaretlenmiştir ve Flux koşullandırma sisteminin bir parçasıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Evet | - | Referans gizli değişken yöntemiyle değiştirilecek koşullandırma verileri |
| `reference_latents_method` | STRING | Evet | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` | Referans gizli değişken işleme için kullanılacak yöntem. "uxo" veya "uso" seçilirse "uxo"ya dönüştürülür. Bu parametre gelişmiş olarak işaretlenmiştir. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `conditioning` | CONDITIONING | Referans gizli değişken yöntemi uygulanmış, değiştirilmiş koşullandırma verileri |

---
**Source fingerprint (SHA-256):** `9d39a8fee08ae347a745b20b3dc39051ee2f4645392e769247ae32be35491048`
