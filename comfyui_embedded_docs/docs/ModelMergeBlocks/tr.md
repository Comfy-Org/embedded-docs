# ModelBloklarınıBirleştir

ModelMergeBlocks, gelişmiş model birleştirme işlemleri için tasarlanmış olup, modellerin farklı bölümleri için özelleştirilebilir karışım oranlarıyla iki modelin entegrasyonuna olanak tanır. Bu düğüm, belirtilen parametrelere göre iki kaynak modelden bileşenleri seçerek birleştirip hibrit modeller oluşturmayı kolaylaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model1` | Birleştirilecek ilk model. İkinci modelden alınan yamaların uygulanacağı temel model olarak işlev görür. | `MODEL` |
| `model2` | Belirtilen karışım oranlarına göre yamaların çıkarıldığı ve ilk modele uygulandığı ikinci model. | `MODEL` |
| `giriş` | Modellerin giriş katmanı için karışım oranını belirtir. İkinci modelin giriş katmanının ne kadarının ilk modele ekleneceğini belirler. | `FLOAT` |
| `orta` | Modellerin orta katmanları için karışım oranını tanımlar. Bu parametre, modellerin orta katmanlarının entegrasyon seviyesini kontrol eder. | `FLOAT` |
| `çıktı` | Modellerin çıkış katmanı için karışım oranını belirler. İkinci modelin çıkış katmanının katkısını ayarlayarak nihai çıktıyı etkiler. | `FLOAT` |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen karışım oranlarına göre yamaların uygulandığı, iki giriş modelinin birleşimi olan hibrit model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeBlocks/tr.md)
