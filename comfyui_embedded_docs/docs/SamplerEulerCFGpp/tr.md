> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/tr.md)

SamplerEulerCFGpp düğümü, çıktı üretmek için bir Euler CFG++ örnekleme yöntemi sağlar. Bu düğüm, Euler CFG++ örnekleyicisinin kullanıcı tercihine göre seçilebilen iki farklı uygulama sürümünü sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `version` | STRING | Evet | `"regular"`<br>`"alternative"` | Kullanılacak Euler CFG++ örnekleyicisinin uygulama sürümü (varsayılan: "regular") |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Yapılandırılmış bir Euler CFG++ örnekleyici örneği döndürür |

---
**Source fingerprint (SHA-256):** `f01732fc39a76fca697aaddefc8cec58d54ba9761eb8d93da806ddd162d42513`
