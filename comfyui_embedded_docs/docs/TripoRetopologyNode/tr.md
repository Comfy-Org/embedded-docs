# Tripo: Retopoloji

Tripo: Retopology, daha önceki bir Tripo düğümü tarafından oluşturulan yüksek poligonlu bir 3B modeli alır ve temiz topolojiye sahip düşük poligonlu bir sürüm olarak yeniden oluşturur. Modeli Tripo retopoloji hizmetine gönderir, görevin tamamlanmasını bekler, ardından tamamlanan modeli indirir ve görev kimliğini diğer Tripo düğümleri tarafından kullanılmak üzere kullanıma sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Kaynak yüksek poligonlu modelin görev kimliği. Bir Tripo oluşturma düğümünden model görev kimliğini veya Tripo: Segment Model'den segment görev kimliğini kabul eder. | STRING | Evet | Tripo görev kimliği |
| `face_limit` | Hedef yüz sayısı: 500-20.000 üçgen veya 500-10.000 dörtgen. -1, Tripo'nun seçmesini sağlar. (varsayılan: -1) | INT | Evet | -1 (otomatik)<br>500 - 20.000 (üçgen)<br>500 - 10.000 (dörtgen) |
| `quad` | Dörtgen ağ çıktısı. Tripo, dörtgen ağları FBX olarak teslim eder; bu nedenle sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır. (varsayılan: False) | BOOLEAN | Evet | True<br>False (varsayılan) |
| `bake` | Kaynak dokuları düşük poligonlu ağ üzerine pişir. (varsayılan: True) | BOOLEAN | Hayır | True (varsayılan)<br>False |
| `part_names` | Tripo: Segment Model'den virgülle ayrılmış parça adları. Boş bırakılırsa tüm model işlenir. (varsayılan: "") | STRING | Hayır | Model parça adları veya boş |

Not: `face_limit` -1 olarak ayarlandığında, Tripo yüz sayısına otomatik olarak karar verir. `quad` etkinleştirildiğinde, maksimum yüz sınırı 20.000 üçgen yerine 10.000 dörtgendir ve sonuç FBX olarak sağlanır (GLB çıktısı boş kalır). `part_names` boş olduğunda, tüm model işlenir. `face_limit` -1 dışında bir değerse ve izin verilen aralığın dışındaysa, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Tamamlanan model dosyasını tanımlayan geriye dönük uyumlu çıktı. Daha yeni iş akışları bunun yerine GLB veya FBX çıktılarını kullanmalıdır. | STRING |
| `model task_id` | Tamamlanan retopoloji sonucunun görev kimliği. Bu modele başvurmak için diğer Tripo düğümlerine aktarılabilir. | STRING |
| `GLB` | GLB biçimindeki yeniden topolojilendirilmiş düşük poligonlu model. `quad` etkinleştirildiğinde boştur. | GLB FILE |
| `FBX` | FBX biçimindeki yeniden topolojilendirilmiş düşük poligonlu model. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FBX FILE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/tr.md)

---
**Source fingerprint (SHA-256):** `b0e967eb4987a70242b6cfce93f09e0caffb7f4bdd3e4f1439e68f33f9138bb5`
