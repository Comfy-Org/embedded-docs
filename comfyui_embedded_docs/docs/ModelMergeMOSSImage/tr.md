# ModelMergeMOSSImage

ModelMergeMOSSImage düğümü, iki MOSS görüntü modelini eşleşen ağırlıklarını blok blok karıştırarak birleştirir; böylece sonucun bir kısmı bir temel modelden, geri kalanı ise bir ince ayardan veya ikinci bir modelden gelebilir. Mimarinin her ana bileşeninin kendi oranı vardır: video gömücü, metin gömücü, zaman gömme, paylaşılan blok modülasyonu, 42 transformer katmanının tamamı ve çıktı başları.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model. İkinci modelin katkıda bulunmadığı her şey bu modelden korunur | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model. Ağırlıkları aşağıdaki oranlara göre karıştırılır | MODEL | Evet | - |
| `video_embedder.` | Video gömücü bloğu için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `text_embedder.proj.` | Metin gömücünün projeksiyon katmanı için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `text_embedder.blocks.0.` ve `text_embedder.blocks.1.` | İki metin gömücü bloğunun her biri için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `time_embedding.` | Zaman gömme bloğu için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `shared_block_modulation.` | Transformer blokları tarafından kullanılan paylaşılan modülasyon katmanı için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `layers.0.` ile `layers.41.` arasında | 42 transformer katmanının her biri için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `final_norm_video.` | Video akışının son normalizasyonu için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `final_linear_video.` | Video akışının son doğrusal katmanı için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `video_head_modulation.` | Video çıktı başının modülasyon katmanı için karışım oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |

0.0 oranı, o bileşeni `model1`'de olduğu gibi korur; 1.0 oranı, onu tamamen `model2`'den alır; aradaki değerler ağırlıklı bir karışım üretir. Her iki girdi de aynı mimariye sahip MOSS görüntü modelleri olmalıdır; yukarıdaki öneklerden herhangi biriyle eşleşmeyen ağırlıklar `video_embedder.` oranına geri döner.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Belirtilen oranlara göre her iki girdiyi birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMOSSImage/tr.md)

---
**Source fingerprint (SHA-256):** `3b7d9c806a8d53ad00044bf30f5e63431fea7ee565414acb70a56e3059164288`
