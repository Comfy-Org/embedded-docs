> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/tr.md)

Runway İlk-Son Kare'den Video'ya düğümü, ilk ve son ana kareleri bir metin istemiyle birlikte yükleyerek videolar oluşturur. Runway'in Gen-3 modelini kullanarak sağlanan başlangıç ve bitiş kareleri arasında yumuşak geçişler oluşturur. Bu, bitiş karesinin başlangıç karesinden önemli ölçüde farklı olduğu karmaşık geçişler için özellikle kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `prompt` | STRING | Evet | Yok | Oluşturma için metin istemi (varsayılan: boş dize) |
| `başlangıç_karesi` | IMAGE | Evet | Yok | Video için kullanılacak başlangıç karesi |
| `bitiş_karesi` | IMAGE | Evet | Yok | Video için kullanılacak bitiş karesi. Yalnızca gen3a_turbo için desteklenir. |
| `süre` | COMBO | Evet | `"5"`<br>`"10"` | Video süresi saniye cinsinden (varsayılan: "5") |
| `oran` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulan video için en boy oranı (varsayılan: "16:9") |
| `tohum` | INT | Hayır | 0 ile 4294967295 arası | Oluşturma için rastgele tohum değeri. Rastgele tohum için 0 olarak ayarlayın (varsayılan: 0). |

**Parametre Kısıtlamaları:**

- `prompt` en az 1 karakter içermelidir
- Hem `start_frame` hem de `end_frame` maksimum 7999x7999 piksel boyutlarında olmalıdır
- Hem `start_frame` hem de `end_frame` 0,5 ile 2,0 arasında en boy oranlarına sahip olmalıdır
- `end_frame` parametresi yalnızca gen3a_turbo modeli kullanılırken desteklenir

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Başlangıç ve bitiş kareleri arasında geçiş yapan oluşturulan video |

---
**Source fingerprint (SHA-256):** `57b72c1143b7053272107403279e1f84919cbfe71c57ca4f4e21b4324f7a5346`
