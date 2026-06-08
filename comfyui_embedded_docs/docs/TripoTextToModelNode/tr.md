Tripo'nun API'sini kullanarak bir metin istemine dayalı olarak eşzamanlı 3B modeller üretir. Bu düğüm, bir metin açıklaması alır ve isteğe bağlı doku ve malzeme özellikleriyle bir 3B model oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `istek` | 3B modelin oluşturulması için metin açıklaması (çok satırlı giriş) | STRING | Evet | - |
| `olumsuz_istek` | Oluşturulan modelde istenmeyen özelliklerin metin açıklaması (çok satırlı giriş) | STRING | Hayır | - |
| `model_versiyonu` | Oluşturma için kullanılacak Tripo modelinin sürümü (varsayılan: v2.5-20250123) | COMBO | Hayır | Birden çok seçenek mevcut |
| `stil` | Oluşturulan model için stil ayarı (varsayılan: "Yok") | COMBO | Hayır | Birden çok seçenek mevcut |
| `doku` | Model için doku oluşturulup oluşturulmayacağı (varsayılan: Doğru) | BOOLEAN | Hayır | - |
| `pbr` | PBR (Fizik Tabanlı İşleme) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: Doğru) | BOOLEAN | Hayır | - |
| `görüntü_tohumu` | Görüntü oluşturma için rastgele tohum değeri (varsayılan: 42) | INT | Hayır | - |
| `model_tohumu` | Model oluşturma için rastgele tohum değeri (varsayılan: 42) | INT | Hayır | - |
| `doku_tohumu` | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) | INT | Hayır | - |
| `doku_kalitesi` | Doku oluşturma için kalite seviyesi (varsayılan: "standart") | COMBO | Hayır | "standart"<br>"detaylı" |
| `yüz_sınırı` | Oluşturulan modeldeki maksimum yüz sayısı, sınırsız için -1 (varsayılan: -1) | INT | Hayır | -1 ila 2000000 |
| `dörtgen` | Üçgenler yerine dörtgen tabanlı geometri oluşturulup oluşturulmayacağı (varsayılan: Yanlış) | BOOLEAN | Hayır | - |
| `geometry_quality` | Geometri oluşturma için kalite seviyesi (varsayılan: "standart") | COMBO | Hayır | "standart"<br>"detaylı" |

**Not:** `prompt` parametresi zorunludur ve boş olamaz. İstem sağlanmazsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_görev_id` | Oluşturulan 3B model dosyası (yalnızca geriye dönük uyumluluk için) | STRING |
| `GLB` | Model oluşturma süreci için benzersiz görev tanımlayıcısı | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3B model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
