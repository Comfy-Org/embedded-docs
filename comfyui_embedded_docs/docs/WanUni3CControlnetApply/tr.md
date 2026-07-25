# Wan Uni3C ControlNet Uygula

## Genel Bakış

Bu düğüm, bir Wan video difüzyon modeline Uni3C ControlNet uygular. Bunu yaparken, oluşturulmuş bir yönlendirme videosu (örneğin, bükülmüş nokta bulutu görüntüleri) kullanarak modelin çıktısını etkiler. Belirli blok katmanlarında kontrol sinyalleri enjekte ederek video üretimi sırasında kamera yörüngesi tabanlı yönlendirme sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Düzeltilecek Wan difüzyon modeli. | MODEL | Evet | – |
| `model_patch` | Bir Uni3C ControlNet düzeltmesi (`comfy.ldm.wan.uni3c.WanUni3CControlnet` örneği olmalıdır). | MODEL_PATCH | Evet | – |
| `vae` | Yönlendirme videosunu gizli değişkenlere kodlamak için kullanılan VAE. | VAE | Evet | – |
| `video_render` | Kamera yörüngesinden oluşturulan yönlendirme videosu, çoğunlukla giriş görüntüsünün bükülmüş nokta bulutu görüntüleridir. | IMAGE | Evet | – |
| `güç` | Uygulanan kontrol sinyalinin gücü. | FLOAT | Evet | -10.0 ile 10.0 (varsayılan: 1.0) |
| `başlangıç_yüzdesi` | Kontrolün başladığı gürültü giderme işleminin yüzdesi. | FLOAT | Evet | 0.0 ile 1.0 (varsayılan: 0.0) |
| `bitiş_yüzdesi` | Kontrolün bittiği gürültü giderme işleminin yüzdesi. | FLOAT | Evet | 0.0 ile 1.0 (varsayılan: 1.0) |

**Notlar:**
- `model_patch` bir Uni3C ControlNet olmalıdır; aksi takdirde düğüm hata verir.
- ControlNet'in iç boyutu, Wan modelinin boyutuyla eşleşmelidir; farklı olmaları durumunda hata verilir.
- `render_video` giriş görüntüsünün RGB formatında olması beklenir (yalnızca ilk 3 kanal kullanılır).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `MODEL` | Uni3C ControlNet uygulanmış düzeltilmiş Wan modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanUni3CControlnetApply/tr.md)

---
**Source fingerprint (SHA-256):** `f69253f06aba9208778f713ad36e9995f53a15d2e61243b853b9ac9131637371`
