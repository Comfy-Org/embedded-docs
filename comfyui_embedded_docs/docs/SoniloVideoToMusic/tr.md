> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/tr.md)

Sonilo'nun yapay zeka modelini kullanarak videodan müzik üretir. Bu düğüm, girdi videosunun içeriğini analiz eder ve ona uygun bir müzik parçası oluşturur. Videoyu işlemek ve sesi üretmek için harici bir yapay zeka hizmeti kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `video` | VIDEO | Evet | - | Müzik oluşturulacak girdi videosu. Maksimum süre: 6 dakika. |
| `prompt` | STRING | Hayır | - | Müzik oluşturmayı yönlendirmek için isteğe bağlı metin istemi. En iyi kalite için boş bırakın; model video içeriğini tam olarak analiz edecektir. (varsayılan: boş dize) |
| `seed` | INT | Hayır | 0 ile 18446744073709551615 arası | Tekrarlanabilirlik için tohum değeri. Şu anda Sonilo hizmeti tarafından yok sayılır ancak grafik tutarlılığı için korunur. (varsayılan: 0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `audio` | AUDIO | Oluşturulan müziğin ses dosyası. |

---
**Source fingerprint (SHA-256):** `542fff1d8db8e48156bf9d1ff4690c91a7d71676332eef4708a6d36686abb31e`
