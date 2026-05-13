> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/tr.md)

PrimitiveFloat düğümü, iş akışınızda kullanılabilecek bir kayan noktalı sayı değeri oluşturur. Tek bir sayısal girdi alır ve aynı değeri çıktı olarak verir; böylece ComfyUI hattınızdaki farklı düğümler arasında float değerleri tanımlamanıza ve iletmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `value` | FLOAT | Evet | -sys.maxsize ile sys.maxsize (adım: 0.1) | Çıktı olarak verilecek kayan noktalı sayı değeri (varsayılan: 0.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | FLOAT | Girdi olarak alınan kayan noktalı sayı değeri |

---
**Source fingerprint (SHA-256):** `a12473ac0efac903249f249770bec92a562b1ef6dede45fc0296e0e397a0754f`
