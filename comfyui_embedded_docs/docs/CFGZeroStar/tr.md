> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/tr.md)

CFGZeroStar düğümü, difüzyon modellerine özel bir yönlendirme ölçekleme tekniği uygular. Koşullu ve koşulsuz tahminler arasındaki farka dayalı olarak optimize edilmiş bir ölçek faktörü hesaplayarak sınıflandırıcısız yönlendirme sürecini değiştirir. Bu yaklaşım, model kararlılığını korurken üretim süreci üzerinde gelişmiş kontrol sağlamak için nihai çıktıyı ayarlar.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|------------|--------|----------|
| `model` | MODEL | zorunlu | - | - | CFGZeroStar yönlendirme ölçekleme tekniği ile değiştirilecek difüzyon modeli |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `patched_model` | MODEL | CFGZeroStar yönlendirme ölçekleme uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `1f5fcd1377c64609e28d85e453aaaa0bcc8f3ac322b7b7240f34f71aa113562a`
