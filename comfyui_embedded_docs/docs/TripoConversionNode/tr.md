# Tripo: Modeli Dönüştür

TripoConversionNode, Tripo API'sini kullanarak 3B modelleri farklı dosya formatları arasında dönüştürür. Önceki bir Tripo işleminden (model oluşturma, iskeletleme veya yeniden hedefleme) bir görev kimliği alır ve ortaya çıkan modeli, çeşitli dışa aktarma seçenekleriyle istediğiniz formata dönüştürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `orijinal_model_görev_id` | Önceki bir Tripo işleminden (model oluşturma, iskeletleme veya yeniden hedefleme) alınan görev kimliği | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Evet | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID |
| `biçim` | Dönüştürülen 3B model için hedef dosya formatı | COMBO | Evet | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `dörtlü` | Üçgenlerin dörtgenlere dönüştürülüp dönüştürülmeyeceği (varsayılan: False) | BOOLEAN | Hayır | True/False |
| `yüz_sınırı` | Çıktı modelindeki maksimum yüz sayısı, sınırsız için -1 kullanın (varsayılan: -1) | INT | Hayır | -1 ile 2000000 |
| `doku_boyutu` | Çıktı dokularının piksel cinsinden boyutu (varsayılan: 4096) | INT | Hayır | 128 ile 4096 |
| `doku_biçimi` | Dışa aktarılan dokular için format (varsayılan: JPEG) | COMBO | Hayır | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Modelde simetrinin zorlanıp zorlanmayacağı (varsayılan: False) | BOOLEAN | Hayır | True/False |
| `flatten_bottom` | Modelin tabanının düzleştirilip düzleştirilmeyeceği (varsayılan: False) | BOOLEAN | Hayır | True/False |
| `flatten_bottom_threshold` | Taban düzleştirme eşiği (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ile 1.0 |
| `pivot_to_center_bottom` | Dönüş noktasının modelin alt merkezine taşınıp taşınmayacağı (varsayılan: False) | BOOLEAN | Hayır | True/False |
| `scale_factor` | Modele uygulanacak ölçek faktörü (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ve üzeri |
| `with_animation` | Dışa aktarıma animasyon verilerinin dahil edilip edilmeyeceği (varsayılan: False) | BOOLEAN | Hayır | True/False |
| `pack_uv` | UV koordinatlarının paketlenip paketlenmeyeceği (varsayılan: False) | BOOLEAN | Hayır | True/False |
| `bake` | Dokuların pişirilip pişirilmeyeceği (varsayılan: False) | BOOLEAN | Hayır | True/False |
| `part_names` | Dışa aktarıma dahil edilecek parça adlarının virgülle ayrılmış listesi (varsayılan: "") | STRING | Hayır | Virgülle ayrılmış liste |
| `fbx_preset` | Kullanılacak FBX dışa aktarma ön ayarı (varsayılan: blender) | COMBO | Hayır | blender<br>mixamo<br>3dsmax |
| `export_vertex_colors` | Köşe renklerinin dışa aktarılıp aktarılmayacağı (varsayılan: False) | BOOLEAN | Hayır | True/False |
| `export_orientation` | Dışa aktarma yönlendirme modu (varsayılan: default) | COMBO | Hayır | align_image<br>default |
| `animate_in_place` | Modelin yerinde canlandırılıp canlandırılmayacağı (varsayılan: False) | BOOLEAN | Hayır | True/False |

**Not:** `original_model_task_id`, önceki bir Tripo işleminden (model oluşturma, iskeletleme veya yeniden hedefleme) alınan geçerli bir görev kimliği olmalıdır. "Gelişmiş" olarak işaretlenen parametreler isteğe bağlıdır ve yalnızca belirli dışa aktarma gereksinimleri için yapılandırılması gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *Adlandırılmış çıktı yok* | Bu düğüm, dönüştürmeyi eşzamansız olarak işler ve sonucu Tripo API sistemi aracılığıyla döndürür | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/tr.md)

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
