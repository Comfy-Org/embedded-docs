# Recraft V4 Metinden Görsele

Bu düğüm, Recraft V4 ve V4.1 AI modellerini kullanarak metin açıklamalarından görüntüler üretir. İsteminizi harici bir API'ye gönderir ve üretilen görüntüleri döndürür. Modeli, görüntü boyutunu ve oluşturulacak görüntü sayısını belirterek çıktıyı kontrol edebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Üretim için kullanılacak model. | DYNAMIC_COMBO | Evet | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Görüntü üretimi için istem. En fazla 10.000 karakter. | STRING | Evet | YOK |
| `negative_prompt` | Bu girdi yok sayılır: negatif istem, Recraft V4 ve V4.1 modelleri tarafından desteklenmez. | STRING | Evet | YOK |
| `n` | Oluşturulacak görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ila 6 |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak belirleyici değildir (varsayılan: 0). | INT | Evet | 0 ila 18446744073709551615 |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | YOK |

### recraftv4_1, recraftv4_1_utility ve recraftv4 Girdileri

`recraftv4_1`, `recraftv4_1_utility` ve `recraftv4` tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Oluşturulan görüntünün boyutu (varsayılan: "1024x1024"). | COMBO | Evet | Birden çok seçenek mevcuttur (standart Recraft V4 boyutları, "1024x1024" dahil) |

### recraftv4_1_pro, recraftv4_1_utility_pro ve recraftv4_pro Girdileri

`recraftv4_1_pro`, `recraftv4_1_utility_pro` ve `recraftv4_pro` tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Oluşturulan görüntünün boyutu (varsayılan: "2048x2048"). | COMBO | Evet | Birden çok seçenek mevcuttur (pro Recraft V4 boyutları, "2048x2048" dahil) |

**Not:** `size` parametresi, seçenekleri seçilen `model`e göre değişen dinamik bir girdidir. `seed` değeri tekrarlanabilir görüntü çıktılarını garanti etmez. Infinite Style Library'den bir stil kimliği kullanıyorsanız, bunun bir Vektör sanat stili olmadığından emin olun; aksi takdirde görüntü yerine SVG verisi dönebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan görüntü veya görüntü grubu. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
