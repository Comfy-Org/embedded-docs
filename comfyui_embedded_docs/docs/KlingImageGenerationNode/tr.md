# Kling Görüntü Oluşturma

Kling Görüntü Oluşturma Düğümü, metin istemlerinden görüntüler oluşturur ve isteğe bağlı olarak rehberlik için bir referans görüntüsü kullanma seçeneği sunar. Metin açıklamanıza ve referans ayarlarınıza bağlı olarak bir veya daha fazla görüntü oluşturur ve ardından oluşturulan görüntüleri çıktı olarak döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Olumlu metin istemi | STRING | Evet | - |
| `negatif_istem` | Olumsuz metin istemi | STRING | Evet | - |
| `görüntü_türü` | Görüntü referans türü seçimi (gelişmiş). Bir referans görüntüsü sağlandığında gereklidir. | COMBO | Evet | `"subject_reference"`<br>`"style_reference"` |
| `görüntü_sadakati` | Kullanıcı tarafından yüklenen görüntüler için referans yoğunluğu (varsayılan: 0.5, gelişmiş) | FLOAT | Evet | 0.0 - 1.0 |
| `insan_sadakati` | Konu referans benzerliği (varsayılan: 0.45, gelişmiş) | FLOAT | Evet | 0.0 - 1.0 |
| `model_adı` | Görüntü oluşturma için model seçimi (varsayılan: "kling-v3") | COMBO | Evet | `"kling-v3"`<br>`"kling-v2"`<br>`"kling-v1-5"` |
| `en_boy_oranı` | Oluşturulan görüntüler için en-boy oranı (varsayılan: "16:9") | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Oluşturulan görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 9 |
| `görüntü` | İsteğe bağlı referans görüntüsü | IMAGE | Hayır | - |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |

**Parametre Kısıtlamaları:**

- `image` parametresi isteğe bağlıdır. Bir referans görüntüsü sağlandığında, `image_type` parametresi `"subject_reference"` veya `"style_reference"` olarak ayarlanmalıdır.
- Referans görüntüsü sağlanmadığında, `image_type`, `image_fidelity` ve `human_fidelity` parametreleri kullanılmaz.
- İstem ve olumsuz istemin maksimum uzunluğu `MAX_PROMPT_LENGTH_IMAGE_GEN` karakterdir.
- `seed` parametresi isteğe bağlıdır ve deterministik sonuçları garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Giriş parametrelerine göre oluşturulan görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/tr.md)

---
**Source fingerprint (SHA-256):** `f25164f4007b1f62285e76519238b5061b63597e1a06365acf93d4289063bd3a`
