> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/tr.md)

TripoImageToModelNode düğümü, Tripo'nun API'sini kullanarak tek bir görüntüye dayalı olarak eşzamanlı 3D modeller üretir. Bu düğüm, bir giriş görüntüsü alır ve doku, kalite ve model özellikleri için çeşitli özelleştirme seçenekleriyle bunu bir 3D modele dönüştürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | 3D model oluşturmak için kullanılan giriş görüntüsü |
| `model_sürümü` | COMBO | Hayır | Birden çok seçenek mevcut | Oluşturma için kullanılacak Tripo modelinin sürümü |
| `stil` | COMBO | Hayır | Birden çok seçenek mevcut | Oluşturulan model için stil ayarı (varsayılan: "Yok") |
| `doku` | BOOLEAN | Hayır | - | Model için doku oluşturulup oluşturulmayacağı (varsayılan: True) |
| `pbr` | BOOLEAN | Hayır | - | Fiziksel Tabanlı İşleme (PBR) kullanılıp kullanılmayacağı (varsayılan: True) |
| `model_tohumu` | INT | Hayır | - | Model oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `yönlendirme` | COMBO | Hayır | Birden çok seçenek mevcut | Oluşturulan model için yönlendirme ayarı |
| `doku_tohumu` | INT | Hayır | - | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `doku_kalitesi` | COMBO | Hayır | "standard"<br>"detailed" | Doku oluşturma için kalite seviyesi (varsayılan: "standard") |
| `doku_hizalama` | COMBO | Hayır | "original_image"<br>"geometry" | Doku eşleme için hizalama yöntemi (varsayılan: "original_image") |
| `yüz_sınırı` | INT | Hayır | -1 ila 500000 | Oluşturulan modeldeki maksimum yüz sayısı, -1 sınırsız anlamına gelir (varsayılan: -1) |
| `dörtlü` | BOOLEAN | Hayır | - | Üçgenler yerine dörtgen yüzler kullanılıp kullanılmayacağı (varsayılan: False) |
| `geometry_quality` | COMBO | Hayır | "standard"<br>"detailed" | Geometri oluşturma için kalite seviyesi (varsayılan: "standard") |

**Not:** `image` parametresi zorunludur ve düğümün çalışması için sağlanmalıdır. Hiçbir görüntü sağlanmazsa, düğüm bir RuntimeError (Çalışma Zamanı Hatası) yükseltecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_görev_id` | STRING | Oluşturulan 3D model dosyası (yalnızca geriye dönük uyumluluk için) |
| `GLB` | MODEL_TASK_ID | Model oluşturma sürecini izlemek için görev kimliği |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3D model |

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
