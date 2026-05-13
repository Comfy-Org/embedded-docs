> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/tr.md)

TripoConversionNode, Tripo API'sini kullanarak 3B modelleri farklı dosya formatları arasında dönüştürür. Önceki bir Tripo işleminden (model oluşturma, iskeletleme veya yeniden hedefleme) bir görev kimliği alır ve ortaya çıkan modeli, çeşitli dışa aktarma seçenekleriyle istediğiniz formata dönüştürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Evet | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | Önceki bir Tripo işleminden (model oluşturma, iskeletleme veya yeniden hedefleme) alınan görev kimliği |
| `format` | COMBO | Evet | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | Dönüştürülen 3B model için hedef dosya formatı |
| `quad` | BOOLEAN | Hayır | True/False | Üçgenlerin dörtgenlere dönüştürülüp dönüştürülmeyeceği (varsayılan: False) |
| `face_limit` | INT | Hayır | -1 ile 2000000 | Çıktı modelindeki maksimum yüz sayısı, sınırsız için -1 kullanın (varsayılan: -1) |
| `texture_size` | INT | Hayır | 128 ile 4096 | Çıktı dokularının piksel cinsinden boyutu (varsayılan: 4096) |
| `texture_format` | COMBO | Hayır | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | Dışa aktarılan dokular için format (varsayılan: JPEG) |
| `force_symmetry` | BOOLEAN | Hayır | True/False | Modelde simetrinin zorlanıp zorlanmayacağı (varsayılan: False) |
| `flatten_bottom` | BOOLEAN | Hayır | True/False | Modelin tabanının düzleştirilip düzleştirilmeyeceği (varsayılan: False) |
| `flatten_bottom_threshold` | FLOAT | Hayır | 0.0 ile 1.0 | Taban düzleştirme eşiği (varsayılan: 0.0) |
| `pivot_to_center_bottom` | BOOLEAN | Hayır | True/False | Dönüş noktasının modelin alt merkezine taşınıp taşınmayacağı (varsayılan: False) |
| `scale_factor` | FLOAT | Hayır | 0.0 ve üzeri | Modele uygulanacak ölçek faktörü (varsayılan: 1.0) |
| `with_animation` | BOOLEAN | Hayır | True/False | Dışa aktarıma animasyon verilerinin dahil edilip edilmeyeceği (varsayılan: False) |
| `pack_uv` | BOOLEAN | Hayır | True/False | UV koordinatlarının paketlenip paketlenmeyeceği (varsayılan: False) |
| `bake` | BOOLEAN | Hayır | True/False | Dokuların pişirilip pişirilmeyeceği (varsayılan: False) |
| `part_names` | STRING | Hayır | Virgülle ayrılmış liste | Dışa aktarıma dahil edilecek parça adlarının virgülle ayrılmış listesi (varsayılan: "") |
| `fbx_preset` | COMBO | Hayır | blender<br>mixamo<br>3dsmax | Kullanılacak FBX dışa aktarma ön ayarı (varsayılan: blender) |
| `export_vertex_colors` | BOOLEAN | Hayır | True/False | Köşe renklerinin dışa aktarılıp aktarılmayacağı (varsayılan: False) |
| `export_orientation` | COMBO | Hayır | align_image<br>default | Dışa aktarma yönlendirme modu (varsayılan: default) |
| `animate_in_place` | BOOLEAN | Hayır | True/False | Modelin yerinde canlandırılıp canlandırılmayacağı (varsayılan: False) |

**Not:** `original_model_task_id`, önceki bir Tripo işleminden (model oluşturma, iskeletleme veya yeniden hedefleme) alınan geçerli bir görev kimliği olmalıdır. "Gelişmiş" olarak işaretlenen parametreler isteğe bağlıdır ve yalnızca belirli dışa aktarma gereksinimleri için yapılandırılması gerekir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *Adlandırılmış çıktı yok* | - | Bu düğüm, dönüştürmeyi eşzamansız olarak işler ve sonucu Tripo API sistemi aracılığıyla döndürür |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
