# ApplyTextureToMesh

Bu düğüm, pişirilmiş doku görüntülerini bir ağın UV yerleşimine ekler; böylece SaveGLB düğümü tarafından ağ ile birlikte dışa aktarılabilirler. Pişirme sırasında kullandığınız UV açılımı yapılmış ağı, pişirilmiş görüntü haritalarıyla birlikte bağlayın. İsteğe bağlı metallic, roughness ve occlusion haritaları tek bir ORM dokusunda paketlenir; ayrıca bir normal harita sağlanması, doğru gölgelendirme için gereken düzgün normalleri ve teğetleri de saklar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Pişirilmiş dokuların ekleneceği UV açılımı yapılmış ağ. Pişirme sırasında kullanılan ağ ile aynı olmalıdır; ağda UV yoksa hata verilir. | MESH | Evet | — |
| `base_color` | Pişirilmiş temel renk görüntüsü. Ağın dokusu olarak saklanır ve 0-1 aralığına sıkıştırılır. | IMAGE | Evet | — |
| `metallic` | Pişirilmiş metallik haritası. Birleşik ORM dokusunun mavi kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 0 alır. | IMAGE | Hayır | — |
| `roughness` | Pişirilmiş pürüzlülük haritası. Birleşik ORM dokusunun yeşil kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 1 alır. | IMAGE | Hayır | — |
| `occlusion` | Pişirilmiş ortam yutulması (ambient occlusion) haritası. Birleşik ORM dokusunun kırmızı kanalı olarak kullanılır; sağlanmadığında varsayılan olarak 1 alır. Sağlandığında, ORM dokusu SaveGLB için ortam yutulması dokusu olarak da işaretlenir. | IMAGE | Hayır | — |
| `normal_map` | Pişirilmiş teğet uzayı normal haritası. Sağlandığında, düğüm köşe başına teğet tabanını yeniden hesaplar ve normal haritanın doğru gölgelenmesi için düzgün köşe normallerini dışa aktarır. | IMAGE | Hayır | — |

Not: `metallic`, `roughness` veya `occlusion` değerlerinden herhangi biri bağlandığında, üçü de R = occlusion, G = roughness, B = metallic kanallarına sahip tek bir glTF ORM dokusunda paketlenir. Eksik haritalar varsayılan değerlerle doldurulur (occlusion 1, roughness 1, metallic 0) ve farklı çözünürlükteki haritalar en büyük genişlik ve yüksekliğe yeniden boyutlandırılır. `normal_map` bağlandığında, ağın normalleri hesaplanan düzgün köşe normalleriyle değiştirilir ve bir teğet tabanı eklenir. [0,1] aralığının dışında kalan UV koordinatları, en-boy oranı korunarak [0,1] aralığına ölçeklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Doku görüntüleri UV yerleşimine eklenmiş, SaveGLB ile kaydedilmeye hazır giriş ağı. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `f91985ef686beddccc41a72614b3d263b4e0d9f1a156db6017d620de26d7b6cf`
