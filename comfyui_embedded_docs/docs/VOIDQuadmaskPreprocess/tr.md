> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/tr.md)

## Genel Bakış

VOIDQuadmaskPreprocess düğümü, bir maskeyi özel dört seviyeli "dörtlü maskeye" dönüştürerek VOID iç boyama (inpainting) için hazırlar. Giriş maskesini alır, isteğe bağlı olarak ana bölgeyi genişletir, ardından maske değerlerini farklı anlamsal bölgeleri (ana nesne, örtüşme, etkilenen alan ve arka plan) temsil eden dört ayrı seviyeye niceleme işlemi uygular. Son olarak, çıktı değerleri [0, 1] aralığında olacak şekilde maskeyi ters çevirir ve normalleştirir; burada 1.0 kaldırılacak alanı, 0.0 ise korunacak alanı belirtir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `mask` | MASK | Evet | Yok | Ön işleme tabi tutulacak giriş maskesi. |
| `dilate_width` | INT | Hayır | 0 ila 50 (adım: 1) | Ana maske bölgesi için genişletme yarıçapı. 0 değeri genişletme uygulanmayacağı anlamına gelir. (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `quadmask` | MASK | Değerleri [0, 1] aralığında olan, dört ayrı seviyeyi temsil eden ön işlenmiş dörtlü maske: 1.0 (kaldırılacak ana nesne), ~0.75 (ana ve etkilenen alan örtüşmesi), ~0.50 (etkilenen bölge) ve 0.0 (korunacak arka plan). |

---
**Source fingerprint (SHA-256):** `12dc5ab215b80d81289942457ce2ddffcb9ec41fc738a53ca5fbf1e9181ed439`
