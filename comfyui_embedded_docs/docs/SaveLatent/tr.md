> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/tr.md)

SaveLatent düğümü, gizli tensörleri daha sonra kullanılmak veya paylaşılmak üzere dosya olarak diske kaydeder. Gizli örnekleri alır ve isteğe bağlı meta veriler (prompt bilgisi dahil) ile birlikte çıktı dizinine kaydeder. Düğüm, gizli veri yapısını korurken dosya adlandırma ve organizasyonunu otomatik olarak halleder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `örnekler` | LATENT | Evet | - | Diske kaydedilecek gizli örnekler |
| `dosyaadı_öneki` | STRING | Hayır | - | Çıktı dosya adı için önek (varsayılan: "latents/ComfyUI") |
| `prompt` | PROMPT | Hayır | - | Meta verilere dahil edilecek prompt bilgisi (gizli parametre) |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Meta verilere dahil edilecek ek PNG bilgisi (gizli parametre) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ui` | UI | ComfyUI arayüzünde kaydedilen gizli dosya için konum bilgisi sağlar |