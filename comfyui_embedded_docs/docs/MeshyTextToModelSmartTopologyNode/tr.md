# Meshy: Text to Model (Smart Topology)

Bu düğüm, Meshy T2.5 ile hedef yüz sayısında oyuna hazır bir üçgen ağ oluşturur. Topoloji, istenen poligon sayısında oluşturulur ve sonradan azaltılmaz; böylece sonuç, ayrı bir yeniden topoloji geçişine gerek kalmadan oyun motoruna hazır olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak Meshy model sürümü. | COMBO | Evet | `"meshy-t2.5"` |
| `prompt` | Oluşturulacak 3B modelin metin açıklaması. | STRING | Evet | 1-800 karakter |
| `target_polycount` | Oluşturulan ağdaki yaklaşık üçgen sayısı. Varsayılan: 15000. | INT | Evet | 100-30000 |
| `pose_mode` | Oluşturulan karakterin pozu. Boş bir dize belirli bir poz istenmediğini belirtir. Bu gelişmiş bir ayardır. Varsayılan: `""` (boş dize). | COMBO | Evet | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0-2147483647 |

**Kısıtlamalar:**

* İstem 1 ile 800 karakter arasında olmalıdır.
* `target_polycount`, ağın oluşturulduğu üçgen sayısıdır; üretimden sonra uygulanan bir sınır değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `meshy_task_id` | Meshy API görevinin benzersiz tanımlayıcısı. | MESHY_TASK_ID |
| `GLB` | Oluşturulan 3B model, GLB formatında. | FILE3DGLB |
| `FBX` | Oluşturulan 3B model, FBX formatında. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelSmartTopologyNode/tr.md)

---
**Source fingerprint (SHA-256):** `9fcdc846a4ba39cf3d099629637fbb0cf6d9c8d65bcee8aff5ec6ac5c76b6af3`
