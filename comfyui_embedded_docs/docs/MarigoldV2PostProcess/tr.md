# Marigold V2 Son İşleme

This node converts a decoded Marigold V2 prediction into a viewable image. It takes the raw prediction tensor and formats it depending on which type of prediction it is: normalized depth (near objects appear bright), unit-length surface normals, or sRGB albedo.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Görüntülenebilir bir görüntüye dönüştürülecek kod çözülmüş Marigold V2 tahmini. | IMAGE | Evet | - |
| `prediction` | Girdide bulunan tahmin türü; verinin nasıl dönüştürüleceğini belirler. `"depth"`, derinlik değerlerini yakın yüzeyler parlak ve uzak yüzeyler koyu olacak şekilde normalleştirir, ardından sonucu üç renk kanalının tümüne kopyalar. `"normals"`, değerleri -1..1 aralığına yeniden ölçekler, bunları birim yüzey normallerine normalleştirir ve 0..1 aralığına geri eşler. `"albedo"`, değerlere doğrusaldan sRGB'ye dönüşüm uygular. | COMBO | Evet | `"depth"`<br>`"normals"`<br>`"albedo"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Seçilen gösterimde işlenmiş görüntü: normalleştirilmiş derinlik (üç kanalda yinelenen gri tonlama), birim yüzey normalleri veya sRGB albedo. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MarigoldV2PostProcess/tr.md)

---
**Source fingerprint (SHA-256):** `848b29e2dfcd34c44cf9707b9b26cb13c18e82bb16618a15afbe477a1d620e1e`
