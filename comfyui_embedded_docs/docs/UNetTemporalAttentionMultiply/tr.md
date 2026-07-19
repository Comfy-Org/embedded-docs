# UNetZamansalDikkatÇarpımı

UNetTemporalAttentionMultiply düğümü, zamansal bir UNet modelindeki farklı dikkat mekanizması türlerine çarpma faktörleri uygular. Kendi kendine dikkat ve çapraz dikkat katmanlarının ağırlıklarını ayarlayarak modeli değiştirir ve yapısal ile zamansal bileşenler arasında ayrım yapar. Bu, her bir dikkat türünün model çıktısı üzerindeki etkisinin ne kadar olacağının ince ayarlanmasına olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dikkat çarpanlarıyla değiştirilecek giriş modeli | MODEL | Evet | - |
| `öz_yapısal` | Kendi kendine dikkat yapısal bileşenleri için çarpan (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `öz_zamansal` | Kendi kendine dikkat zamansal bileşenleri için çarpan (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `çapraz_yapısal` | Çapraz dikkat yapısal bileşenleri için çarpan (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `çapraz_zamansal` | Çapraz dikkat zamansal bileşenleri için çarpan (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Ayarlanmış dikkat ağırlıklarıyla değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/tr.md)

---
**Source fingerprint (SHA-256):** `98d62fb28a0cdf62154ae4e0b672b3a7bcb9ed61186a164a43992263c1f9439a`
