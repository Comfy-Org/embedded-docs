# BozulmuşDikkatRehberliği

PerturbedAttentionGuidance düğümü, üretim kalitesini artırmak için bir difüzyon modeline bozulmuş dikkat yönlendirmesi uygular. Örnekleme sırasında modelin öz-dikkat mekanizmasını, değer projeksiyonlarına odaklanan basitleştirilmiş bir sürümle değiştirerek modifiye eder. Bu teknik, koşullu gürültü giderme sürecini ayarlayarak üretilen görüntülerin tutarlılığını ve kalitesini iyileştirmeye yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Bozulmuş dikkat yönlendirmesinin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `scale` | Bozulmuş dikkat yönlendirmesi etkisinin gücü (varsayılan: 3.0). 0 olarak ayarlandığında, düğümün hiçbir etkisi olmaz ve orijinal gürültü giderme sonucunu döndürür. | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Bozulmuş dikkat yönlendirmesi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
