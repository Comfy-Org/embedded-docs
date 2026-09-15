# Kling Görüntü Oluşturma

Kling Görüntü Üretme Düğümü, metin istemlerinden görüntüler üretir ve rehberlik için referans görüntü kullanma seçeneği sunar. Metin açıklamanıza ve referans ayarlarınıza göre bir veya daha fazla görüntü oluşturur, ardından üretilen görüntüleri çıktı olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Pozitif metin istemi. Gerekli, 1 ile 500 karakter arasında olmalıdır. | STRING | Evet | Maksimum 500 karakter |
| `negatif_istem` | Negatif metin istemi. | STRING | Evet | Maksimum 500 karakter |
| `görüntü_türü` | Görüntü referans türü seçimi (gelişmiş). Referans görüntü sağlandığında gereklidir. | COMBO | Evet | `"subject_reference"`<br>`"style_reference"` |
| `görüntü_sadakati` | Kullanıcı tarafından yüklenen görüntüler için referans yoğunluğu (varsayılan: 0.5, gelişmiş) | FLOAT | Evet | 0.0 - 1.0 |
| `insan_sadakati` | Özne referansı benzerliği (varsayılan: 0.45, gelişmiş) | FLOAT | Evet | 0.0 - 1.0 |
| `model_adı` | Görüntü üretimi için model seçimi (varsayılan: "kling-v3") | COMBO | Evet | `"kling-v3"` |
| `en_boy_oranı` | Üretilen görüntüler için en-boy oranı (varsayılan: "16:9") | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Üretilen görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 9 |
| `görüntü` | İsteğe bağlı referans görüntü | IMAGE | Hayır | - |
| `seed` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |

**Parametre Kısıtlamaları:**

- `image` parametresi isteğe bağlıdır. Bir referans görüntü sağlandığında, `image_type` parametresi referansın özne referansı olarak mı yoksa stil referansı olarak mı kullanılacağını belirler.
- Referans görüntü sağlanmadığında, referansla ilgili ayarların (`image_type`, `image_fidelity`, `human_fidelity`) sonuç üzerinde etkisi yoktur.
- `prompt` ve `negative_prompt` en fazla 500 karakter uzunluğundadır.
- `seed` parametresi isteğe bağlıdır ve deterministik sonuçları garanti etmez.
- `n` parametresi kaç görüntü üretileceğini kontrol eder ve ayrıca isteğin fiyatını belirler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Girdi parametrelerine göre üretilen görüntü(ler). `n` 1'den büyük olduğunda, birden fazla görüntü toplu olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/tr.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
