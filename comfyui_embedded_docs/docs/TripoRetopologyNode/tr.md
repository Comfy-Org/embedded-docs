# TripoRetopologyNode

Tripo: Retopology, daha önceki bir Tripo düğümü tarafından oluşturulan yüksek poli 3D modeli alır ve onu temiz topolojili düşük poli bir sürüm olarak yeniden oluşturur. Modeli Tripo retopoloji hizmetine gönderir, görevin tamamlanmasını bekler, ardından tamamlanan modeli indirir ve görev kimliğini diğer Tripo düğümlerinin kullanımına sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Kaynak yüksek poli modelin görev kimliği. Bir Tripo oluşturma düğümünden gelen bir model görev kimliğini veya Tripo: Segment Model'den gelen bir parça görev kimliğini kabul eder. | STRING | Evet | Tripo task ID |
| `face_limit` | Hedef yüz sayısı: 500-20.000 üçgen veya 500-10.000 dörtgen. -1 değeri Tripo'nun seçim yapmasını sağlar. (varsayılan: -1) | INT | Evet | -1 (automatic)<br>500 ile 20,000 arası (triangles)<br>500 ile 10,000 arası (quads) |
| `quad` | Dörtgen ağ çıktısı. Tripo, dörtgen ağları FBX olarak teslim eder, bu nedenle sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır. (varsayılan: False) | BOOLEAN | Evet | True<br>False (default) |
| `bake` | Kaynak dokuları düşük poli ağa pişirir. (varsayılan: True) | BOOLEAN | Hayır | True (default)<br>False |
| `part_names` | Tripo: Segment Model'den virgülle ayrılmış parça adları. Boş bırakılırsa modelin tamamı işlenir. (varsayılan: "") | STRING | Hayır | Model part names or empty |

Not: `face_limit` -1 olarak ayarlandığında Tripo yüz sayısını otomatik olarak belirler. `quad` etkinleştirildiğinde maksimum yüz sınırı 20.000 üçgen yerine 10.000 dörtgendir ve sonuç FBX olarak sağlanır (GLB çıktısı boş kalır). `part_names` boş olduğunda modelin tamamı işlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Tamamlanan model dosyasını tanımlayan geriye dönük uyumlu çıktı. Daha yeni iş akışları bunun yerine GLB veya FBX çıktılarını kullanmalıdır. | STRING |
| `model task_id` | Tamamlanan retopoloji sonucunun görev kimliği. Bu modele başvurmak için diğer Tripo düğümlerine iletilebilir. | STRING |
| GLB | GLB formatında retopoloji uygulanmış düşük poli model. `quad` etkinleştirildiğinde boş kalır. | GLB FILE |
| FBX | FBX formatında retopoloji uygulanmış düşük poli model. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FBX FILE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/tr.md)

---
**Source fingerprint (SHA-256):** `dc15f469b160a1d738e8089cf18de4a8262721bc77ebafa45bf194f04c7726b6`
