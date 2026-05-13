> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/tr.md)

`CLIPSave` düğümü, bir CLIP metin kodlayıcı modelini SafeTensors formatında diske kaydeder. Gelişmiş model birleştirme iş akışları için tasarlanmıştır ve CLIP modelini, modelin iç yapısına bağlı olarak otomatik olarak bileşen parçalarına (CLIP-L, CLIP-G veya T5XXL gibi) ayırır ve her bileşeni ayrı bir dosya olarak kaydeder.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Zorunlu | - | - | Kaydedilecek CLIP modeli. |
| `filename_prefix` | STRING | Zorunlu | `clip/ComfyUI` | - | Kaydedilen dosya(lar) için ön ek yolu ve dosya adı. Düğüm, benzersiz dosya adları oluşturmak için bir bileşen son eki (ör. `_clip_l`, `_clip_g`) ve bir sayaç ekleyecektir. |
| `prompt` | PROMPT | Gizli | - | - | Çıktı dosyasında meta veri olarak kaydedilen iş akışı istem bilgisi. |
| `extra_pnginfo` | EXTRA_PNGINFO | Gizli | - | - | Çıktı dosyasında anahtar-değer çiftleri olarak kaydedilen ek meta veriler. |

## Çıktılar

Bu düğümün herhangi bir çıktı bağlantısı yoktur. İşlenen dosyaları doğrudan `ComfyUI/output/` dizinine kaydeder.

### Kaydedilen Dosya Ayrıntıları

Düğüm, CLIP modelinin durum sözlüğünü analiz eder ve algılanan her bileşen için ayrı SafeTensors dosyaları kaydeder. Bileşen, parametre anahtarlarının ön ekiyle tanımlanır. Aşağıdaki ön ekler kontrol edilir:

- `clip_l.` (CLIP-L metin kodlayıcı)
- `clip_g.` (CLIP-G metin kodlayıcı)
- `clip_h.` (CLIP-H metin kodlayıcı)
- `t5xxl.` (T5-XXL metin kodlayıcı)
- `pile_t5xl.` (Pile-T5-XL metin kodlayıcı)
- `mt5xl.` (mT5-XL metin kodlayıcı)
- `umt5xxl.` (UMT5-XXL metin kodlayıcı)
- `t5base.` (T5-Base metin kodlayıcı)
- `gemma2_2b.` (Gemma 2 2B metin kodlayıcı)
- `llama.` (LLaMA metin kodlayıcı)
- `hydit_clip.` (Hydit CLIP metin kodlayıcı)
- Boş ön ek (diğer CLIP bileşenleri)

Algılanan her bileşen için düğüm, `{filename_prefix}_{counter:05}_.safetensors` adında bir dosya oluşturur; burada bileşen ön eki, dosya adı ön ekine eklenir (ör. `clip/ComfyUI_clip_l_00001_.safetensors`). Kaydetme sırasında `transformer.` ön eki parametre anahtarlarından kaldırılır.

---
**Source fingerprint (SHA-256):** `039b39cbfb9b04ccebc5fc885ebe75dfde14838530d38133d0a3a6311e392059`
