# CLIP Kaydet

The `CLIPSave` düğümü, bir CLIP metin kodlayıcı modelini SafeTensors formatında diske kaydeder. Gelişmiş model birleştirme iş akışları için tasarlanmıştır ve CLIP modelini iç yapısına göre bileşen parçalarına (CLIP-L, CLIP-G veya T5XXL gibi) otomatik olarak ayırıp her bileşeni ayrı bir dosya olarak kaydeder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Kaydedilecek CLIP modeli. | CLIP | Evet | - |
| `filename_prefix` | Kaydedilen dosya(lar) için önek yol ve dosya adı. Düğüm, benzersiz dosya adları oluşturmak için bir bileşen soneki (örn. `_clip_l`, `_clip_g`) ve bir sayaç ekler (varsayılan: `clip/ComfyUI`). | STRING | Evet | - |
| `prompt` | Çıktı dosyasında meta veri olarak kaydedilen iş akışı bilgisi. Bu parametre arayüzde gizlidir. | PROMPT | Hayır | - |
| `extra_pnginfo` | Çıktı dosyasında anahtar-değer çiftleri olarak kaydedilen ek meta veri. Bu parametre arayüzde gizlidir. | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

Bu düğümün çıkış bağlantısı yoktur. İşlenen dosyaları doğrudan `ComfyUI/output/` dizinine kaydeder.

### Kaydedilen Dosya Ayrıntıları

Düğüm, CLIP modelinin durum sözlüğünü analiz eder ve algılanan her bileşen için ayrı SafeTensors dosyaları kaydeder. Bileşen, parametre anahtarlarının ön ekiyle tanımlanır. Düğüm aşağıdaki ön ekleri sırasıyla kontrol eder:

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

Düğüm, algılanan her bileşen için `{filename}_{counter:05}_.safetensors` adında bir dosya oluşturur (örneğin, `ComfyUI_clip_l_00001_.safetensors`). Burada bileşen adı dosya adı önekine eklenir ve sayaç benzersiz dosya adlarını sağlar. Bir bileşen kaydedildiğinde, `transformer.` ön eki parametre anahtarlarından kaldırılır.

Her dosyaya yazılan meta veriler, meta veri kaydetme `--disable-metadata` komut satırı bağımsız değişkeniyle devre dışı bırakılmadığı sürece iş akışı bilgisini ve ek PNG bilgilerini içerir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/tr.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
