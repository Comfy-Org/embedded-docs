> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/tr.md)

Kling Görüntü Oluşturma Düğümü, metin istemlerinden görüntüler oluşturur ve isteğe bağlı olarak rehberlik için bir referans görüntüsü kullanma seçeneği sunar. Metin açıklamanıza ve referans ayarlarınıza bağlı olarak bir veya daha fazla görüntü oluşturur ve ardından oluşturulan görüntüleri çıktı olarak döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Olumlu metin istemi |
| `negative_prompt` | STRING | Evet | - | Olumsuz metin istemi |
| `image_type` | COMBO | Evet | `"subject_reference"`<br>`"style_reference"` | Görüntü referans türü seçimi (gelişmiş). Bir referans görüntüsü sağlandığında gereklidir. |
| `image_fidelity` | FLOAT | Evet | 0.0 - 1.0 | Kullanıcı tarafından yüklenen görüntüler için referans yoğunluğu (varsayılan: 0.5, gelişmiş) |
| `human_fidelity` | FLOAT | Evet | 0.0 - 1.0 | Konu referans benzerliği (varsayılan: 0.45, gelişmiş) |
| `model_name` | COMBO | Evet | `"kling-v3"`<br>`"kling-v2"`<br>`"kling-v1-5"` | Görüntü oluşturma için model seçimi (varsayılan: "kling-v3") |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | Oluşturulan görüntüler için en-boy oranı (varsayılan: "16:9") |
| `n` | INT | Evet | 1 - 9 | Oluşturulan görüntü sayısı (varsayılan: 1) |
| `image` | IMAGE | Hayır | - | İsteğe bağlı referans görüntüsü |
| `seed` | INT | Hayır | 0 - 2147483647 | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) |

**Parametre Kısıtlamaları:**

- `image` parametresi isteğe bağlıdır. Bir referans görüntüsü sağlandığında, `image_type` parametresi `"subject_reference"` veya `"style_reference"` olarak ayarlanmalıdır.
- Referans görüntüsü sağlanmadığında, `image_type`, `image_fidelity` ve `human_fidelity` parametreleri kullanılmaz.
- İstem ve olumsuz istemin maksimum uzunluğu `MAX_PROMPT_LENGTH_IMAGE_GEN` karakterdir.
- `seed` parametresi isteğe bağlıdır ve deterministik sonuçları garanti etmez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Giriş parametrelerine göre oluşturulan görüntü(ler) |

---
**Source fingerprint (SHA-256):** `f25164f4007b1f62285e76519238b5061b63597e1a06365acf93d4289063bd3a`
