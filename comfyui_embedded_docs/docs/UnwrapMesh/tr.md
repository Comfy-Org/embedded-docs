# UnwrapMesh

3B bir ağ için UV atlası oluşturur. Yüzey parçalara (chart) bölünür, her parça iki boyuta düzleştirilir ve sonuçlar [0,1] UV atlasına paketlenir. Parça dikişlerindeki köşeler çoğaltılır, bu nedenle çıktı ağı girdiden daha fazla köşe içerebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Açılacak (unwrap) giriş ağı. Tek bir ağı veya bir grup ağı kabul eder. | MESH | Evet | — |
| `segmenter` | Kullanılacak parçalama algoritması. pec: GPU üzerinde hızlı paralel kenar-çökmesi parçalama. adaptive: CPU, daha yavaş. (varsayılan: "pec") | COMBO | Evet | "pec"<br>"adaptive" |
| `resolution` | Teksel yoğunluğu otomatik ölçekleme için hedef atlas çözünürlüğü (0 = içeriğe sığdır). (varsayılan: 1024) | INT | Evet | 0 to 8192 (step 256) |
| `padding` | Parçalar arasındaki teksel boşluk (padding). (varsayılan: 1) | INT | Evet | 0 to 16 |
| `weld_distance` | Çakışan köşelerin birleştirilme yarıçapı, ağ boyutunun kesri olarak (0 = otomatik). Üçgen başına parçalar elde ediyorsanız (kaynaşmamış giriş) ~0.001'e yükseltin. (varsayılan: 0.0) | FLOAT | Evet | 0.0 to 1.0 (step 0.0001) |

Not: Giriş ağı kaynaşmamış köşeler içeriyorsa (üçgen çorbası), düğüm yüzey bitişikliğinin düşük olduğu konusunda uyarı verebilir ve yüzey başına UV parçaları üretebilir; `weld_distance` değerini artırmak, açılımdan önce çakışan köşeleri birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | [0,1] aralığında oluşturulmuş UV atlasına sahip giriş ağı. Dikiş köşeleri çoğaltılır, bu nedenle çıktı köşe sayısı girdiyi aşabilir. Giriş ağındaki köşe renkleri ve dokular korunur. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/tr.md)

---
**Source fingerprint (SHA-256):** `cf0dbbe43df507921e6e9795b42d5cb5691ccc2ae98a8bb17e02e3928ea0b815`
