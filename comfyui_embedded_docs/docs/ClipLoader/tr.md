CLIPLoader düğümü, bir dosyadan metin kodlayıcı modelini (CLIP, T5 veya benzeri) yükleyerek, metin istemlerini sayısal temsillere dönüştürmesi gereken diğer düğümlerde kullanıma sunar. Her biri belirli bir kodlayıcı türü gerektiren çok çeşitli model mimarilerini destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip_adı` | Yüklenecek metin kodlayıcı modelinin dosya adı. Bu dosya, `ComfyUI/models/text_encoders/` veya `ComfyUI/models/clip/` dizininde bulunmalıdır. | STRING | Evet | `text_encoders` klasöründe bulunan dosyaların listesi |
| `tür` | Yüklenen modelin mimari türü. Bu, hangi belirli kodlayıcı varyantının kullanılacağını belirler. Varsayılan değer `"stable_diffusion"` şeklindedir. | STRING | Evet | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"` |
| `cihaz` | Modelin yükleneceği aygıt. `"default"`, varsa GPU'yu kullanırken, `"cpu"` CPU'ya yüklemeyi zorunlu kılar. Bu gelişmiş bir seçenektir (varsayılan: `"default"`). | STRING | Hayır | `"default"`<br>`"cpu"` |

### Desteklenen Tür-Kodlayıcı Eşleştirmeleri

`type` parametresi, belirli bir model mimarisi için doğru kodlayıcıyı seçer. Aşağıda yaygın eşleştirmeler yer almaktadır:

| Tür | Kodlayıcı |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226-token dolgulu) |
| cosmos | eski t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (önerilen) veya t5 |
| omnigen2 | qwen vl 2.5 3B |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip` | Metin kodlama ve koşullandırma için diğer düğümlere bağlanmaya hazır, yüklenmiş metin kodlayıcı modeli. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/tr.md)

---
**Source fingerprint (SHA-256):** `1051bfe5570dff81719682cb09938bae4c03e94e0e72f7a2be84867cccb48017`
