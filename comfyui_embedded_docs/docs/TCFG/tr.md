> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/tr.md)

TCFG (Teğetsel Sönümleme CFG), koşulsuz (negatif) tahminleri, koşullu (pozitif) tahminlerle daha iyi uyum sağlaması için iyileştiren bir kılavuzlama tekniği uygular. Bu yöntem, 2503.18137 referans numaralı araştırma makalesine dayanarak, koşulsuz kılavuzluğa teğetsel sönümleme uygulayarak çıktı kalitesini artırır. Düğüm, sınıflandırıcısız kılavuzlama süreci boyunca koşulsuz tahminlerin nasıl işlendiğini ayarlayarak modelin örnekleme davranışını değiştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Teğetsel sönümleme CFG'nin uygulanacağı model |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Teğetsel sönümleme CFG uygulanmış, değiştirilmiş model |