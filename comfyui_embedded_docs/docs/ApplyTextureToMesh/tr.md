# ApplyTextureToMesh

Bu düğüm, pişirilmiş doku görüntülerini bir ağın UV düzenine ekler; böylece SaveGLB düğümü tarafından ağ ile birlikte dışa aktarılabilirler. Pişirme sırasında kullandığınız aynı UV açılmış ağı, pişirilmiş görüntü haritalarıyla birlikte bağlayın. İsteğe bağlı metalik, pürüzlülük ve oklüzyon haritaları tek bir ORM dokusunda paketlenir ve normal harita sağlanması, doğru gölgeleme için gereken düzgün normalleri ve teğetleri de saklar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Pişirilmiş dokuların ekleneceği UV açılmış ağ. Pişirme sırasında kullanılan ağ ile aynı olmalıdır; ağda UV yoksa hata oluşturulur. | MESH | Evet | — |
| `base_color` | Pişirilmiş temel renk görüntüsü. Ağın dokusu olarak saklanır ve 0-1 aralığına sınırlanır. | IMAGE | Evet | — |
| `metallic` | Pişirilmiş metalik harita. Birleşik ORM dokusunun mavi kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 0 değerini alır. | IMAGE | Hayır | — |
| `roughness` | Pişirilmiş pürüzlülük haritası. Birleşik ORM dokusunun yeşil kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 1 değerini alır. | IMAGE | Hayır | — |
| `occlusion` | Pişirilmiş ortam oklüzyon haritası. Birleşik ORM dokusunun kırmızı kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 1 değerini alır. Sağlandığında, ORM dokusu SaveGLB için oklüzyon dokusu olarak da işaretlenir. | IMAGE | Hayır | — |
| `normal_map` | Pişirilmiş teğet uzayı normal haritası. Sağlandığında, düğüm tepe noktası başına teğet tabanını yeniden hesaplar ve normal haritanın doğru gölgelenmesi için düzgün tepe normallerini dışa aktarır. | IMAGE | Hayır | — |

Not: `metallic`, `roughness` veya `occlusion` girdilerinden herhangi biri bağlandığında, üçü de kanalları R = oklüzyon, G = pürüzlülük, B = metalik olacak şekilde tek bir glTF ORM dokusunda paketlenir. Eksik haritalar varsayılan değerlerle doldurulur (oklüzyon 1, pürüzlülük 1, metalik 0) ve farklı çözünürlükteki haritalar en büyük genişlik ve yüksekliğe yeniden boyutlandırılır. `normal_map` bağlandığında, ağın normalleri hesaplanan düzgün tepe normalleriyle değiştirilir ve bir teğet tabanı eklenir. [0,1] aralığının dışında kalan UV koordinatları, en-boy oranı korunarak [0,1] aralığına eşit şekilde ölçeklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Doku görüntüleri UV düzenine eklenmiş, SaveGLB tarafından kaydedilmeye hazır giriş ağı. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `f91985ef686beddccc41a72614b3d263b4e0d9f1a156db6017d620de26d7b6cf`
