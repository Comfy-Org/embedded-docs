# DecimateMesh

### Midpoint Girdileri

`"midpoint"` yerleştirme modu ek alt parametreler sunmaz; varsayılan midpoint yerleştirme ön ayarını kullanır.

### QEM Girdileri

Aşağıdaki alt parametreler yalnızca `placement_mode` değeri `"qem"` olarak ayarlandığında arayüzde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | Kenar başına çizgi-kuadrik ağırlığı; keskin sırtları/vadileri korur. 0 = kapalı. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ile 100.0 |
| `feature_edge_quadric_weight` | Dihedral özellik kenarlarındaki (kıvrımlar) ekstra kuadrik ağırlığı. 0 = kapalı. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ile 1000.0 |
| `feature_edge_min_dihedral_deg` | Bir kenarın özellik kenarı sayılması için minimum dihedral açı (derece). (varsayılan: 30.0) | FLOAT | Hayır | 0.0 ile 180.0 |
| `clamp_v_to_edge` | QEM-optimal konumunu daraltılmış kenar parçasına yansıt. (varsayılan: true) | BOOLEAN | Hayır | `true`<br>`false` |

Not: `target_face_count` 0 olduğunda veya mesh zaten hedeften daha az yüze sahip olduğunda sadeleştirme atlanır. Düğüm, üzerinde bir yüz azaltma özeti görüntüler, örneğin `faces: 1.23M → 200K (-84%)`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Yüz sayısı azaltılmış sadeleştirilmiş mesh; bağlantı kaynaklı kalır. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/tr.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
