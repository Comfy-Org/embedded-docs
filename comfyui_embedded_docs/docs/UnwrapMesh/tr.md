# UnwrapMesh

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Açılacak girdi ağı. Tek bir ağı veya bir ağ kümesini kabul eder. | MESH | Evet | — |
| `segmenter` | Kullanılacak parçalama algoritması. pec: GPU üzerinde hızlı paralel kenar daraltma tabanlı parçalama. adaptive: CPU, daha yavaş. (varsayılan: "pec") | COMBO | Evet | "pec"<br>"adaptive" |
| `resolution` | Texel yoğunluğu otomatik ölçekleme için hedef atlas çözünürlüğü (0 = içeriğe sığdır). (varsayılan: 1024) | INT | Evet | 0 ila 8192 (adım 256) |
| `padding` | Parçalar arasındaki texel dolgusu. (varsayılan: 1) | INT | Evet | 0 ila 16 |
| `weld_distance` | Çakışık köşe birleştirme yarıçapı, ağ kapsamının bir kesri olarak (0 = otomatik). Üçgen başına parça (kaynaklanmamış girdi) görürseniz ~0.001'e yükseltin. (varsayılan: 0.0) | FLOAT | Evet | 0.0 ila 1.0 (adım 0.0001) |

Not: Girdi ağı birleştirilmemiş köşeler içeriyorsa (üçgen çorbası), düğüm yüzey bitişikliğinin düşük olduğuna dair uyarı verebilir ve yüzey başına UV parçaları üretebilir; `weld_distance` değerini artırmak, açma işleminden önce çakışık köşeleri birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-----------|-------------|-----------|
| `mesh` | [0,1] içinde oluşturulmuş UV atlasına sahip girdi ağı. Dikiş köşeleri çoğaltılır, bu nedenle çıktı köşe sayısı girdiyi aşabilir. Girdi ağından köşe renkleri ve doku korunur. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/tr.md)

---
**Source fingerprint (SHA-256):** `cf0dbbe43df507921e6e9795b42d5cb5691ccc2ae98a8bb17e02e3928ea0b815`
