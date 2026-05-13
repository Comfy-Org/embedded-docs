> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/tr.md)

Bu düğüm, bir nesnenin farklı açılardan görüntülerini gösteren en fazla dört görüntüyü işleyerek Tripo'nun API'sini kullanarak eşzamanlı olarak 3B modeller oluşturur. Tam bir 3B model oluşturmak için bir ön görüntü ve en az bir ek görünüm (sol, arka veya sağ) gerektirir; doku ve malzeme seçenekleri sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `image` | IMAGE | Evet | - | Nesnenin ön görünüm görüntüsü (zorunlu) |
| `image_left` | IMAGE | Hayır | - | Nesnenin sol görünüm görüntüsü |
| `image_back` | IMAGE | Hayır | - | Nesnenin arka görünüm görüntüsü |
| `image_right` | IMAGE | Hayır | - | Nesnenin sağ görünüm görüntüsü |
| `model_version` | COMBO | Hayır | Birden çok seçenek mevcut | Oluşturma için kullanılacak model sürümü |
| `orientation` | COMBO | Hayır | Birden çok seçenek mevcut | 3B model için yönlendirme ayarı (varsayılan: "default") |
| `texture` | BOOLEAN | Hayır | - | Model için doku oluşturulup oluşturulmayacağı (varsayılan: True) |
| `pbr` | BOOLEAN | Hayır | - | PBR (Fiziksel Tabanlı İşleme) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: True) |
| `model_seed` | INT | Hayır | - | Model oluşturma için rastgele tohum (varsayılan: 42) |
| `texture_seed` | INT | Hayır | - | Doku oluşturma için rastgele tohum (varsayılan: 42) |
| `texture_quality` | COMBO | Hayır | `"standard"`<br>`"detailed"` | Doku oluşturma için kalite seviyesi (varsayılan: "standard") |
| `texture_alignment` | COMBO | Hayır | `"original_image"`<br>`"geometry"` | Dokuların modele hizalanma yöntemi (varsayılan: "original_image") |
| `face_limit` | INT | Hayır | -1 ila 500000 | Oluşturulan modeldeki maksimum yüz sayısı. Sınırsız için -1 olarak ayarlayın (varsayılan: -1) |
| `quad` | BOOLEAN | Hayır | - | Bu parametre kullanımdan kaldırılmıştır ve hiçbir işlevi yoktur (varsayılan: False) |
| `geometry_quality` | COMBO | Hayır | `"standard"`<br>`"detailed"` | Geometri oluşturma için kalite seviyesi (varsayılan: "standard") |

**Not:** Ön görüntü (`image`) her zaman zorunludur. Çoklu görünüm işleme için en az bir ek görünüm görüntüsü (`image_left`, `image_back` veya `image_right`) sağlanmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model_file` | STRING | Oluşturulan 3B model için dosya yolu veya tanımlayıcı (yalnızca geriye dönük uyumluluk için) |
| `model task_id` | MODEL_TASK_ID | Model oluşturma sürecini izlemek için görev tanımlayıcı |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3B model dosyası |

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
