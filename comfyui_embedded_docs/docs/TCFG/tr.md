> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/tr.md)

TCFG (Teğetsel Sönümleme CFG), örnekleme sürecinde koşulsuz (negatif) tahminleri, koşullu (pozitif) tahminlerle daha iyi uyumlu hale getirecek şekilde iyileştirir. Bu teknik, 2503.18137 numaralı araştırma makalesine dayanarak, koşulsuz yönlendirmeye teğetsel sönümleme uygulayarak çıktı kalitesini artırır. Düğüm, sınıflandırıcısız yönlendirme sırasında koşulsuz tahminlerin nasıl işlendiğini ayarlayarak modelin örnekleme davranışını değiştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Teğetsel sönümleme CFG'nin uygulanacağı model |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Teğetsel sönümleme CFG uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `de6b4deb8a42f05dff90e393bff1e0b4b8ed58887586ca81c236e1a780be5776`
