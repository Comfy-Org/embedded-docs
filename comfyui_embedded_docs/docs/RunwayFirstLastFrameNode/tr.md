# Runway İlk-Son-Kare'den Videoya

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Üretim için metin istemi (varsayılan: boş dize) | STRING | Evet | N/A |
| `start_frame` | Video için kullanılacak başlangıç karesi | IMAGE | Evet | N/A |
| `end_frame` | Video için kullanılacak bitiş karesi. Yalnızca gen3a_turbo için desteklenir. | IMAGE | Evet | N/A |
| `duration` | Video süresi (saniye) (varsayılan: "5") | COMBO | Evet | `"5"`<br>`"10"` |
| `ratio` | Oluşturulan video için en-boy oranı (varsayılan: "768:1280") | COMBO | Evet | `"768:1280"`<br>`"1280:768"` |
| `seed` | Üretim için rastgele tohum. Rastgele tohum için 0 olarak ayarlayın (varsayılan: 0). | INT | Hayır | 0 to 4294967295 |

**Parametre Kısıtlamaları:**

- `prompt` en az 1 karakter içermelidir
- Hem `start_frame` hem de `end_frame` maksimum 7999x7999 piksel boyutlarına sahip olmalıdır
- Hem `start_frame` hem de `end_frame` 0.5 ile 2.0 arasında en-boy oranına sahip olmalıdır
- `end_frame` parametresi yalnızca gen3a_turbo modeli kullanıldığında desteklenir

**Not:** Bu düğüm artık kullanımdan kaldırılmıştır. Kullanmadan önce Runway'in Gen-3'te anahtar karelerle oluşturma konusundaki en iyi uygulamalarını inceleyin: https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-----------|----------|-----------|
| `output` | Oluşturulan ve başlangıç ile bitiş kareleri arasında geçiş yapan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
