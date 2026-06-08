MiniMax'ın API'sini kullanarak, bir konu görseli ve metin istemine dayalı olarak eşzamanlı video oluşturur. Bu düğüm, bir konunun görselini ve bir açıklamayı alarak, isteme göre bu konuyu canlandıran veya öne çıkaran bir video oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `subject` | Video oluşturma için referans alınacak konu görseli | IMAGE | Evet | - |
| `prompt_text` | Video oluşturmayı yönlendirecek metin istemi (varsayılan: boş dize) | STRING | Evet | - |
| `model` | Video oluşturma için kullanılacak model (varsayılan: "S2V-01") | COMBO | Hayır | "S2V-01" |
| `seed` | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0) | INT | Hayır | 0 ile 18446744073709551615 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Giriş konu görseli ve isteme dayalı olarak oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
