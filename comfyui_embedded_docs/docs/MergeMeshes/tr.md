# MergeMeshes

MergeMeshes, birden fazla mesh girdisini; köşe noktalarını, yüzeyleri, UV koordinatlarını ve köşe renklerini üst üste ekleyerek ve yüzey indekslerini ayarlayarak tek bir mesh halinde birleştirir. Böylece sonuç, tek bir sürekli mesh olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `meshes` | Genişletilebilir yuva: 2 ila 50 mesh nesnesi bağlayın (`mesh_1`, `mesh_2`, ..., `mesh_50` olarak adlandırılır). Bağlanan tüm meshler tek bir çıktı meshinde birleştirilir. | MESH | Evet | 2 ila 50 mesh |

**Not:** Her girdi mesh'inin grubundan yalnızca ilk mesh öğesi kullanılır. Herhangi bir girdi mesh'inde UV verisi varsa, çıktı UV'leri içerir ve UV'si olmayan meshler sıfır değerli UV değerleri alır. Herhangi bir girdi mesh'inde köşe rengi varsa, çıktı köşe renklerini içerir; rengi olmayan meshler beyaz (değer 1) renk alır ve renk kanalları, girdiler arasında bulunan en büyük kanal sayısına göre doldurulur. Yalnızca doku sağlayan ilk girdiden gelen doku korunur; ek dokular atılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Tüm girdi köşe noktalarını, yüzeyleri, UV'leri ve renkleri tek bir mesh içinde birleştiren birleştirilmiş mesh. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/tr.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`
