SaveAudio düğümü, ses verilerini FLAC formatında bir dosyaya kaydeder. Ses girişini alır ve belirtilen çıktı dizinine verilen dosya adı önekiyle yazar. Düğüm, dosya adlandırmayı otomatik olarak yönetir ve sesin daha sonra kullanılmak üzere doğru şekilde kaydedilmesini sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Kaydedilecek ses verisi | AUDIO | Evet | - |
| `dosyaadı_öneki` | Çıktı dosya adı için önek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |

*Not: `prompt` ve `extra_pnginfo` parametreleri gizlidir ve sistem tarafından otomatik olarak yönetilir.*

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *Yok* | Bu düğüm herhangi bir çıktı verisi döndürmez, ancak ses dosyasını çıktı dizinine kaydeder | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/tr.md)

---
**Source fingerprint (SHA-256):** `16242dfc45d0f2808a5615e9c1bfe4de4d19e2f5f6b28370f631439021dc72e5`
