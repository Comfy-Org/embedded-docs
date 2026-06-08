Bu düğüm, bir nesnenin farklı açılardan görüntülerini gösteren en fazla dört görüntüyü işleyerek Tripo'nun API'sini kullanarak eşzamanlı olarak 3B modeller oluşturur. Tam bir 3B model oluşturmak için bir ön görüntü ve en az bir ek görünüm (sol, arka veya sağ) gerektirir; doku ve malzeme seçenekleri sunar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Nesnenin ön görünüm görüntüsü (zorunlu) | IMAGE | Evet | - |
| `sol_görüntü` | Nesnenin sol görünüm görüntüsü | IMAGE | Hayır | - |
| `arka_görüntü` | Nesnenin arka görünüm görüntüsü | IMAGE | Hayır | - |
| `sağ_görüntü` | Nesnenin sağ görünüm görüntüsü | IMAGE | Hayır | - |
| `model_versiyonu` | Oluşturma için kullanılacak model sürümü | COMBO | Hayır | Birden çok seçenek mevcut |
| `yönlendirme` | 3B model için yönlendirme ayarı (varsayılan: "default") | COMBO | Hayır | Birden çok seçenek mevcut |
| `doku` | Model için doku oluşturulup oluşturulmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `pbr` | PBR (Fiziksel Tabanlı İşleme) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `model_tohumu` | Model oluşturma için rastgele tohum (varsayılan: 42) | INT | Hayır | - |
| `doku_tohumu` | Doku oluşturma için rastgele tohum (varsayılan: 42) | INT | Hayır | - |
| `doku_kalitesi` | Doku oluşturma için kalite seviyesi (varsayılan: "standard") | COMBO | Hayır | `"standard"`<br>`"detailed"` |
| `doku_hizalama` | Dokuların modele hizalanma yöntemi (varsayılan: "original_image") | COMBO | Hayır | `"original_image"`<br>`"geometry"` |
| `yüz_sınırı` | Oluşturulan modeldeki maksimum yüz sayısı. Sınırsız için -1 olarak ayarlayın (varsayılan: -1) | INT | Hayır | -1 ila 500000 |
| `dörtgen` | Bu parametre kullanımdan kaldırılmıştır ve hiçbir işlevi yoktur (varsayılan: False) | BOOLEAN | Hayır | - |
| `geometry_quality` | Geometri oluşturma için kalite seviyesi (varsayılan: "standard") | COMBO | Hayır | `"standard"`<br>`"detailed"` |

**Not:** Ön görüntü (`image`) her zaman zorunludur. Çoklu görünüm işleme için en az bir ek görünüm görüntüsü (`image_left`, `image_back` veya `image_right`) sağlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_görev_id` | Oluşturulan 3B model için dosya yolu veya tanımlayıcı (yalnızca geriye dönük uyumluluk için) | STRING |
| `GLB` | Model oluşturma sürecini izlemek için görev tanımlayıcı | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3B model dosyası | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
