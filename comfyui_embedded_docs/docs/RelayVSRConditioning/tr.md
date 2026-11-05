# RelayVSRConditioning

RelayVSR Conditioning, bir RelayVSR video büyütmesi için koşullandırmayı ve boş latent'i hazırlar. RelayVSR, tek adımlı Wan 2.2 modelini yalnızca klibin her 15. karesinde ve son karesinde çalıştırır; bu nedenle size verdiği latent yalnızca bu ana kareleri içerir. VSR Decode ardından aralarındaki kareleri doldurur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Load Model ile yüklenen RelayVSR difüzyon modeli: `relayvsr_x2_lightx2v_int8_convrot.safetensors` veya `relayvsr_x4_int8_convrot.safetensors`. | MODEL | Evet | N/A |
| `images` | Kendi yerel çözünürlüğündeki düşük kaliteli video. Modelin büyütme faktörü sonucun ne kadar büyük olacağını belirler. | IMAGE | Evet | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Seçilen ana kareleri düşük kaliteli kılavuz olarak taşıyan koşullandırma. | CONDITIONING |
| `latent` | Her ana kare için bir kare içeren, örnekleyiciye hazır boş latent. | LATENT |

## Kullanım

`positive` çıktısını örnekleyicinin pozitif girdisine bağlayın, ardından `latent` üzerinde CFG 1'de tek adımla örnekleme yapın: grafikte istem ve metin kodlayıcı yoktur. Örnekleyicinin çıktısını, aynı `images` girdisini ve bir RelayVSR Flash VAE'yi VSR Decode'a gönderin ve çifti eşleşmiş tutun: x2 modeli x2 kod çözücüyle, x4 modeli x4 kod çözücüyle.

Yalnızca ana kareler örneklenir; bu nedenle 150 karelik bir klip 11 karelik bir latent'e dönüşür. Örnekleyici videonun küçük bir bölümü üzerinde çalışır ve VSR Decode geri kalanı geri yükler.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RelayVSRConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `fd1a86262240430e4f2a811c2c9d8d62f0b6cdfccb26d5285e36d0d6de3b186f`
