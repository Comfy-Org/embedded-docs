> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/tr.md)

SaveLatent düğümü, gizli tensörleri dosya olarak diske kaydederek daha sonra kullanım veya paylaşım için saklar. Gizli örnekleri alır ve isteğe bağlı olarak bilgi istemi bilgilerini içeren meta verilerle birlikte çıktı dizinine kaydeder. Düğüm, gizli veri yapısını korurken dosya adlandırma ve düzenlemeyi otomatik olarak halleder.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `örnekler` | LATENT | Evet | - | Diske kaydedilecek gizli örnekler |
| `dosyaadı_öneki` | STRING | Hayır | - | Çıktı dosya adı için ön ek (varsayılan: "latents/ComfyUI") |
| `prompt` | PROMPT | Hayır | - | Meta verilere dahil edilecek bilgi istemi bilgisi (gizli parametre) |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Meta verilere dahil edilecek ek PNG bilgisi (gizli parametre) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `ui` | UI | Kaydedilen gizli dosyanın ComfyUI arayüzünde dosya konumu bilgisini sağlar |

---
**Source fingerprint (SHA-256):** `dc7fd101c8dd93e2bcc39de64e0c39abe8e056c9e5932587fc6ce80e2fd143e8`
