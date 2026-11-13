# TripoTextureNodeV2

Bu düğüm, Tripo iş akışındaki mevcut bir 3B modele, önceki bir oluşturma adımından alınan görev kimliğiyle tanımlanan doku ekler. PBR malzeme haritaları veya düz renkli doku üretebilir; sonuç bir metin istemi, bir stil görseli veya referans görsellerle yönlendirilebilir.

<Note>
Tripo, görev kayıtlarını sunucularında 7 gün saklar (1 Aralık 2026'dan itibaren geçerli). Bu süreden eski bir görev kimliği artık çözümlenemez, bu nedenle kaydedilmiş bir iş akışını bu süreden sonra yeniden çalıştırmak bu düğümde başarısız olur. Devam etmek için yeni bir görev kimliği oluşturmak üzere önceki Tripo düğümünü yeniden çalıştırın veya zaten indirdiğiniz modeli **Tripo: Model İçe Aktar** ile yeniden içe aktarın.
</Note>

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Daha önceki bir Tripo düğümü (model oluşturma veya model segmentasyonu) tarafından üretilen kaynak modelin görev kimliği. | MODEL_TASK_ID / SEGMENT_TASK_ID | Evet | - |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal); kapalı olduğunda düz renkli doku verir. (varsayılan: true) | BOOLEAN | Hayır | true<br>false |
| `texture_seed` | Doku oluşturmada kullanılan tohum. (varsayılan: 42) Gelişmiş girdi. | INT | Hayır | 0 ile 2147483647 arası |
| `texture_quality` | Üretilen dokuların kalitesi. `detailed` = HD dokular, `extreme` = 8K Ultra dokular. (varsayılan: "standard") Gelişmiş girdi. | COMBO | Hayır | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Dokuların modele nasıl hizalandığı. (varsayılan: "original_image") Gelişmiş girdi. | COMBO | Hayır | "original_image"<br>"geometry" |
| `texture_prompt` | Dokulama için isteğe bağlı metin yönlendirmesi. Renklerin çıkarılacağı bir kaynak görüntü taşımayan içe aktarılmış modeller (Tripo: Import Model) için pratikte gereklidir. Referans görsellerle birlikte kullanılamaz. (varsayılan: boş) | STRING | Hayır | - |
| `model_version` | Doku modeli: v3.x ile üretilen mesh'ler için v3.0, v2.5 ile üretilen mesh'ler için v2.5. (varsayılan: v3_0_20250812) | COMBO | Hayır | Tripo doku modeli sürümleri, varsayılan "v3_0_20250812" |
| `style_image` | Dokuların sanatsal stili için referans görsel. Yalnızca `texture_prompt` ile birlikte kullanılır. | IMAGE | Hayır | - |
| `reference` | Dokuları yönlendiren referans görseller. `texture_prompt` veya `style_image` ile birlikte kullanılamaz. (varsayılan: "none") | DYNAMIC_COMBO | Hayır | "none"<br>"image"<br>"multiview" |
| `part_names` | Tripo: Segment Model'den doku uygulanacak virgülle ayrılmış parça adları. Boş bırakılırsa her parçaya doku uygular. (varsayılan: boş) Gelişmiş girdi. | STRING | Hayır | - |

### Görsel Referans Girdileri

`reference` "image" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Dokuların izlemesi gereken tek referans görseli. | IMAGE | Evet | - |

### Çok Görünümlü Referans Girdileri

`reference` "multiview" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Ön görünüm (0°). | IMAGE | Evet | - |
| `image_left` | Sol görünüm (90°). | IMAGE | Evet | - |
| `image_back` | Arka görünüm (180°). | IMAGE | Evet | - |
| `image_right` | Sağ görünüm (270°). | IMAGE | Evet | - |

**Parametre kısıtlamalarına ilişkin notlar:**

- Referans görseller (referans modları "image" veya "multiview") `texture_prompt` veya `style_image` ile birlikte kullanılamaz.
- `style_image` için bir `texture_prompt` sağlanması gerekir.
- `texture_prompt` verilmediğinde, kaynak model bir text-to-model, image-to-model, multiview-to-model veya texture-model görevinden gelmelidir. Kaynak görüntüsü olmayan modeller (içe aktarılmış, segmentlenmiş, tamamlanmış veya retopoloji uygulanmış modeller) bir `texture_prompt` gerektirir; çünkü Tripo referans görselleri yalnızca kendisinin ürettiği modeller için kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model task_id` | Diğer Tripo düğümlerine aktarılabilecek doku işleminin görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB formatında doku uygulanmış model. Kaynak bir quad mesh veya FBX içe aktarımı olduğunda boştur. | FILE_3D_GLB |
| `FBX` | FBX formatında doku uygulanmış model. Tripo quad mesh'ler ve FBX içe aktarımları için FBX döndürür; aksi durumda boştur. | FILE_3D_FBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `dd9b05e37fcdd29896a50451b92a267862ad94b59abfb8680c8b648390cca091`
