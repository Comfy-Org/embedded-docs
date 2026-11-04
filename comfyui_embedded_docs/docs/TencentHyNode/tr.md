# Tencent HY

Bu düğüm, Tencent'in Hy4 modeliyle metin yanıtları üretir. Bir metin istemi ve isteğe bağlı olarak bağlam görevi gören bir veya daha fazla görüntü gönderir ve modelin yanıtını metin olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan model. Seçildiğinde ilgili girdiler aşağıda görünür. Varsayılan: `"Hy4"`. | DYNAMIC_COMBO | Evet | `"Hy4"` |

### Hy4 Girdileri

Bu girdiler, `model` değeri `"Hy4"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele gönderilecek mesaj. Boş olmamalıdır. Varsayılan: "" (boş dize). | STRING | Evet | En az 1 karakter |
| `images` | En fazla 20 görüntü. Bir toplu işteki her görüntü sayılır. Varsayılan: görüntü yok. | AUTOGROW | Hayır | 0 ile 20 görsel arası |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. Varsayılan: "" (boş dize). | STRING | Hayır | - |
| `reasoning` | Model, yanıtlamadan önce düşünür. Yanıtlar daha uzun sürer ve daha fazla token kullanır; çok zor görevler zaman aşımına uğrayabilir. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `temperature` | Rastgeleliği kontrol eder. Sonuçlar 0 değerinde bile değişiklik gösterir. Varsayılan: 1.0. | FLOAT | Evet | 0.0 ile 1.4 arası (adım: 0.01) |
| `max_tokens` | Üretilecek maksimum token sayısı; `reasoning` açıkken akıl yürütme token'ları dahil. Çok uzun yanıtlar zaman aşımına uğrayabilir. Varsayılan: 32000. | INT | Evet | 1 ile 64000 arası |

**Kısıtlamalar:**

* İstek başına en fazla 20 görüntü kabul edilir; bir toplu işteki her görüntü sayılır.
* Tencent'in içerik filtresi bir isteği engelleyebilir ve bu bir hata oluşturur.
* Yanıt tamamlanmadan `max_tokens` tükenirse düğüm bir hata verir: `max_tokens` değerini artırın veya `reasoning` seçeneğini kapatın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | Hy4 modelinden gelen metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentHyNode/tr.md)

---
**Source fingerprint (SHA-256):** `c7c1d2908d2fba8172fa279b7d273f5f3f96cf10b531f81650824fc8e0176f21`
