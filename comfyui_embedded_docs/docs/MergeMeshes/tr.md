# Mesh'leri Birleştir

MergeMeshes, birden çok mesh girdisini; köşe noktalarını, yüzlerini, UV koordinatlarını ve köşe renklerini üst üste yerleştirerek ve yüz indekslerini kaydırarak tüm parçaların doğru şekilde tek bir sürekli mesh halinde birleşmesini sağlayarak tek bir mesh'te birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh'ler` | Genişletilebilir yuva: 2 ila 50 arasında mesh nesnesi bağlayın (`mesh_1`, `mesh_2`, ..., `mesh_50` olarak adlandırılır). Bağlanan tüm mesh'ler tek bir çıktı mesh'inde birleştirilir. | MESH | Evet | 2 ila 50 mesh |

**Not:** En az bir mesh sağlanmalıdır; aksi takdirde düğüm bir hata verir. Her girdi mesh'inin grubundan yalnızca ilk mesh öğesi kullanılır. Girdi mesh'leri birleştirme öncesinde CPU'ya taşınır. Herhangi bir girdi mesh'i UV verisine sahipse çıktı UV'leri içerir ve UV'si olmayan mesh'ler sıfırla doldurulmuş UV değerleri alır. Herhangi bir girdi mesh'i köşe renklerine sahipse çıktı köşe renklerini içerir; renkleri olmayan mesh'ler beyaz (değer 1) renkler alır ve renk kanalları, girdiler arasında bulunan en büyük kanal sayısına doldurulur. Yalnızca bir doku sağlayan ilk girdiden gelen doku tutulur; ek dokular atılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Tüm girdi köşe noktalarını, yüzlerini, UV'lerini ve renklerini tek bir mesh'te birleştiren birleştirilmiş mesh. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/tr.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`
