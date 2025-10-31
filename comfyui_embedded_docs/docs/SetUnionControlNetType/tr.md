> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/tr.md)

SetUnionControlNetType düğümü, koşullandırma için kullanılacak kontrol ağı türünü belirtmenize olanak tanır. Mevcut bir kontrol ağını alır ve seçiminize dayalı olarak kontrol türünü ayarlar, böylece belirtilen tür yapılandırmasına sahip değiştirilmiş bir kontrol ağı kopyası oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `kontrol_ağı` | CONTROL_NET | Evet | - | Yeni bir tür ayarıyla değiştirilecek kontrol ağı |
| `tür` | STRING | Evet | `"auto"`<br>Tüm mevcut UNION_CONTROLNET_TYPES anahtarları | Uygulanacak kontrol ağı türü. Otomatik tür algılama için "auto" kullanın veya mevcut seçeneklerden belirli bir kontrol ağı türü seçin |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `kontrol_ağı` | CONTROL_NET | Belirtilen tür ayarı uygulanmış değiştirilmiş kontrol ağı |