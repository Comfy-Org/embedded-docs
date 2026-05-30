> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/tr.md)

## Genel Bakış

Bu düğüm, Tripo P1 API'sini kullanarak bir metin açıklamasından 3B model oluşturur. Düşük poli sayılı, oyuna hazır, kararlı topolojiye sahip ağlar oluşturmak için optimize edilmiştir ve gerçek zamanlı uygulamalar için uygundur.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | 1024 karaktere kadar | Oluşturmak istediğiniz 3B modelin metin açıklaması. |
| `negative_prompt` | STRING | Hayır | 255 karaktere kadar | Oluşturulan modelde istemediğiniz şeylerin metin açıklaması. |
| `output_mode` | DICT | Evet | Açıklamaya bakın | Çıktı modelinin kalitesini ve doku ayarlarını kontrol eder. Bu parametre aşağıdaki anahtarlara sahip bir sözlüktür:<br><br>`texture_quality`: STRING, Aralık: `"standard"`<br>`pbr`: BOOLEAN, varsayılan: True<br>`texture`: BOOLEAN, varsayılan: True<br>`subdivision`: INT, varsayılan: 0, Aralık: 0 ile 2 arası<br>`texture_size`: INT, varsayılan: 2048, Aralık: 512 ile 4096 arası (2'nin katı olmalıdır)<br>`texture_format`: STRING, Aralık: `"png"`<br>`texture_clean`: BOOLEAN, varsayılan: False<br>`texture_seamless`: BOOLEAN, varsayılan: False<br><br>Varsayılan: `{"texture_quality": "standard", "pbr": True, "texture": True, "subdivision": 0, "texture_size": 2048, "texture_format": "png", "texture_clean": False, "texture_seamless": False}` |
| `image_seed` | INT | Hayır |  | Görüntü oluşturma için rastgeleliği kontrol etmek amacıyla kullanılan bir tohum değeri. Varsayılan: 42. |
| `face_limit` | INT | Hayır |  | Oluşturulan ağ için maksimum yüz sayısı. -1 değeri sınır olmadığı anlamına gelir. Varsayılan: -1. |
| `model_seed` | INT | Hayır |  | Model oluşturma için rastgeleliği kontrol etmek amacıyla kullanılan bir tohum değeri. |
| `auto_size` | BOOLEAN | Hayır |  | Etkinleştirilirse, düğüm otomatik olarak en uygun model boyutunu belirler. Varsayılan: False. |
| `export_uv` | BOOLEAN | Hayır |  | Etkinleştirilirse, model doku haritalaması için UV koordinatlarını içerir. Varsayılan: True. |
| `compress_geometry` | BOOLEAN | Hayır |  | Etkinleştirilirse, dosya boyutunu azaltmak için geometri sıkıştırılır. Varsayılan: False. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan 3B modelin dosya yolu (yalnızca geriye dönük uyumluluk için). |
| `model task_id` | MODEL_TASK_ID | Model oluşturma isteği için benzersiz görev kimliği. |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3B model. |

---
**Source fingerprint (SHA-256):** `154e75209d65c823d5681b74cd12fe7b2ed37d7b94bf51cac86f343c68f85722`
