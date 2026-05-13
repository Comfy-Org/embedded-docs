> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/tr.md)

SetUnionControlNetType düğümü, koşullandırma için kullanılacak kontrol ağının türünü belirlemenizi sağlar. Mevcut bir kontrol ağını alır ve seçiminize göre kontrol türünü ayarlayarak, belirtilen tür yapılandırmasına sahip değiştirilmiş bir kopyasını oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `kontrol_ağı` | CONTROL_NET | Evet | - | Yeni bir tür ayarıyla değiştirilecek kontrol ağı |
| `tür` | STRING | Evet | `"auto"`<br>Mevcut tüm UNION_CONTROLNET_TYPES anahtarları | Uygulanacak kontrol ağı türü. Otomatik tür algılama için "auto" kullanın veya mevcut seçenekler arasından belirli bir kontrol ağı türü seçin |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `kontrol_ağı` | CONTROL_NET | Belirtilen tür ayarı uygulanmış değiştirilmiş kontrol ağı |

---
**Source fingerprint (SHA-256):** `a64308aec96784f08b6f3f8e96e85f532bd1c536301739e7252b2c7978921b5a`
