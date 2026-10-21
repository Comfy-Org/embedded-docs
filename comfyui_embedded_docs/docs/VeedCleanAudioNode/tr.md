# VEED Clean Audio

VEED ile konuşmadaki arka plan gürültüsünü kaldırın. Her dildeki konuşma için tasarlanmıştır: sesin altındaki gürültü temizlenir, duraklamalar tamamen temizlenir ve müzik ile ses efektleri korunmak yerine kaldırılır. Çıktı, 48 kHz mono sestir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `audio` | Konuşma kaydı, 30 dakikadan kısa. | AUDIO | Evet | 1799 saniyeye kadar |
| `strength` | Konuşmanın altındaki gürültünün ne kadarının kaldırılacağı. Daha düşük değerler sesin arkasında daha fazla ortam tonu bırakır; kelimeler arasındaki duraklamalar her zaman tamamen temizlenir ve varsayılanın üzerindeki değerler çok az fark yaratır. (varsayılan: 0.874) | FLOAT | Evet | 0.0 ile 1.0 arası (adım 0.001) |
| `loudness` | Çıktı ses yüksekliğinin normalleştirilip normalleştirilmeyeceği. `"normalize"` çıktıyı `target_lufs` değerine ayarlar; `"keep input level"` ses düzeyini olduğu gibi bırakır. Bir seçenek seçildiğinde ilgili parametreler görünür. (varsayılan: `"normalize"`) | DYNAMIC_COMBO | Evet | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Çıktının LUFS cinsinden bütünleşik ses yüksekliği. Tepe değerler -1.1 dBTP ile sınırlandırılır, bu nedenle yüksek hedefler erken durur (tipik konuşma için yaklaşık -15 LUFS). `loudness` değeri `"normalize"` olduğunda kullanılabilir (varsayılan: -19.0). | FLOAT | Evet | -40.0 ile -8.0 arası (adım 0.1) |

Kayıt 1799 saniyeden uzun olduğunda düğüm bir hatayla durur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `AUDIO` | Temizlenmiş konuşma, 48 kHz mono ses olarak. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanAudioNode/tr.md)

---
**Source fingerprint (SHA-256):** `c85949385109a5d320e52619e9df17c245b19f8f16cc1a0b69a37ae2e7bb5b6d`
