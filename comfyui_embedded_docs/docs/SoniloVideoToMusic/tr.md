Sonilo'nun yapay zeka modelini kullanarak videodan müzik üretir. Bu düğüm, girdi videosunun içeriğini analiz eder ve ona uygun bir müzik parçası oluşturur. Videoyu işlemek ve sesi üretmek için harici bir yapay zeka hizmeti kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Müzik oluşturulacak girdi videosu. Maksimum süre: 6 dakika. | VIDEO | Evet | - |
| `prompt` | Müzik oluşturmayı yönlendirmek için isteğe bağlı metin istemi. En iyi kalite için boş bırakın; model video içeriğini tam olarak analiz edecektir. (varsayılan: boş dize) | STRING | Hayır | - |
| `seed` | Tekrarlanabilirlik için tohum değeri. Şu anda Sonilo hizmeti tarafından yok sayılır ancak grafik tutarlılığı için korunur. (varsayılan: 0) | INT | Hayır | 0 ile 18446744073709551615 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Oluşturulan müziğin ses dosyası. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/tr.md)

---
**Source fingerprint (SHA-256):** `542fff1d8db8e48156bf9d1ff4690c91a7d71676332eef4708a6d36686abb31e`
