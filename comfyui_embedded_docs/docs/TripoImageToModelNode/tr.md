TripoImageToModelNode düğümü, Tripo'nun API'sini kullanarak tek bir görüntüye dayalı olarak eşzamanlı 3D modeller üretir. Bu düğüm, bir giriş görüntüsü alır ve doku, kalite ve model özellikleri için çeşitli özelleştirme seçenekleriyle bunu bir 3D modele dönüştürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | 3D model oluşturmak için kullanılan giriş görüntüsü | IMAGE | Evet | - |
| `model_sürümü` | Oluşturma için kullanılacak Tripo modelinin sürümü | COMBO | Hayır | Birden çok seçenek mevcut |
| `stil` | Oluşturulan model için stil ayarı (varsayılan: "Yok") | COMBO | Hayır | Birden çok seçenek mevcut |
| `doku` | Model için doku oluşturulup oluşturulmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `pbr` | Fiziksel Tabanlı İşleme (PBR) kullanılıp kullanılmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `model_tohumu` | Model oluşturma için rastgele tohum değeri (varsayılan: 42) | INT | Hayır | - |
| `yönlendirme` | Oluşturulan model için yönlendirme ayarı | COMBO | Hayır | Birden çok seçenek mevcut |
| `doku_tohumu` | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) | INT | Hayır | - |
| `doku_kalitesi` | Doku oluşturma için kalite seviyesi (varsayılan: "standard") | COMBO | Hayır | "standard"<br>"detailed" |
| `doku_hizalama` | Doku eşleme için hizalama yöntemi (varsayılan: "original_image") | COMBO | Hayır | "original_image"<br>"geometry" |
| `yüz_sınırı` | Oluşturulan modeldeki maksimum yüz sayısı, -1 sınırsız anlamına gelir (varsayılan: -1) | INT | Hayır | -1 ila 500000 |
| `dörtlü` | Üçgenler yerine dörtgen yüzler kullanılıp kullanılmayacağı (varsayılan: False) | BOOLEAN | Hayır | - |
| `geometry_quality` | Geometri oluşturma için kalite seviyesi (varsayılan: "standard") | COMBO | Hayır | "standard"<br>"detailed" |

**Not:** `image` parametresi zorunludur ve düğümün çalışması için sağlanmalıdır. Hiçbir görüntü sağlanmazsa, düğüm bir RuntimeError (Çalışma Zamanı Hatası) yükseltecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_görev_id` | Oluşturulan 3D model dosyası (yalnızca geriye dönük uyumluluk için) | STRING |
| `GLB` | Model oluşturma sürecini izlemek için görev kimliği | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3D model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
