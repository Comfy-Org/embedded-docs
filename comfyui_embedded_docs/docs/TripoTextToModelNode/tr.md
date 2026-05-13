> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/tr.md)

Tripo'nun API'sini kullanarak bir metin istemine dayalı olarak eşzamanlı 3B modeller üretir. Bu düğüm, bir metin açıklaması alır ve isteğe bağlı doku ve malzeme özellikleriyle bir 3B model oluşturur.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `istek` | STRING | Evet | - | 3B modelin oluşturulması için metin açıklaması (çok satırlı giriş) |
| `olumsuz_istek` | STRING | Hayır | - | Oluşturulan modelde istenmeyen özelliklerin metin açıklaması (çok satırlı giriş) |
| `model_versiyonu` | COMBO | Hayır | Birden çok seçenek mevcut | Oluşturma için kullanılacak Tripo modelinin sürümü (varsayılan: v2.5-20250123) |
| `stil` | COMBO | Hayır | Birden çok seçenek mevcut | Oluşturulan model için stil ayarı (varsayılan: "Yok") |
| `doku` | BOOLEAN | Hayır | - | Model için doku oluşturulup oluşturulmayacağı (varsayılan: Doğru) |
| `pbr` | BOOLEAN | Hayır | - | PBR (Fizik Tabanlı İşleme) malzemelerinin oluşturulup oluşturulmayacağı (varsayılan: Doğru) |
| `görüntü_tohumu` | INT | Hayır | - | Görüntü oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `model_tohumu` | INT | Hayır | - | Model oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `doku_tohumu` | INT | Hayır | - | Doku oluşturma için rastgele tohum değeri (varsayılan: 42) |
| `doku_kalitesi` | COMBO | Hayır | "standart"<br>"detaylı" | Doku oluşturma için kalite seviyesi (varsayılan: "standart") |
| `yüz_sınırı` | INT | Hayır | -1 ila 2000000 | Oluşturulan modeldeki maksimum yüz sayısı, sınırsız için -1 (varsayılan: -1) |
| `dörtgen` | BOOLEAN | Hayır | - | Üçgenler yerine dörtgen tabanlı geometri oluşturulup oluşturulmayacağı (varsayılan: Yanlış) |
| `geometry_quality` | COMBO | Hayır | "standart"<br>"detaylı" | Geometri oluşturma için kalite seviyesi (varsayılan: "standart") |

**Not:** `prompt` parametresi zorunludur ve boş olamaz. İstem sağlanmazsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model_görev_id` | STRING | Oluşturulan 3B model dosyası (yalnızca geriye dönük uyumluluk için) |
| `GLB` | MODEL_TASK_ID | Model oluşturma süreci için benzersiz görev tanımlayıcısı |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3B model |

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
