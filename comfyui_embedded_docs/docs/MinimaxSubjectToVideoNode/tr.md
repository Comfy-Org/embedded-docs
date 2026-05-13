> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/tr.md)

MiniMax'ın API'sini kullanarak, bir konu görseli ve metin istemine dayalı olarak eşzamanlı video oluşturur. Bu düğüm, bir konunun görselini ve bir açıklamayı alarak, isteme göre bu konuyu canlandıran veya öne çıkaran bir video oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `subject` | IMAGE | Evet | - | Video oluşturma için referans alınacak konu görseli |
| `prompt_text` | STRING | Evet | - | Video oluşturmayı yönlendirecek metin istemi (varsayılan: boş dize) |
| `model` | COMBO | Hayır | "S2V-01" | Video oluşturma için kullanılacak model (varsayılan: "S2V-01") |
| `seed` | INT | Hayır | 0 ile 18446744073709551615 arası | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Giriş konu görseli ve isteme dayalı olarak oluşturulan video |

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
