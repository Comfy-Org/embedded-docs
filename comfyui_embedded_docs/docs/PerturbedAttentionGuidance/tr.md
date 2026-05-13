> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/tr.md)

PerturbedAttentionGuidance düğümü, bir difüzyon modeline bozulmuş dikkat yönlendirmesi uygulayarak üretim kalitesini artırır. Örnekleme sırasında modelin öz-dikkat mekanizmasını, değer projeksiyonlarına odaklanan basitleştirilmiş bir sürümle değiştirir. Bu teknik, koşullu gürültü giderme sürecini ayarlayarak üretilen görüntülerin tutarlılığını ve kalitesini iyileştirmeye yardımcı olur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `model` | MODEL | Evet | - | Bozulmuş dikkat yönlendirmesinin uygulanacağı difüzyon modeli |
| `ölçek` | FLOAT | Hayır | 0.0 - 100.0 | Bozulmuş dikkat yönlendirme etkisinin gücü (varsayılan: 3.0). 0 olarak ayarlandığında düğümün hiçbir etkisi olmaz ve orijinal gürültü giderilmiş sonucu döndürür. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Bozulmuş dikkat yönlendirmesi uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `8808aa3a3f7cfe306e17f8f4424779cb8e4565647bbcc9d4907da2215affe191`
