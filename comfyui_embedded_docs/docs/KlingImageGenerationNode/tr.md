# Kling Görüntü Oluşturma

Kling Görsel Üretim Düğümü, metin istemlerinden görseller üretir ve rehberlik için referans görsel kullanma seçeneği sunar. Metin açıklamanıza ve referans ayarlarınıza göre bir veya daha fazla görsel oluşturur ve üretilen görselleri çıktı olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Pozitif metin istemi | STRING | Evet | Maksimum 500 karakter |
| `negative_prompt` | Negatif metin istemi | STRING | Evet | Maksimum 500 karakter |
| `image_type` | Görsel referans türü seçimi (gelişmiş). Referans görsel sağlandığında kullanılır. | COMBO | Evet | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Kullanıcı tarafından yüklenen görseller için referans yoğunluğu (varsayılan: 0.5, gelişmiş) | FLOAT | Evet | 0.0 - 1.0 |
| `human_fidelity` | Özne referans benzerliği (varsayılan: 0.45, gelişmiş) | FLOAT | Evet | 0.0 - 1.0 |
| `model_name` | Görsel üretimi için model seçimi (varsayılan: "kling-v3") | COMBO | Evet | `"kling-v3"`<br>`"kling-v2"` |
| `aspect_ratio` | Üretilen görseller için en-boy oranı (varsayılan: "16:9") | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Üretilen görsel sayısı (varsayılan: 1) | INT | Evet | 1 - 9 |
| `image` | İsteğe bağlı referans görsel | IMAGE | Hayır | - |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; seed ne olursa olsun sonuçlar deterministik değildir (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |

**Parametre Kısıtlamaları:**

- `image` parametresi isteğe bağlıdır. Referans görsel sağlandığında, `image_type` görselin özne referansı mı yoksa stil referansı mı olarak kullanılacağını belirler. Referans görsel sağlanmadığında `image_type` uygulanmaz.
- `prompt` en az 1 karakter ve en fazla 500 karakter içermelidir. `negative_prompt` boş olabilir ancak 500 karakterle sınırlıdır.
- `seed` parametresi isteğe bağlıdır ve deterministik sonuçları garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Girdi parametrelerine göre üretilen görsel(ler). Birden fazla görsel istendiğinde, tüm görseller tek bir grup halinde döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/tr.md)

---
**Source fingerprint (SHA-256):** `165d18244870b5b4f34587633a5492e733ad0b0a923bb8c3e506319460321906`
