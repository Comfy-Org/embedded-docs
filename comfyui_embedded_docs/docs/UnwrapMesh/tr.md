# Mesh UV'lerini Aç

3D bir ağ için UV atlası oluşturur. Ağ yüzeyi adalara bölünür, her ada iki boyuta düzleştirilir ve düzleştirilmiş adalar [0,1] UV atlasına paketlenir. Ada dikişlerindeki köşe noktaları çoğaltılır (her ada için bir kopya, aynı konum, kendi UV'si), böylece çıktı ağı girdi ağından daha fazla köşe noktası içerebilir ve çıktı yüzleri sayıca girdiden farklı olabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Açılacak girdi ağı. Tek bir ağ veya bir ağ grubunu kabul eder; gruplar her seferinde bir öğe olarak işlenir. | MESH | Evet | — |
| `segmenter` | Kullanılacak ada oluşturma algoritması. `pec`: GPU'da hızlı paralel kenar daraltmalı ada oluşturma. `adaptive`: CPU, daha yavaş. (varsayılan: "pec") | COMBO | Evet | "pec"<br>"adaptive" |
| `resolution` | Texel yoğunluğuna göre otomatik ölçekleme için hedef atlas çözünürlüğü (0 = içeriğe sığdır). (varsayılan: 1024) | INT | Evet | 0 - 8192 (adım 256) |
| `padding` | Adalar arasındaki texel dolgusu. (varsayılan: 1) | INT | Evet | 0 - 16 |
| `weld_distance` | Ağ kapsamının bir kesri olarak çakışık köşe birleştirme yarıçapı (0 = otomatik). Üçgen başına adalar alırsanız (kaynaklanmamış girdi) ~0.001 değerine yükseltin. (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 (adım 0.0001) |

Not: Girdi ağı kaynaklanmamış köşeler içeriyorsa, düğüm yüz komşuluğunun düşük olduğu konusunda uyarabilir ve yüz başına UV adaları üretebilir; `weld_distance` değerini artırmak, açmadan önce çakışık köşeleri birleştirir. Dejenere yüzler (aynı köşe indeksini yeniden kullanan yüzler) işleme sırasında atılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Girdi ağı, [0,1] aralığında oluşturulmuş bir UV atlası ile birlikte. Dikiş köşeleri çoğaltılır, bu nedenle çıktı köşe sayısı girdiyi aşabilir. Girdi ağının köşe renkleri ve dokusu korunur. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/tr.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`
