> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/tr.md)

TorchCompileModel düğümü, bir modelin performansını optimize etmek için PyTorch derlemesi uygular. Giriş modelinin bir kopyasını oluşturur ve belirtilen arka ucu kullanarak PyTorch'un derleme işlevselliğiyle sarar. Bu, çıkarım sırasında modelin yürütme hızını artırabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Derlenecek ve optimize edilecek model |
| `backend` | STRING | Evet | "inductor"<br>"cudagraphs" | Optimizasyon için kullanılacak PyTorch derleme arka ucu (varsayılan: "inductor") |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | PyTorch derlemesi uygulanmış derlenmiş model |

---
**Source fingerprint (SHA-256):** `923e71b528e6e53468916f74c2a02924bf51738f29e36638312c6da6357fcedb`
