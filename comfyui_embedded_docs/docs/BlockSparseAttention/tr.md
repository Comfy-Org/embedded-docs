# Model Seyrek Dikkat

**Block Sparse Attention** düğümü, dikkat katmanları tüm girdiye aynı anda odaklanmak yerine yalnızca girdinin en ilgili kısımlarına odaklanacak şekilde bir modeli değiştirir; bu, uzun diziler için gereken hesaplama işini azaltır. Tasarruf, dizi uzunluğuyla birlikte artar; çünkü kısa diziler genellikle normal (yoğun) dikkat ile daha hızlıdır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yamalanacak model. | MODEL | Evet | N/A |
| `selection` | Tam token düzeyinde dikkat için anahtar bloklarını seçmekte kullanılan yöntem (`method` olarak görüntülenir). <br>`sol-attn`: Sparsifying Online Attention, her dikkat başlığı ve sorgu bloğu için eğitim gerektirmeyen uyarlanabilir bir eşik kullanır.<br>`sla`: Sparse-Linear Attention, en yüksek puanlı anahtar bloklarının sabit bir yüzdesini korur; yalnızca bu desen için eğitilmiş model ağırlıklarıyla kullanın.<br>`vsa`: Video Sparse Attention (FastVideo), 3B video-küp döşeme ve öğrenilmiş kaba bir dikkat dalı kullanır; FastH3 model ağırlıkları gerektirir. | DYNAMIC_COMBO | Evet | `"sol-attn"`<br>`"sla"`<br>`"vsa"` |
| `start_percent` | Seyrek dikkatin başladığı yüzde noktası. Bu noktadan önce dikkat yoğun kalır. Varsayılan: 0.2. | FLOAT | Hayır | min: 0.0, max: 1.0, step: 0.01 |
| `end_percent` | Seyrek dikkatin bittiği yüzde noktası. Bu noktadan sonra dikkat yoğunluğa döner. Varsayılan: 1.0. | FLOAT | Hayır | min: 0.0, max: 1.0, step: 0.01 |
| `dense_blocks` | Her zaman yoğun çalışan Transformer blokları, örn. '0, 1, 47-49'. Varsayılan: "" (boş). Gelişmiş girdi. | STRING | Hayır | Varsayılan: "" |
| `min_tokens` | Bundan daha kısa diziler yoğun kalır. Varsayılan: 12288. Gelişmiş girdi. | INT | Hayır | min: 0, max: 1048576, step: 512 |
| `extra_tokens` | Her sorgu bloğunun seçili bloklarının ötesinde dikkat ettiği ek en yüksek puanlı tokenlar. Daha fazla dikkat süresi için yoğuna yaklaşır; 256 önerilir, 0 devre dışı bırakır. VSA için yok sayılır. Varsayılan: 256. Gelişmiş girdi. | INT | Hayır | min: 0, max: 256, step: 64 |
| `sink_conditioning` | Yalnızca MiniMax-H3. `exact_kv`: her sorgu, paketlenmiş metin/ses/referans satırlarına tam olarak dikkat eder (yaklaşık %3 maliyet). `exact_kv_and_rows`: ek olarak hedef ses sorgu satırlarını yoğun çalıştırır (üretilen sesi bozulmadan korur). `off` bu davranışı devre dışı bırakır. Varsayılan: "exact_kv_and_rows". Gelişmiş girdi. | COMBO | Hayır | `"exact_kv"`<br>`"exact_kv_and_rows"`<br>`"off"` |
| `verbose` | Her dikkat biçiminin seyrek dikkat kullanıp kullanmadığını veya neden yoğun kaldığını günlüğe kaydeder. Varsayılan: False. Gelişmiş girdi. | BOOLEAN | Hayır | Varsayılan: False |

### sol-attn Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `tau` | Puan dağılımı sigmalarında eşik. Daha yüksek değer daha seyrektir: 1.0, anahtar bloklarının yaklaşık %16'sını tam tutar; 1.5 yaklaşık %7'sini; 2.0 yaklaşık %2.7'sini. Varsayılan: 1.3. | FLOAT | Hayır | min: 0.0, max: 4.0, step: 0.05 |

### sla Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `keep_percent` | Her sorgu bloğunun tam olarak tuttuğu anahtar bloklarının yüzdesi (sink'ler ve köşegen bunun üzerine eklenir). Seçim, SLA tarzı LoRA'ların damıtıldığı hedeftir; böyle bir LoRA olmadan daha yüksek değer yoğuna daha yakındır. Varsayılan: 10.0. | FLOAT | Hayır | min: 0.5, max: 95.0, step: 0.5 |

### vsa Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `keep_percent` | Her sorgu küpünün tuttuğu video küplerinin yüzdesi; FastH3-VSA kontrol noktaları 10 ile eğitilmiştir. Mevcut olduğunda kaba dal için modelin `to_gate_compress` katmanlarını kullanır. Varsayılan: 10.0. | FLOAT | Hayır | min: 0.5, max: 95.0, step: 0.5 |

**Not:** Arayüzde yalnızca seçili yönteme ait parametreler gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Blok seyrek dikkat uygulanmış model. | MODEL |

## Kısıtlamalar ve Sınırlamalar

- `min_tokens` değerinden kısa diziler, `dense_blocks` içinde listelenen bloklar ve `start_percent` ile `end_percent` aralığının dışındaki örnekleme adımları, Model Attention Backend düğümü tarafından seçilen yoğun model dikkat arka ucuna geri döner.
- `vsa` yöntemi seçildiğinde `extra_tokens` yok sayılır. VSA ağırlıkları kendi seyrek desenlerine karşı eğitildiği için bir mesaj günlüğe kaydedilir.
- `vsa` yöntemi bir MiniMax-H3 modeli gerektirir; başka herhangi bir model hata verir. Modelde `to_gate_compress` katmanları yoksa, ince aşama kaba dal olmadan çalışır ve bir uyarı günlüğe kaydedilir.
- Blok indekslerini bildirmeyen modeller için `dense_blocks` yok sayılır; bu, `verbose` etkinleştirildiğinde günlüğe not edilir.
- `sink_conditioning` yalnızca geçerli dizi uzunluğuyla eşleşen bir düzen bildiren MiniMax-H3 modelleri için geçerlidir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/tr.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
