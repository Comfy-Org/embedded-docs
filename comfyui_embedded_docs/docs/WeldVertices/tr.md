# Köşeleri Kaynaştır

Weld Vertices, 3B bir mesh'teki çakışan köşeleri birleştirir; böylece daha önce ayrı köşe noktalarına sahip olan yüzler aynı köşeleri paylaşır. Yakındaki köşeleri, mesh sınırlayıcı kutusuna dayalı bir toleransla ızgara nicemleme kullanarak gruplandırır ve birleştirilen her grup için köşe renklerinin ortalamasını alır. Bu, bir mesh birleştirilmemiş olarak geldiğinde (yani her yüzün kendi köşeleri vardır ve paylaşılan kenar yoktur) kullanışlıdır ve FillHoles veya DecimateMesh gibi topolojiye duyarlı işlemlerden önce bir ön geçiş olarak hizmet edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ağ` | Çakışan köşeleri birleştirilecek girdi 3B mesh'i. | MESH | Evet | - |
| `epsilon_rel` | Birleştirme toleransı (sınırlayıcı kutu köşegeninin kesri). Float tekilleştirme için 1e-5; görünürde yakın ancak farklı köşeler için 1e-3. Varsayılan: 1e-5. | FLOAT | Evet | 0.0 to unlimited (step 1e-6) |
| `epsilon_abs` | Mutlak birleştirme toleransı (> 0 olduğunda epsilon_rel değerini geçersiz kılar). Varsayılan: 0.0. | FLOAT | Evet | 0.0 to unlimited (step 1e-6) |

Not: `epsilon_abs` 0'dan büyük olduğunda `epsilon_rel`'e göre önceliklidir ve göreli tolerans yok sayılır. `epsilon_abs` 0 olduğunda, göreli tolerans `epsilon_rel` kullanılır ve mesh sınırlayıcı kutusu köşegeniyle çarpılarak mutlak bir mesafeye dönüştürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Birleştirilmiş köşelere, güncellenmiş yüz indekslerine ve (girdi mesh renklere sahipse) ortalaması alınmış köşe renklerine sahip birleştirilmiş mesh. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/tr.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
