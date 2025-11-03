> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/tr.md)

CLIPAttentionMultiply düğümü, CLIP modellerindeki dikkat mekanizmasını, öz-dikkat katmanlarının farklı bileşenlerine çarpım faktörleri uygulayarak ayarlamanıza olanak tanır. Bu işlem, CLIP modelinin dikkat mekanizmasındaki sorgu, anahtar, değer ve çıktı projeksiyon ağırlıklarını ve önyargılarını değiştirerek çalışır. Bu deneysel düğüm, belirtilen ölçeklendirme faktörlerinin uygulandığı, girdi CLIP modelinin değiştirilmiş bir kopyasını oluşturur.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | gerekli | - | - | Değiştirilecek CLIP modeli |
| `q` | FLOAT | gerekli | 1.0 | 0.0 - 10.0 | Sorgu projeksiyonu ağırlıkları ve önyargıları için çarpım faktörü |
| `k` | FLOAT | gerekli | 1.0 | 0.0 - 10.0 | Anahtar projeksiyonu ağırlıkları ve önyargıları için çarpım faktörü |
| `v` | FLOAT | gerekli | 1.0 | 0.0 - 10.0 | Değer projeksiyonu ağırlıkları ve önyargıları için çarpım faktörü |
| `çıktı` | FLOAT | gerekli | 1.0 | 0.0 - 10.0 | Çıktı projeksiyonu ağırlıkları ve önyargıları için çarpım faktörü |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Belirtilen dikkat ölçeklendirme faktörlerinin uygulandığı değiştirilmiş bir CLIP modeli döndürür |