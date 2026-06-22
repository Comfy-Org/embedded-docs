# Tripo P1: Metinden Modele

## Genel Bakış

Bu düğüm, Tripo P1 API'sini kullanarak bir metin açıklamasından 3B model oluşturur. Düşük poli sayılı, oyuna hazır, kararlı topolojiye sahip ağlar oluşturmak için optimize edilmiştir ve gerçek zamanlı uygulamalar için uygundur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Oluşturmak istediğiniz 3B modelin metin açıklaması. | STRING | Evet | 1024 karaktere kadar |
| `negatif_istem` | Oluşturulan modelde istemediğiniz şeylerin metin açıklaması. | STRING | Hayır | 255 karaktere kadar |
| `çıktı_modu` | Çıktı modelinin kalitesini ve doku ayarlarını kontrol eder. Bu parametre aşağıdaki anahtarlara sahip bir sözlüktür:<br><br>`texture_quality`: STRING, Aralık: `"standard"`<br>`pbr`: BOOLEAN, varsayılan: True<br>`texture`: BOOLEAN, varsayılan: True<br>`subdivision`: INT, varsayılan: 0, Aralık: 0 ile 2 arası<br>`texture_size`: INT, varsayılan: 2048, Aralık: 512 ile 4096 arası (2'nin katı olmalıdır)<br>`texture_format`: STRING, Aralık: `"png"`<br>`texture_clean`: BOOLEAN, varsayılan: False<br>`texture_seamless`: BOOLEAN, varsayılan: False<br><br>Varsayılan: `{"texture_quality": "standard", "pbr": True, "texture": True, "subdivision": 0, "texture_size": 2048, "texture_format": "png", "texture_clean": False, "texture_seamless": False}` | DICT | Evet | Açıklamaya bakın |
| `görüntü_tohumu` | Görüntü oluşturma için rastgeleliği kontrol etmek amacıyla kullanılan bir tohum değeri. Varsayılan: 42. | INT | Hayır |  |
| `yüz_sınırı` | Oluşturulan ağ için maksimum yüz sayısı. -1 değeri sınır olmadığı anlamına gelir. Varsayılan: -1. | INT | Hayır |  |
| `model_tohumu` | Model oluşturma için rastgeleliği kontrol etmek amacıyla kullanılan bir tohum değeri. | INT | Hayır |  |
| `otomatik_boyut` | Etkinleştirilirse, düğüm otomatik olarak en uygun model boyutunu belirler. Varsayılan: False. | BOOLEAN | Hayır |  |
| `uv_dışa_aktar` | Etkinleştirilirse, model doku haritalaması için UV koordinatlarını içerir. Varsayılan: True. | BOOLEAN | Hayır |  |
| `geometriyi_sıkıştır` | Etkinleştirilirse, dosya boyutunu azaltmak için geometri sıkıştırılır. Varsayılan: False. | BOOLEAN | Hayır |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_görev_id` | Oluşturulan 3B modelin dosya yolu (yalnızca geriye dönük uyumluluk için). | STRING |
| `GLB` | Model oluşturma isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3B model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `154e75209d65c823d5681b74cd12fe7b2ed37d7b94bf51cac86f343c68f85722`
