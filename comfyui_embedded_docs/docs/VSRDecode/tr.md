# VSR Decode

VSR Decode, RelayVSR Conditioning düğümünden gelen anahtar kare latentlerini RelayVSR Flash kod çözücüyle yeniden tam bir videoya dönüştürür. Kod çözücü, sağladığınız düşük kaliteli karelerin bikübik yükseltmesinin üzerine kendi ayrıntısını kod çözücünün x2 veya x4 faktöründe ekler. Kare sayısı aynı kalır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | RelayVSR Flash kod çözücü; Load VAE ile yüklenir: `relayvsr_flash_vae_x2_fp32.safetensors` veya `relayvsr_flash_vae_x4_fp32.safetensors`. Dosyanın meta verisi yükseltme faktörünü belirler, bu nedenle modelle eşleşmesi gerekir. | VAE | Evet | N/A |
| `samples` | Örnekleyici tarafından döndürülen ve her anahtar kare için bir kare taşıyan latent. | LATENT | Evet | N/A |
| `images` | RelayVSR Conditioning'e verilen aynı düşük kaliteli video. | IMAGE | Evet | N/A |
| `detail` | Kod çözücünün ayrıntısının bikübik yükseltmenin üzerinde ne kadar tutulacağı: 1 tam model çıktısıdır, 0 düz yükseltmedir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Her karesi geri yüklenmiş yükseltilmiş video. | IMAGE |

## Notlar

- Aynı düşük kaliteli videoyu her iki düğüme de verin. Kod çözücü onu kare kare okur; bu nedenle uzunluk veya çözünürlükteki bir uyuşmazlık yanlış ya da bozuk bir sonuç verir.
- `detail` değerini düşürmek, geri yüklenen ayrıntıyı yumuşatır ve çıktıyı düz bir bikübik yükseltmeye daha yakın tutar; bu, çok gürültülü kaynaklarda yardımcı olabilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VSRDecode/tr.md)

---
**Source fingerprint (SHA-256):** `946ac04bc9f205fd6d1088554caaa16238086e570f212e747b166e3fb0d9b3c5`
