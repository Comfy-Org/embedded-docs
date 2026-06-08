# Splatları Birleştir

Merge Splats düğümü, birden fazla gauss splat modelini verilerini birleştirerek tek bir splat halinde birleştirir. Bu, farklı tohumlarla oluşturulan aynı gizli kodun birden fazla kod çözümünü birleştirmek için kullanışlıdır; bu, yüzeyi yoğunlaştırabilir ve 3D ağlar oluştururken kaliteyi artırabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `splat0` | Birleştirilecek ilk gauss splatı | SPLAT | Evet | En az 1 splat gerekli |
| `splat1` | Birleştirilecek ikinci gauss splatı | SPLAT | Evet | En az 1 splat gerekli |
| `splat2` | Birleştirilecek ek gauss splatı (isteğe bağlı) | SPLAT | Hayır | Toplam 32 splata kadar |
| `splat3` | Birleştirilecek ek gauss splatı (isteğe bağlı) | SPLAT | Hayır | Toplam 32 splata kadar |
| ... | Ek splatlar (splat31'e kadar) | SPLAT | Hayır | Toplam 32 splata kadar |

**Not:** Giriş listesi, splatları bağladıkça otomatik olarak yeni yuvalar oluşturur. En az bir splat bağlamanız gerekir. Düğüm, minimum 2 ve maksimum 32 splat kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `splat` | Tüm giriş splatlarının birleştirilmesiyle oluşan, birleştirilmiş gauss splatı | SPLAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeSplat/tr.md)

---
**Source fingerprint (SHA-256):** `597671a3c37d1a4fb7b5a772396e08b7041b3fe8f04120891b1382d42e409d26`
