# Runway Aleph2 Prompt Image

Bu düğüm, bir kılavuz görüntüyü çıktı videosunda belirli bir ana sabitleyerek, düzenlenmiş videonun o noktada nasıl görüneceğini kontrol eder. Bu düğümü Runway Aleph2 Video to Video düğümünün `prompt_images` girişine bağlayın ve isteğe bağlı `prompt_images` girişini kullanarak birden fazlasını (en fazla 5) zincirleyin.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `image` | Çıktı videosunun seçilen anına yerleştirilecek kılavuz görüntü. | IMAGE | Evet | - |
| `position` | Bu görüntünün çıktı videosunun zaman çizelgesine nasıl yerleştirileceği. Mutlak zamanlama (başlangıçtan itibaren saniye) veya kesirli zamanlama (video süresinin yüzdesi) arasında seçim yapın. | COMBO | Evet | `Absolute (seconds)`<br>`Fraction (0.0 to 1.0)` |
| `prompt_images` | Bununla zincirlenecek isteğe bağlı önceki prompt görüntüleri. En fazla 5 kılavuz görüntüden oluşan bir zincir oluşturmak için başka bir Runway Aleph2 Prompt Image düğümünün çıktısını buraya bağlayın. | PROMPT_IMAGE_CHAIN | Hayır | - |

**Konum Modu Detayları:**

`position` `Absolute (seconds)` olarak ayarlandığında, bir `seconds` değeri sağlamanız gerekir (varsayılan: 0.0, aralık: 0.0 ila 30.0, adım: 0.1). Bu, bu görüntünün uygulandığı çıktı videosunun başlangıcından itibaren saniye cinsinden tam zamanı belirtir.

`position` `Fraction (0.0 to 1.0)` olarak ayarlandığında, bir `fraction` değeri sağlamanız gerekir (varsayılan: 0.0, aralık: 0.0 ila 1.0, adım: 0.01). Bu, bu görüntünün çıktı videosunun toplam süresinin bir kesri olarak uygulandığı yeri belirtir (0.0 = başlangıç, 1.0 = bitiş).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `prompt_images` | Runway Aleph2 Video to Video düğümünün `prompt_images` girişine bağlanabilen bir prompt görüntü zinciri. | PROMPT_IMAGE_CHAIN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2PromptImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `a8b86fb5d73d27cc58aa59c195ca058eec8a5c9433ea09522ff3e905f6b88193`
