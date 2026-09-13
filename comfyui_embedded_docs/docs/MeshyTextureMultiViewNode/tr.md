# Meshy: Modeli Doku Kapla (Çoklu Görünüm)

Bu düğüm, daha önce oluşturulmuş bir 3D modeli, aynı nesnenin 1 ila 4 referans görünümünü kullanarak dokulandırır. Orijinal modelin görev kimliğini ve referans görüntülerini sağlarsınız; düğüm bunları Meshy hizmetine gönderir, işin tamamlanmasını bekler ve dokulandırılmış modeli GLB ve FBX dosyaları olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Dokulandırma işi için kullanılan yapay zeka modeli. Şu anda yalnızca `"meshy-7"` kullanılabilir. | COMBO | Evet | `"meshy-7"` |
| `meshy_task_id` | Dokulandırılacak, daha önce oluşturulmuş 3D modelin görev kimliği. | MESHY_TASK_ID | Evet | — |
| `multiview_images` | Aynı nesnenin referans görünümleri. İlk görüntü birincil (ön) görünümdür; kalan görünümlerin sırası önemli değildir. Büyütülebilir yuva: 1 ila 4 görüntü bağlayın (`image_1` ila `image_4`). | IMAGE | Evet | 1 ila 4 görüntü |
| `enable_original_uv` | Yeni UV'ler oluşturmak yerine modelin orijinal UV'sini kullanın. Etkinleştirildiğinde Meshy, yüklenen modeldeki mevcut dokuları korur. Modelin orijinal UV'si yoksa çıktının kalitesi o kadar iyi olmayabilir. (varsayılan: True; gelişmiş seçenek) | BOOLEAN | Hayır | True / False |
| `pbr` | PBR (fiziksel tabanlı işleme) doku üretimini etkinleştirir. (varsayılan: False; gelişmiş seçenek) | BOOLEAN | Hayır | True / False |
| `texture_resolution` | Temel renk dokusu çözünürlüğü. Daha yüksek çözünürlükler daha fazla yüzey ayrıntısı yakalar. | COMBO | Evet | `"2k"`<br>`"4k"`<br>`"8k"` |

**Not:** `multiview_images` 1 ile 4 arasında görüntü içermelidir. Düğüm bunu çalışma zamanında doğrular ve sayı bu aralığın dışındaysa hata verir. Bağlanan bir görüntü birden çok görüntüden oluşan bir toplu iş içeriyorsa, toplu işteki her görüntü sınıra dahil edilir. İlk görüntü birincil (ön) görünüm olarak kullanılır; kalan görüntülerin sırası önemli değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Model dosyası adı. Bu çıktı yalnızca geriye dönük uyumluluk için tutulur. | STRING |
| `meshy_task_id` | Dokulandırma işinin görev kimliği. | MESHY_TASK_ID |
| `GLB` | GLB biçiminde indirilen dokulandırılmış 3D model. | FILE3DGLB |
| `FBX` | FBX biçiminde indirilen dokulandırılmış 3D model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureMultiViewNode/tr.md)

---
**Source fingerprint (SHA-256):** `3a08d003683a182121471a064833c09b932c7c84c20fd5cb5ac0285e135b2b7e`
