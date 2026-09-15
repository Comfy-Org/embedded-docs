# Ağı Sadeleştir

QEM (kuadratik hata metriği) basitleştirmesi kullanarak bir 3B ağı hedef yüz sayısına basitleştirir ve hesaplamayı etkin hesaplama aygıtında çalıştırır. `"midpoint"` yerleştirme modu, saç gibi ince özellikleri korurken en iyi kaliteyi sağlayan cumesh-faithful ön ayarıdır; `"qem"` ise isteğe bağlı çizgi ve özellik-kenarı kontrolleriyle köşeleri QEM-optimal konuma yerleştirir. Çıktı ağı kaynaştırılmış olarak kalır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Basitleştirilecek 3B ağ. | MESH | Evet | - |
| `target_face_count` | Hedef maksimum yüz sayısı. 0 devre dışı bırakır. (varsayılan: 200000) | INT | Evet | 0 ile 50000000 |
| `placement_mode` | midpoint: cumesh-faithful (önerilir). qem: QEM-optimal yerleştirme. (varsayılan: `"midpoint"`) | DYNAMIC_COMBO | Evet | `"midpoint"`<br>`"qem"` |

### Midpoint Girdileri

`"midpoint"` yerleştirme modu ek alt parametre sunmaz; varsayılan midpoint yerleştirme ön ayarını kullanır.

### QEM Girdileri

Aşağıdaki alt parametreler yalnızca `placement_mode` `"qem"` olarak ayarlandığında arayüzde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | Kenar başına çizgi-kuadratik ağırlığı; keskin sırtları/çukurları korur. 0 = kapalı. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ile 100.0 |
| `feature_edge_quadric_weight` | Dihedral özellik kenarlarındaki (katlanma çizgileri) ek kuadratik ağırlık. 0 = kapalı. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ile 1000.0 |
| `feature_edge_min_dihedral_deg` | Bir kenarın özellik kenarı olarak sayılması için minimum dihedral açı (derece). (varsayılan: 30.0) | FLOAT | Hayır | 0.0 ile 180.0 |
| `clamp_v_to_edge` | QEM-optimal konumu daraltılmış kenar segmentine yansıt. (varsayılan: true) | BOOLEAN | Hayır | `true`<br>`false` |

Not: `target_face_count` 0 olduğunda veya ağın zaten hedeften daha fazla yüzü olmadığında azaltma işlemi atlanır. Düğüm kendi üzerinde bir yüz azaltma özeti görüntüler, örneğin `faces: 1.23M → 200K (-84%)`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `mesh` | Azaltılmış yüz sayısına sahip basitleştirilmiş ağ; bağlantısallık kaynaştırılmış olarak kalır. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/tr.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
