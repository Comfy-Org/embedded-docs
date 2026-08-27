# ClipLoader

CLIPLoader düğümü, bir dosyadan metin kodlayıcı modelini (CLIP, T5 veya benzeri) yükleyerek, metin istemlerini sayısal temsillere dönüştürmesi gereken diğer düğümlerde kullanılabilir hale getirir. Her biri belirli bir kodlayıcı türü gerektiren çok çeşitli model mimarilerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_adı` | Yüklenecek metin kodlayıcı modelinin dosya adı. Bu, `ComfyUI/models/text_encoders/` dizininde bulunan bir dosya olmalıdır. | STRING | Evet | `text_encoders` klasöründe bulunan dosyaların listesi |
| `tür` | Yüklenen modelin mimari türü. Hangi spesifik kodlayıcı varyantının kullanılacağını belirler (varsayılan: `"stable_diffusion"`). | COMBO | Evet | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `cihaz` | Modelin yükleneceği aygıt. `"default"`, GPU varsa onu kullanırken, `"cpu"` CPU yüklemeyi zorunlu kılar. Bu gelişmiş bir seçenektir (varsayılan: `"default"`). | COMBO | Hayır | `"default"`<br>`"cpu"` |

### Desteklenen Tür-Kodlayıcı Eşlemeleri

`type` parametresi, belirli bir model mimarisi için doğru kodlayıcıyı seçer. Aşağıdakiler yaygın eşlemelerdir:

| Tür | Kodlayıcı |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226 token dolgulu) |
| cosmos | eski t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (önerilir) veya t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL veya Music3 Qwen/RVQ |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `clip` | Yüklenen metin kodlayıcı modeli; metin kodlama ve koşullandırma için diğer düğümlere bağlanmaya hazırdır. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipLoader/tr.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
