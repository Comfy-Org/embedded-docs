# Recraft V4 Metinden Görsele

Bu düğüm, Recraft V4 ve V4.1 yapay zeka modellerini kullanarak metin açıklamalarından görüntüler üretir. İstemi ve üretim ayarlarını Recraft görüntü üretim hizmetine gönderir ve ortaya çıkan görüntüyü veya görüntüleri döndürür. Modeli, görüntü boyutunu ve üretilecek görüntü sayısını seçebilirsiniz.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak model. Bir model seçmek, kullanılabilir `size` seçeneklerini belirler. | DYNAMIC_COMBO | Evet | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Görüntü üretimi için istem. En fazla 10.000 karakter. | STRING | Evet | 1 ila 10000 karakter |
| `negative_prompt` | Bu girdi yok sayılır: negatif istem, Recraft V4 ve V4.1 modelleri tarafından desteklenmez. | STRING | Evet | N/A |
| `n` | Üretilecek görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ila 6 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ila 18446744073709551615 |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | N/A |

### recraftv4_1, recraftv4_1_utility ve recraftv4 Girdileri

Bu girdiler `recraftv4_1`, `recraftv4_1_utility` ve `recraftv4` modelleri tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Üretilen görüntünün boyutu (varsayılan: 1024x1024). | COMBO | Evet | Birden çok seçenek mevcuttur (standart Recraft V4 boyutları) |

### recraftv4_1_pro, recraftv4_1_utility_pro ve recraftv4_pro Girdileri

Bu girdiler `recraftv4_1_pro`, `recraftv4_1_utility_pro` ve `recraftv4_pro` modelleri tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Üretilen görüntünün boyutu (varsayılan: 2048x2048). | COMBO | Evet | Birden çok seçenek mevcuttur (Pro Recraft V4 boyutları) |

**Notlar:**

- `size` girdisi bir model seçildiğinde görünür ve kullanılabilir seçenekler modele bağlıdır: standart modeller (`recraftv4_1`, `recraftv4_1_utility`, `recraftv4`) aynı boyut kümesini paylaşırken, Pro modeller (`recraftv4_1_pro`, `recraftv4_1_utility_pro`, `recraftv4_pro`) farklı bir küme paylaşır.
- `negative_prompt` girdisi arayüzde gösterilir ancak modele gönderilmez; negatif istemler Recraft V4 ve V4.1 modelleri tarafından desteklenmez.
- `seed` değeri yalnızca değer değiştiğinde düğümün yeniden çalıştırılıp çalıştırılmayacağını belirler; gerçek görüntü sonuçları tohum değerinden bağımsız olarak deterministik değildir.
- Recraft Controls girdisi aracılığıyla Infinite Style Library'den bir stil kimliği kullanıyorsanız, bunun Vector art stili olmadığından emin olun; aksi takdirde görüntü yerine SVG verisi dönebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen görüntü veya görüntü grubu. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
