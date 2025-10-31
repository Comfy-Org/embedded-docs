> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/tr.md)

TorchCompileModel düğümü, bir modelin performansını optimize etmek için PyTorch derlemesi uygular. Girdi modelinin bir kopyasını oluşturur ve belirtilen backend kullanılarak PyTorch'un derleme işlevselliği ile sarar. Bu, modelin çıkarım sırasındaki yürütme hızını artırabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Derlenecek ve optimize edilecek model |
| `arka_uç` | STRING | Evet | "inductor"<br>"cudagraphs" | Optimizasyon için kullanılacak PyTorch derleme backend'i |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | PyTorch derlemesi uygulanmış derlenmiş model |