# Recraft V4 Metinden Vektöre

Recraft V4 Text to Vector düğümü, bir metin açıklamasından Ölçeklenebilir Vektör Grafikleri (SVG) illüstrasyonları üretir. Recraft API'ye bağlanarak Recraft V4 ve V4.1 modellerini kullanarak görüntüler üretir ve isteminize bağlı olarak bir veya daha fazla SVG dosyası çıkarır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak model. Model seçmek, kullanılabilir `size` seçeneklerini değiştirir. | DYNAMIC_COMBO | Evet | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Görüntü üretimi için istem. Maksimum 10.000 karakter. | STRING | Evet | N/A |
| `negative_prompt` | Bu girdi yok sayılır: negatif istem, Recraft V4 ve V4.1 modelleri tarafından desteklenmez. | STRING | Evet | N/A |
| `n` | Oluşturulacak görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ila 6 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak belirlenemezdir (varsayılan: 0). | INT | Evet | 0 ila 18446744073709551615 |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | N/A |

### recraftv4_1_vector, recraftv4_1_utility_vector ve recraftv4 Girdileri

Bu modeller aynı `size` seçeneklerini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Oluşturulan görüntünün boyutu. Varsayılan: `"1024x1024"`. | COMBO | Evet | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector ve recraftv4_pro Girdileri

Bu modeller aynı `size` seçeneklerini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Oluşturulan görüntünün boyutu. Varsayılan: `"2048x2048"`. | COMBO | Evet | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**Not:** `size` parametresi, kullanılabilir seçenekleri seçilen `model`e göre değişen dinamik bir girdidir. `seed` değeri, harici API'den tekrarlanabilir sonuçlar garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan Ölçeklenebilir Vektör Grafikleri (SVG) görüntüsü/görüntüleri. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/tr.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
