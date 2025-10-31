> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeBlocks/tr.md)

ModelMergeBlocks, iki modelin farklı bölümleri için özelleştirilebilir karıştırma oranlarıyla entegrasyonuna olanak tanıyarak gelişmiş model birleştirme işlemleri için tasarlanmıştır. Bu düğüm, belirtilen parametrelere dayanarak iki kaynak modelden bileşenleri seçerek birleştirerek melez modellerin oluşturulmasını kolaylaştırır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | Birleştirilecek ilk model. İkinci modelden yamaların uygulandığı temel model olarak hizmet eder. |
| `model2`  | `MODEL`     | Belirtilen karıştırma oranlarına göre, yamaların çıkarıldığı ve ilk modele uygulandığı ikinci model. |
| `input`   | `FLOAT`     | Modellerin giriş katmanı için karıştırma oranını belirtir. İkinci modelin giriş katmanının ne kadarının ilk modele birleştirileceğini belirler. |
| `middle`  | `FLOAT`     | Modellerin orta katmanları için karıştırma oranını tanımlar. Bu parametre, modellerin orta katmanlarının entegrasyon seviyesini kontrol eder. |
| `out`     | `FLOAT`     | Modellerin çıkış katmanı için karıştırma oranını belirler. İkinci modelin çıkış katmanının katkısını ayarlayarak nihai çıktıyı etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Belirtilen karıştırma oranlarına göre yamalar uygulanmış, iki girdi modelinin melezi olan ortaya çıkan birleştirilmiş model. |