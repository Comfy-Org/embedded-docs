# BozulmuşDikkatRehberliği

PerturbedAttentionGuidance düğümü, üretim kalitesini artırmak için bir difüzyon modeline bozulmuş dikkat rehberliği uygular. Örnekleme sırasında modelin gürültü giderme sürecini, normal koşullu tahmini yalnızca değer projeksiyonlarını kullanan basitleştirilmiş bir dikkat mekanizmasıyla yapılan tahminle karşılaştırarak ayarlar ve ölçeklendirilmiş farkı sonuca geri ekler. Ölçek 0 olarak ayarlandığında düğümün hiçbir etkisi yoktur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Bozulmuş dikkat rehberliğinin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `ölçek` | Bozulmuş dikkat rehberliği etkisinin gücü (varsayılan: 3.0). 0 olarak ayarlandığında düğümün hiçbir etkisi yoktur ve orijinal gürültüsü giderilmiş sonucu döndürür. | FLOAT | Evet | 0.0 - 100.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Bozulmuş dikkat rehberliği uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
