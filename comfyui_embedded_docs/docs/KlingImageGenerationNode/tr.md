# Kling Görüntü Oluşturma

Kling Image Generation Node, metin istemlerinden görseller üretir ve isteğe bağlı olarak rehberlik için bir referans görsel kullanma seçeneği sunar. Metin açıklamanıza ve referans ayarlarınıza dayalı olarak bir veya daha fazla görsel oluşturur ve ardından üretilen görselleri çıktı olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Pozitif metin istemi | STRING | Evet | En fazla 500 karakter |
| `negatif_istem` | Negatif metin istemi | STRING | Evet | En fazla 500 karakter |
| `görüntü_türü` | Görsel referans türü seçimi (gelişmiş). Referans görsel sağlandığında gereklidir. | COMBO | Evet | `"subject_reference"`<br>`"style_reference"` |
| `görüntü_sadakati` | Kullanıcı tarafından yüklenen görseller için referans yoğunluğu (varsayılan: 0.5, gelişmiş) | FLOAT | Evet | 0.0 - 1.0 |
| `insan_sadakati` | Özne referansı benzerliği (varsayılan: 0.45, gelişmiş) | FLOAT | Evet | 0.0 - 1.0 |
| `model_adı` | Görsel üretimi için model seçimi (varsayılan: "kling-v3") | COMBO | Evet | `"kling-v3"` |
| `en_boy_oranı` | Üretilen görseller için en-boy oranı (varsayılan: "16:9") | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Üretilen görsel sayısı (varsayılan: 1) | INT | Evet | 1 - 9 |
| `görüntü` | İsteğe bağlı referans görseli | IMAGE | Hayır | - |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; seed'dan bağımsız olarak sonuçlar deterministik değildir (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |

**Parametre Kısıtlamaları:**

- `image` parametresi isteğe bağlıdır. Bir referans görsel sağlandığında, `image_type` parametresi referansın özne referansı mı yoksa stil referansı mı olarak kullanılacağını belirler.
- Referans görsel sağlanmadığında, referansla ilgili ayarların (`image_type`, `image_fidelity`, `human_fidelity`) sonuç üzerinde etkisi yoktur.
- `prompt` ve `negative_prompt` maksimum 500 karakter uzunluğundadır.
- `seed` parametresi isteğe bağlıdır ve deterministik sonuçları garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Girdi parametrelerine dayalı olarak üretilen görsel(ler). `n` değeri 1'den büyük olduğunda, birden fazla görsel bir yığın (batch) olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/tr.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
