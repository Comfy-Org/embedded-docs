> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/tr.md)

## Genel Bakış

Bir dosyadan MoGe (Monoküler Geometri) modelini yükler ve geometri tahmini görevlerinde kullanıma hazır hale getirir. Bu düğüm, `geometry_estimation` klasöründen bir model dosyasını okur ve MoGe modelini eğitilmiş ağırlıklarıyla başlatır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | Evet | `geometry_estimation` klasöründeki mevcut model dosyalarının listesi | Yüklenecek MoGe model dosyasının adı. ComfyUI kurulumunuzdaki mevcut model dosyaları arasından seçim yapın. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MOGE_MODEL` | MOGE_MODEL | Yüklenmiş MoGe model örneği, geometri tahmini iş akışlarında kullanıma hazırdır. |

---
**Source fingerprint (SHA-256):** `4707002565181ca17936ecf87ea8059630c97c44c17facfecd04053d9581b7d1`
