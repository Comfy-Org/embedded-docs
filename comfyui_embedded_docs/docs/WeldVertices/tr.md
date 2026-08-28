# WeldVertices

Weld Vertices, bir 3B ağdaki çakışık köşeleri birleştirir; böylece daha önce ayrı köşe noktalarına sahip olan yüzeyler sonunda aynı köşeleri paylaşır. Yakın köşeleri, ağ sınır kutusuna dayalı bir toleransla ızgara niceleme kullanarak gruplar ve her birleştirilmiş grup için köşe renklerinin ortalamasını alır. Bu, bir ağ birleştirilmemiş olarak geldiğinde, yani her yüzeyin kendi köşelerine sahip olduğu ve hiçbir ortak kenarın bulunmadığı durumlarda kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ağ` | Çakışık köşeleri birleştirilecek olan giriş 3B ağı. | MESH | Evet | - |
| `epsilon_rel` | Birleştirme toleransı (sınır kutusu köşegeninin oranı). Float tekilleştirme için 1e-5; gözle görülür şekilde yakın ancak farklı köşeler için 1e-3. Varsayılan: 1e-5. | FLOAT | Evet | 0.0 to unlimited |
| `epsilon_abs` | Mutlak birleştirme toleransı (0'dan büyükken epsilon_rel'i geçersiz kılar). Varsayılan: 0.0. | FLOAT | Evet | 0.0 to unlimited |

Not: `epsilon_abs` 0'dan büyük olduğunda, `epsilon_rel`'e göre önceliklidir ve göreli tolerans yok sayılır. `epsilon_abs` 0 olduğunda ise göreli tolerans `epsilon_rel` kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `ağ` | Birleştirilmiş köşelere, güncellenmiş yüz indekslerine ve ortalaması alınmış köşe renklerine (giriş ağında renkler varsa) sahip birleştirilmiş ağ. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/tr.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
