# BozulmuşDikkatRehberliği

PerturbedAttentionGuidance düğümü, üretim kalitesini artırmak için bir difüzyon modeline pertürbe edilmiş dikkat rehberliği uygular. Örnekleme sırasında, orta bloğun öz-dikkatinin, değer projeksiyonlarını doğrudan geçiren basitleştirilmiş bir sürümle değiştirildiği ek bir tahmin yapar; ardından normal koşullu tahmin ile bu pertürbe edilmiş tahmin arasındaki ölçeklenmiş farkı, gürültüsü giderilmiş sonuca ekler. `scale` değerini 0 yapmak etkiyi tamamen devre dışı bırakır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Pertürbe edilmiş dikkat rehberliğinin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `scale` | Pertürbe edilmiş dikkat rehberliği etkisinin gücü (varsayılan: 3.0). 0 olarak ayarlandığında düğümün hiçbir etkisi olmaz ve özgün gürültüsü giderilmiş sonucu değiştirmeden döndürür. | FLOAT | Evet | 0.0 - 100.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Örnekleme sürecine pertürbe edilmiş dikkat rehberliği yaması eklenmiş değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
