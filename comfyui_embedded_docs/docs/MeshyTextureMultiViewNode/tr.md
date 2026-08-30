# Meshy: Modeli Doku Kapla (Çoklu Görünüm)

Bu düğüm, aynı nesnenin 1 ila 4 referans görünümünü kullanarak daha önce oluşturulmuş bir 3B modeli dokulandırır. Orijinal modelin görev kimliğini ve referans görüntüleri sağlarsınız; düğüm bunları Meshy hizmetine gönderir, işin bitmesini bekler ve dokulandırılmış modeli GLB ve FBX dosyaları olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Dokulandırma işi için kullanılan yapay zeka modeli. Şu anda yalnızca "meshy-7" kullanılabilir. | COMBO | Evet | `"meshy-7"` |
| `meshy_task_id` | Dokulandırılacak daha önce oluşturulmuş 3B modelin görev kimliği. | MESHY_TASK_ID | Evet | — |
| `multiview_images` | Aynı nesnenin referans görünümleri. İlk görüntü ana (ön) görünümdür; kalan görünümlerin sırası önemli değildir. Genişletilebilir yuva: 1 ila 4 görüntü bağlayın (`image_1` - `image_4`). | IMAGE | Evet | 1 ila 4 görüntü |
| `enable_original_uv` | Yeni UV'ler oluşturmak yerine modelin orijinal UV'sini kullanın. Etkinleştirildiğinde, Meshy yüklenen modeldeki mevcut dokuları korur. Modelin orijinal UV'si yoksa, çıktının kalitesi iyi olmayabilir. (varsayılan: True) | BOOLEAN | Hayır | True / False |
| `pbr` | PBR (fiziksel tabanlı işleme) doku üretimini etkinleştirir. (varsayılan: False) | BOOLEAN | Hayır | True / False |
| `texture_resolution` | Temel renk dokusu çözünürlüğü. Daha yüksek çözünürlükler daha fazla yüzey detayı yakalar. | COMBO | Evet | `"2k"`<br>`"4k"`<br>`"8k"` |

**Not:** `multiview_images` 1 ila 4 görüntü içermelidir. Düğüm bunu çalışma zamanında doğrular ve sayı bu aralığın dışındaysa bir hata verir. Bağlı bir görüntü birden çok görüntü içeren bir grup içeriyorsa, gruptaki her görüntü sınıra dahil edilir. İlk görüntü ana (ön) görünüm olarak kullanılır; kalan görüntülerin sırası önemli değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Model dosya adı. Bu çıktı yalnızca geriye dönük uyumluluk için korunmaktadır. | STRING |
| `meshy_task_id` | Dokulandırma işinin görev kimliği. | MESHY_TASK_ID |
| `GLB` | GLB formatında indirilen dokulandırılmış 3B model. | GLB |
| `FBX` | FBX formatında indirilen dokulandırılmış 3B model. | FBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureMultiViewNode/tr.md)

---
**Source fingerprint (SHA-256):** `3a08d003683a182121471a064833c09b932c7c84c20fd5cb5ac0285e135b2b7e`
