> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/tr.md)

ModelMergeSD35_Large düğümü, farklı model bileşenlerinin etkisini ayarlayarak iki Stable Diffusion 3.5 Large modelini birbirine karıştırmanıza olanak tanır. Gömmeli katmanlardan ortak bloklara ve son katmanlara kadar, ikinci modelin her bir parçasının nihai birleştirilmiş modele ne kadar katkıda bulunacağı üzerinde hassas kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirme için temel oluşturan ana model |
| `model2` | MODEL | Evet | - | Bileşenleri ana modele karıştırılacak ikincil model |
| `pos_embed.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen konum gömme (position embedding) katmanının birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `x_embedder.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen x gömücü (x embedder) katmanının birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `context_embedder.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen bağlam gömücü (context embedder) katmanının birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `y_embedder.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen y gömücü (y embedder) katmanının birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen t gömücü (t embedder) katmanının birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.0.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 0'ın birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.1.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 1'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.2.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 2'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.3.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 3'ün birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.4.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 4'ün birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.5.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 5'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.6.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 6'nın birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.7.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 7'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.8.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 8'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.9.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 9'un birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.10.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 10'un birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.11.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 11'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.12.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 12'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.13.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 13'ün birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.14.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 14'ün birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.15.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 15'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.16.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 16'nın birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.17.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 17'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.18.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 18'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.19.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 19'un birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.20.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 20'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.21.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 21'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.22.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 22'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.23.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 23'ün birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.24.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 24'ün birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.25.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 25'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.26.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 26'nın birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.27.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 27'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.28.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 28'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.29.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 29'un birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.30.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 30'un birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.31.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 31'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.32.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 32'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.33.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 33'ün birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.34.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 34'ün birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.35.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 35'in birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.36.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 36'nın birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `joint_blocks.37.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen ortak blok 37'nin birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 ile 1.0 arası | model2'den gelen son katmanın birleştirilmiş modele ne kadar karıştırılacağını kontrol eder (varsayılan: 1.0) |

**Not:** Tüm karıştırma parametreleri 0.0 ile 1.0 arasında değerler kabul eder; burada 0.0, model2'den hiçbir katkı olmadığı ve 1.0, ilgili bileşen için model2'den tam katkı olduğu anlamına gelir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen karıştırma parametrelerine göre her iki girdi modelinin özelliklerini birleştiren ortaya çıkan birleştirilmiş model |

---
**Source fingerprint (SHA-256):** `1b491bd96cc40c6098fd8194f66753bc0f7aa485ea5f97b67b4d864cc9615c9a`
