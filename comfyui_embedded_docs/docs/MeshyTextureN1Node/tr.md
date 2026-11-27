# Meshy: Texture Model (N1)

Bu düğüm, daha önce oluşturulmuş bir 3B modeli Meshy N1 doku modeliyle, aynı nesnenin 1 ile 4 referans görünümünü kullanarak dokulandırır. Orijinal modelin görev kimliğini ve görünümleri bağlayın; düğüm bunları Meshy'ye gönderir, işin tamamlanmasını bekler ve dokulandırılmış modeli yeni görev kimliğiyle birlikte GLB ve FBX dosyaları olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|----------|--------|
| `model` | Dokulama işi için kullanılan yapay zekâ modeli. Şu anda yalnızca `"meshy-n1"` kullanılabilir. | COMBO | Evet | `"meshy-n1"` |
| `meshy_task_id` | Dokulandırılacak, daha önce oluşturulmuş 3B modelin görev kimliği. | MESHY_TASK_ID, STRING | Evet | Yok |
| `front_view` | Meshy'nin ön olarak değerlendirdiği görünüm. Tek görüntü ön tarafı dokulandırır ve arka tarafı düz bırakır; arka tarafın aslına uygun olması için `extra_views` içine arka ve yan görünümler ekleyin. | IMAGE | Evet | Tek görüntü |
| `extra_views` | Aynı nesnenin herhangi bir sıradaki diğer görünümleri. Büyütülebilir yuva: 0 ile 3 görüntü bağlayın (`view_1` ... `view_3`). `front_view` ile birlikte en fazla 4 görüntü. | IMAGE | Hayır | 0 ile 3 görüntü arası |
| `enable_original_uv` | Yeni UV'ler oluşturmak yerine modelin orijinal UV'sini kullanın. Etkinleştirildiğinde Meshy, yüklenen modeldeki mevcut dokuları korur. Modelin orijinal UV'si yoksa çıktının kalitesi o kadar iyi olmayabilir. (varsayılan: True; gelişmiş seçenek) | BOOLEAN | Hayır | True / False |

**Not:** `front_view` ve `extra_views` birlikte en fazla 4 görüntü tutabilir; daha fazlası bağlandığında düğüm bir hata verir. Bağlanan bir görüntü toplu iş taşıyorsa, toplu iş içindeki her görüntü bu sınıra dahil edilir. Doku çözünürlüğü 2K olarak sabittir ve PBR haritaları oluşturulmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `meshy_task_id` | Dokulama işinin görev kimliği; sonraki Meshy düğümleri tarafından kullanılabilir. | MESHY_TASK_ID, STRING |
| `GLB` | GLB biçiminde indirilen dokulandırılmış 3B model. | FILE3DGLB |
| `FBX` | FBX biçiminde indirilen dokulandırılmış 3B model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureN1Node/tr.md)

---
**Source fingerprint (SHA-256):** `be4191fd091839cfdce82b4f41fc6ae9e70f7b5b5504eb14a3c0d741d25ac8fd`
