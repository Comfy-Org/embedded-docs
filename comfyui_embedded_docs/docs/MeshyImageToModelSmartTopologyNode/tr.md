# Meshy: Image to Model (Smart Topology)

Bu düğüm, Meshy T2.5 ile hedef yüz sayısında bir referans görselden oyun motoruna hazır bir üçgen ağ oluşturur. Topoloji, sonradan desimasyon uygulanmak yerine istenen poligon sayısında oluşturulur; böylece sonuç, ayrı bir yeniden topolojilendirme geçişi olmadan oyun motoruna hazır olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Oluşturma için kullanılacak Meshy model sürümü. | COMBO | Evet | `"meshy-t2.5"` |
| `image` | Modelin oluşturulduğu referans görsel. | IMAGE | Evet | - |
| `target_polycount` | Oluşturulan ağdaki yaklaşık üçgen sayısı. Varsayılan: 15000. | INT | Evet | 100 - 30000 |
| `should_texture` | Dokuların oluşturulup oluşturulmayacağını belirler. `"false"` doku aşamasını atlar ve dokusuz bir ağ döndürür. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `enable_pbr` | Temel renge ek olarak PBR Haritaları (metalik, pürüzlülük, normal) oluşturur. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `False`. | BOOLEAN | Hayır | - |
| `texture_prompt` | Dokulandırma sürecini yönlendirmek için metin istemi. En fazla 800 karakter. `texture_image` ile aynı anda kullanılamaz. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `""` (boş dize). | STRING | Hayır | 1 - 800 karakter |
| `texture_image` | Dokulandırma süreci için referans görsel. `texture_image` veya `texture_prompt` seçeneklerinden aynı anda yalnızca biri kullanılabilir. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. | IMAGE | Hayır | - |
| `texture_resolution` | Doku çözünürlüğü. Daha yüksek çözünürlükler daha fazla yüzey ayrıntısı yakalar. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. | COMBO | Hayır | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | Oluşturulan karakterin duruşu. Boş dize, belirli bir duruş istenmediğini belirtir. Bu gelişmiş bir ayardır. Varsayılan: `""` (boş dize). | COMBO | Evet | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 - 2147483647 |

**Not:** `enable_pbr`, `texture_prompt`, `texture_image` ve `texture_resolution` girdileri yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir.

**Kısıtlar:**

* `target_polycount`, ağın oluşturulduğu üçgen sayısıdır; oluşturma sonrasında uygulanan bir sınır değildir.
* `should_texture` `"true"` olarak ayarlandığında, `texture_prompt` ve `texture_image` aynı anda kullanılamaz. İkisi de sağlanırsa düğüm bir hata verir.
* `texture_prompt` en fazla 800 karakter uzunluğunda olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `meshy_task_id` | Meshy API görevinin benzersiz tanımlayıcısı. | MESHY_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3D model. | FILE3DGLB |
| `FBX` | FBX biçiminde oluşturulan 3D model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelSmartTopologyNode/tr.md)

---
**Source fingerprint (SHA-256):** `e78034a591825ec6e105df1942cf501e882ac780cc2584bfa04b424ecc34a02e`
