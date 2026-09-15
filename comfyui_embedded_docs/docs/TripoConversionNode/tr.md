# Tripo: Modeli Dönüştür

Bu düğüm, mevcut bir Tripo 3B modelini başka bir 3B dosya biçimine dönüştürür. Daha önce bir Tripo işlemiyle (model oluşturma, rigleme, yeniden hedefleme veya segmentasyon gibi) oluşturulmuş veya işlenmiş bir modelin görev kimliğini alır, Tripo API'sine bir dönüştürme görevi gönderir, bu görevin tamamlanmasını bekler ve ardından dönüştürülmüş model dosyasını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `orijinal_model_görev_id` | Dönüştürülecek Tripo modelinin görev kimliği. Daha önceki bir Tripo model oluşturma, rigleme, yeniden hedefleme veya segmentasyon görevinden gelmelidir. Kimlik eksik veya boşsa düğüm hata verir. | STRING | Evet | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `biçim` | Dönüştürülen 3B model için hedef dosya biçimi. | COMBO | Evet | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `dörtlü` | Etkinleştirildiğinde üçgenleri dörtgenlere dönüştürür (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `yüz_sınırı` | Dönüştürülen modeldeki maksimum yüz sayısı. Sınır olmaması için -1 olarak ayarlayın (varsayılan: -1). | INT | Hayır | -1 ile 2000000 |
| `doku_boyutu` | Çıktı dokularının piksel cinsinden çözünürlüğü (varsayılan: 4096). | INT | Hayır | 128 ile 8192 |
| `doku_biçimi` | Dışa aktarılan dokular için kullanılan dosya biçimi (varsayılan: JPEG). | COMBO | Hayır | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Etkinleştirildiğinde modeli simetrik olmaya zorlar (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `flatten_bottom` | Etkinleştirildiğinde modelin altını düzleştirir (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `flatten_bottom_threshold` | `flatten_bottom` ile kullanılan düzleştirme derinliği (varsayılan: 0.01). Bu değer yalnızca `flatten_bottom` etkinleştirildiğinde uygulanır. | FLOAT | Hayır | 0.01 ile 1.0 |
| `pivot_to_center_bottom` | Etkinleştirildiğinde pivot noktasını modelin alt merkezine taşır (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `scale_factor` | Dönüştürülen modele uygulanan ölçek faktörü (varsayılan: 1.0). | FLOAT | Hayır | 0.01 and above |
| `with_animation` | Riglenmiş veya yeniden hedeflenmiş modellerin iskeletini ve animasyonunu korur (varsayılan: True). | BOOLEAN | Hayır | True or False |
| `pack_uv` | Etkinleştirildiğinde UV koordinatlarını yeniden paketler (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `bake` | Gelişmiş malzemeleri temel dokulara bake ederek daha geniş uyumluluk sağlar (varsayılan: True). | BOOLEAN | Hayır | True or False |
| `part_names` | Dönüştürmeye gönderilecek model parça adlarının virgülle ayrılmış listesi. Boş girdiler yok sayılır ve yinelenen adlar kaldırılır. Bu seçeneği atlamak için boş bırakın (varsayılan: boş). | STRING | Hayır | Virgülle ayrılmış parça adları listesi |
| `fbx_preset` | FBX uyumluluk ön ayarı. bake_scale, ölçek dönüşümünü geometriye bake eder (varsayılan: blender). | COMBO | Hayır | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | Etkinleştirildiğinde köşe renklerini dışa aktarır (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `export_orientation` | Dışa aktarılan modelin ileri ekseni. default, Tripo'nun +x eksenini korur (varsayılan: default). | COMBO | Hayır | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | Etkinleştirildiğinde modeli yerinde canlandırır (varsayılan: False). | BOOLEAN | Hayır | True or False |

**Not:** `original_model_task_id` ve `format` dışında tüm girdiler isteğe bağlı gelişmiş ayarlardır. Varsayılan değerlerinde bırakılan çoğu ayar, Tripo API'sinin standart davranışını kullanabilmesi için dönüştürme isteğinden çıkarılır. `with_animation` ve `bake` seçenekleri her zaman gönderilir. `flatten_bottom_threshold` yalnızca `flatten_bottom` etkinleştirildiğinde uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | İstenen biçimde dönüştürülmüş model. OBJ, Tripo tarafından ZIP arşivi (mesh, malzeme ve dokular) olarak teslim edilir. | FILE_3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/tr.md)

---
**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`
