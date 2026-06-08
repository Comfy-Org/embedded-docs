# MiniMaxTextToVideoNode

Bir metin istemi ve isteğe bağlı parametreler kullanarak MiniMax'ın API'si aracılığıyla eşzamanlı olarak videolar oluşturur. Bu düğüm, MiniMax'ın metinden videoya hizmetine bağlanarak metin açıklamalarından video içeriği oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem_metni` | Video oluşturmayı yönlendiren metin istemi | STRING | Evet | - |
| `model` | Video oluşturma için kullanılacak model (varsayılan: "T2V-01") | COMBO | Hayır | "T2V-01"<br>"T2V-01-Director" |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0) | INT | Hayır | 0 ile 18446744073709551615 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Girdi istemine göre oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `bdbd8f9defc4c626f07b36c1ba9859155fa90a2d7ef9a491c30dac4d003d39be`
