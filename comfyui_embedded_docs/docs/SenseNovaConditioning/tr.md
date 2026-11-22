# SenseNova Conditioning

SenseNova koşullandırmasını görüntü oluşturma veya iç içe metin ve görüntü çıktısı için hazırlayın. `task` seçicisi istem şablonunu ve durma davranışını ayarlar; düğüm, modelin bir görüntü isteyip istemediğini bildirir, böylece bir döngü örnekleyicinin ne zaman çalıştırılacağını bilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `clip` | SenseNova CLIP modeli. CLIP Text Encode’u da besleyen CLIP yükleyicisini bağlayın; kodlayıcı çıktısı `conditioning` girişine gider. Gelen koşullandırma zaten tamamlanmış olduğu durumlar hariç her görev için gereklidir. | CLIP | Hayır | - |
| `koşullandırma` | CLIP Text Encode'dan gelen SenseNova metin koşullandırması. | CONDITIONING | Evet | - |
| `negatif` | İsteğe bağlı negatif koşullandırma. `interleave` ve `self-correction` görevleri için güncellenir ve döndürülür. | CONDITIONING | Hayır | - |
| `görev` | Çalıştırılacak görev. `"image"` standart bir örnekleyici için istemi kodlar, `"image thinking"` modelin yanıtlamadan önce düşünmesini sağlar, `"interleave"` tek geçişte metin ve görüntüler üretir ve `"self-correction"` modelin kendi önceki çıktısını düzeltmesini sağlar. | DYNAMIC_COMBO | Evet | `"image"`<br>`"image thinking"`<br>`"interleave"`<br>`"self-correction"` |
| `max_tokens` | Bu çağrı sırasında üretilen maksimum token sayısı. Varsayılan: 1024. | INT | Evet | 1 ile 8192 arası |

### `interleave` Girdileri

`task` değeri `"interleave"` olarak ayarlandığında bu girdiler görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `thinking` | Modelin yanıtlamadan önce düşünmesini sağlar. Varsayılan: True. | BOOLEAN | Evet | True<br>False |
| `samples` | Önceki örnekleyici çıktısı; bir görüntü isteğinden sonra devam edilirken bağlanır. | LATENT | Hayır | - |

### `self-correction` Girdileri

`task` değeri `"self-correction"` olarak ayarlandığında bu girdiler görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `samples` | Önceki örnekleyici çıktısı; bir görüntü isteğinden sonra devam edilirken bağlanır. | LATENT | Hayır | - |

**Kısıtlamalar ve davranış:**

* `clip` girdisi CLIP Text Encode çıktısını (o `CONDITIONING`'dir) değil, SenseNova CLIP modelinin kendisini alır. `clip` yoksa (gelen koşullandırma zaten tamamlanmışsa hariç) veya SenseNova CLIP değilse düğüm hata verir.
* `"image thinking"` tam olarak bir pozitif koşullandırma girdisi gerektirir; `"interleave"` ve `"self-correction"` bir pozitif ve bir negatif girdi gerektirir.
* Model bir görüntü beklerken, önceki örnekleyicinin LATENT çıktısını `samples` girdisine bağlayın. Bir görüntü istenmeden önce `samples` geçirmek hatadır.
* Gelen koşullandırma zaten tamamlanmışsa düğüm, boş bir `generated_text` ve False değerine ayarlanmış `image_requested` ile onu değiştirmeden döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `conditioning` | Örnekleyici için koşullandırma; bu çağrıda üretilen metinle genişletilir. | CONDITIONING |
| `generated_text` | Bu çağrıda üretilen metin. Tam sonuç için SenseNova Interleave Decode kullanın. | STRING |
| `negative` | `interleave` ve `self-correction` görevleri için güncellenmiş negatif koşullandırma. | CONDITIONING |
| `image_requested` | Model bir görüntü istediğinde True: örnekleyiciyi çalıştırın, ardından döngüyü bu düğüme geri besleyin. | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `97fcdc26ccf80f48c5628f695a4ae8231b065b67414c93dec9bced6bb8d4c77c`
