# Doku'yu Mesh'e Uygula

Bu düğüm, pişirilmiş doku görüntülerini bir ağın UV düzenine ekler; böylece SaveGLB düğümü tarafından ağ ile birlikte dışa aktarılabilirler. Dokuları pişirdiğiniz aynı UV açılmış ağı ve pişirilmiş görüntü haritalarını bu düğüme verin. İsteğe bağlı metalik, pürüzlülük ve ortam kapanması haritaları tek bir ORM dokusunda paketlenir; bir normal haritası sağlamak ayrıca doğru gölgeleme için gereken düzgün köşe normallerini ve teğet temelini depolar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Pişirilmiş dokuların ekleneceği UV açılmış ağ. Pişirme sırasında kullanılan aynı ağ olmalıdır; ağın UV'si yoksa hata verilir. | MESH | Evet | — |
| `base_color` | Pişirilmiş taban renk görüntüsü. Ağın dokusu olarak saklanır ve 0-1 aralığına kısıtlanır. | IMAGE | Evet | — |
| `metallic` | Pişirilmiş metalik haritası. Birleştirilmiş ORM dokusunun mavi kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 0 olur. | IMAGE | Hayır | — |
| `roughness` | Pişirilmiş pürüzlülük haritası. Birleştirilmiş ORM dokusunun yeşil kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 1 olur. | IMAGE | Hayır | — |
| `occlusion` | Pişirilmiş ortam kapanması (ambient occlusion) haritası. Birleştirilmiş ORM dokusunun kırmızı kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 1 olur. Sağlandığında, ORM dokusu SaveGLB için ortam kapanması dokusu olarak da işaretlenir. | IMAGE | Hayır | — |
| `normal_map` | Pişirilmiş teğet uzayı normal haritası. Sağlandığında düğüm, köşe başına teğetleri yeniden hesaplar ve normal haritasının doğru gölgelenmesi için düzgün köşe normallerini dışa aktarır. | IMAGE | Hayır | — |

Not: `mesh` girdisinin UV koordinatları olmalıdır; yoksa düğüm, pişirme için kullanılan aynı UV açılmış ağı bağlamanızı isteyen bir hata verir.

Not: `metallic`, `roughness` veya `occlusion` girdilerinden herhangi biri bağlandığında, üçü de R = occlusion, G = roughness, B = metallic kanallarına sahip tek bir glTF ORM dokusunda paketlenir. Eksik haritalar varsayılanlarla doldurulur (occlusion 1, roughness 1, metallic 0) ve farklı çözünürlüklere sahip haritalar, sağlanan haritalar arasındaki en büyük genişlik ve yüksekliğe yeniden boyutlandırılır.

Not: `normal_map` bağlandığında, ağın saklanan normalleri hesaplanmış düzgün köşe normalleriyle değiştirilir ve köşe başına bir teğet temeli eklenir. [0,1] aralığının dışına düşen UV koordinatları, en-boy oranı korunarak [0,1] aralığına tekdüze ölçeklenir; UV yayılımı döşemeli/UDIM düzeni gibi görünüyorsa bir uyarı günlüğe kaydedilir. Toplu ağlar için UV normalleştirme, pişirme adımıyla aynı mantık kullanılarak toplu işteki her öğeye ayrı ayrı uygulanır, böylece ikisi de hizalı kalır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Doku görüntüleri UV düzenine eklenmiş girdi ağı; SaveGLB tarafından kaydedilmeye hazır. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`
