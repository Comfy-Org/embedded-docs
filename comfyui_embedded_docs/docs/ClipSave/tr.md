# ClipSave

`CLIPSave` düğümü, bir CLIP metin kodlayıcı modelini SafeTensors formatında diske kaydeder. Gelişmiş model birleştirme iş akışları için tasarlanmıştır ve CLIP modelini, modelin iç yapısına göre bileşen parçalarına (CLIP-L, CLIP-G veya T5XXL gibi) otomatik olarak ayırır ve her bileşeni ayrı bir dosya olarak kaydeder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Kaydedilecek CLIP modeli. | CLIP | Evet | - |
| `dosyaadı_öneki` | Kaydedilen dosyalar için önek yolu ve dosya adı. Düğüm, benzersiz dosya adları oluşturmak için bir bileşen son eki (örn. `_clip_l`, `_clip_g`) ve bir sayaç ekler (varsayılan: `clip/ComfyUI`). | STRING | Evet | - |
| `prompt` | İş akışı prompt bilgisi; çıktı dosyasına meta veri olarak kaydedilir. Bu parametre kullanıcı arayüzünde gizlidir. | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek meta veri; çıktı dosyasına anahtar-değer çiftleri olarak kaydedilir. Bu parametre kullanıcı arayüzünde gizlidir. | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

Bu düğümün çıktı bağlantısı yoktur. İşlenen dosyaları doğrudan `ComfyUI/output/` dizinine kaydeder. Kaydedilen dosyalar, ComfyUI `--disable-metadata` bağımsız değişkeniyle başlatılmadığı sürece meta veri içerir (format "pt" olarak ayarlanır, ayrıca iş akışı promptu ve varsa ek PNG bilgileri de meta veriye dahil edilir).

### Kaydedilen Dosya Ayrıntıları

Düğüm, CLIP modelinin durum sözlüğünü (state dictionary) analiz eder ve algılanan her bileşen için ayrı SafeTensors dosyaları kaydeder. Bileşen, parametre anahtarlarının önekine göre tanımlanır. Aşağıdaki önekler kontrol edilir:

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
- Boş önek (diğer CLIP bileşenleri)

Algılanan her bileşen için düğüm, `{filename_prefix}_{counter:05}_.safetensors` adında bir dosya oluşturur; bileşen öneki dosya adı önekine eklenir (örn. `clip/ComfyUI_clip_l_00001_.safetensors`). Kaydetme sırasında `transformer.` öneki parametre anahtarlarından kaldırılır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipSave/tr.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
