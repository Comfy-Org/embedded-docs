# BileşimControlNetTürüAyarla

SetUnionControlNetType düğümü, koşullandırma için kullanılacak kontrol ağının türünü belirlemenizi sağlar. Mevcut bir kontrol ağını alır ve seçiminize göre kontrol türünü ayarlayarak, belirtilen tür yapılandırmasına sahip değiştirilmiş bir kopyasını oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `kontrol_ağı` | Yeni bir tür ayarıyla değiştirilecek kontrol ağı | CONTROL_NET | Evet | - |
| `tür` | Uygulanacak kontrol ağı türü. Otomatik tür algılama için "auto" kullanın veya mevcut seçenekler arasından belirli bir kontrol ağı türü seçin | STRING | Evet | `"auto"`<br>Mevcut tüm UNION_CONTROLNET_TYPES anahtarları |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `kontrol_ağı` | Belirtilen tür ayarı uygulanmış değiştirilmiş kontrol ağı | CONTROL_NET |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/tr.md)

---
**Source fingerprint (SHA-256):** `a64308aec96784f08b6f3f8e96e85f532bd1c536301739e7252b2c7978921b5a`
