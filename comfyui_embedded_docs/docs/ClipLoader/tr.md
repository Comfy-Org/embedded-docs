# ClipLoader

CLIPLoader düğümü, bir metin kodlayıcı modelini (CLIP, T5 veya benzeri) bir dosyadan yükler ve metin istemlerini sayısal gösterimlere dönüştürmesi gereken diğer düğümlerde kullanılabilir hale getirir. Çok çeşitli model mimarilerini destekler ve her biri belirli bir kodlayıcı türü gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `clip_adı` | Yüklenecek metin kodlayıcı modelinin dosya adı. Bu, `ComfyUI/models/text_encoders/` dizininde bulunan bir dosya olmalıdır. | STRING | Evet | `text_encoders` klasöründe bulunan dosyaların listesi |
| `tür` | Yüklenen modelin mimari türü. Kullanılacak belirli kodlayıcı varyantını belirler (varsayılan: `"stable_diffusion"`). | COMBO | Evet | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"` |
| `cihaz` | Modelin yükleneceği aygıt. `"default"` varsa GPU'yu kullanır, `"cpu"` ise CPU'da yüklemeye zorlar. Bu gelişmiş bir seçenektir (varsayılan: `"default"`). | COMBO | Hayır | `"default"`<br>`"cpu"` |

### Desteklenen Tür-Kodlayıcı Eşlemeleri

`type` parametresi, belirli bir model mimarisi için doğru kodlayıcıyı seçer. Aşağıdakiler yaygın eşlemelerdir:

| Tür | Kodlayıcı |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226 token dolgusu) |
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
| `CLIP` | Yüklenen metin kodlayıcı modeli; metin kodlama ve koşullandırma için diğer düğümlere bağlanmaya hazırdır. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipLoader/tr.md)

---
**Source fingerprint (SHA-256):** `6df608d500520d9414acd82d9fd509b1e211a8385202cefd5579e8a8f397bc64`
