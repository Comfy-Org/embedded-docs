# WeldVertices

Weld Vertices, bir 3B ağdaki çakışık köşeleri birleştirir; böylece önceden ayrı köşe noktalarına sahip olan yüzler sonuçta aynı köşeleri paylaşır. Yakın köşeleri, ağın sınırlama kutusuna dayalı bir toleransla ızgara niceleme (grid quantization) kullanarak gruplar ve birleştirilen her grup için köşe renklerinin ortalamasını alır. Bu, bir ağ birleştirilmemiş olarak geldiğinde, yani her yüzün kendi köşelerine sahip olduğu ve paylaşılan kenarların bulunmadığı durumlarda kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Çakışık köşeleri birleştirilecek olan girdi 3B ağı. | MESH | Evet | - |
| `epsilon_rel` | Birleştirme toleransı (sınırlama kutusu köşegeninin oranı). Float yinelenenlerini birleştirmek için 1e-5; gözle görülür şekilde yakın ancak ayrı köşeler için 1e-3. Varsayılan: 1e-5. | FLOAT | Evet | 0.0 to unlimited |
| `epsilon_abs` | Mutlak birleştirme toleransı (0'dan büyük olduğunda `epsilon_rel` değerini geçersiz kılar). Varsayılan: 0.0. | FLOAT | Evet | 0.0 to unlimited |

Not: `epsilon_abs` 0'dan büyük olduğunda, `epsilon_rel` değerine göre önceliklidir ve göreli tolerans yok sayılır. `epsilon_abs` 0 olduğunda, göreli tolerans `epsilon_rel` kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Birleştirilmiş köşelere, güncellenmiş yüz indekslerine ve ortalaması alınmış köşe renklerine sahip birleştirilmiş ağ (girdi ağında renkler varsa). | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/tr.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
