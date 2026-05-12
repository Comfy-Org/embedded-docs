> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/tr.md)

## Genel Bakış

VOIDQuadmaskPreprocess düğümü, bir maskeyi VOID iç boyama (inpainting) işlemi için özel dört seviyeli "dörtlü maskeye" (quadmask) dönüştürerek hazırlar. Giriş maskesini alır, isteğe bağlı olarak ana bölgeyi genişletir (dilate), ardından maske değerlerini farklı anlamsal bölgeleri (ana nesne, örtüşme, etkilenen alan ve arka plan) temsil eden dört ayrı seviyeye niceleme (quantize) işlemi yapar. Son olarak, çıkış değerleri [0, 1] aralığında olacak şekilde maskeyi ters çevirir ve normalleştirir; burada 1.0 kaldırılacak alanı, 0.0 ise korunacak alanı belirtir.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `mask` | MASK | Evet | Yok | Ön işleme tabi tutulacak giriş maskesi. |
| `dilate_width` | INT | Hayır | 0 ila 50 (adım: 1) | Ana maske bölgesi için genişletme yarıçapı. 0 değeri genişletme uygulanmayacağı anlamına gelir. (varsayılan: 0) |

## Çıktılar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `quadmask` | MASK | Değerleri [0, 1] aralığında olan, dört ayrı seviyeyi temsil eden ön işlenmiş dörtlü maske: 1.0 (kaldırılacak ana nesne), ~0.75 (ana nesne ve etkilenen alanın örtüşmesi), ~0.50 (etkilenen bölge) ve 0.0 (korunacak arka plan). |