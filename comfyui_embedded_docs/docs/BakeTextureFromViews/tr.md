# Bake Texture From Views

Render edilmiş görüntüleri mesh'in UV düzenine geri yansıtır. Mesh'i Render Mesh ile render edin, görüntüleri düzenleyin veya yeniden oluşturun, ardından aynı mesh ve kameralarla bunları bake edin. Hiçbir görünümün kapsamadığı texel'ler, mesh'in kendi dokusunu veya köşe renklerini korur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `mesh` | Render edilen, UV'si açılmış mesh. | MESH | Evet | - |
| `images` | Kamera başına bir görüntü, kamera sırasına göre (Batch Images). Render'ın en-boy oranına sahip herhangi bir çözünürlük; daha yüksek olması daha keskin bir bake verir. | IMAGE | Evet | - |
| `camera_info` | Görüntülerin render edildiği kameralar; Render Mesh'e bağlandığı şekilde. Rig'leri Batch Cameras ile birleştirin. Yok: Render Mesh'in otomatik çerçevelenmiş ön görünümü. | LOAD3D_CAMERA | Hayır | - |
| `resolution` | Kare doku çözünürlüğü. 0, mesh'in mevcut doku boyutunu korur; doku yoksa 2048 olur; aksi halde mevcut doku bu değere yeniden örneklenir. Varsayılan: 0. | INT | Hayır | 0 ile 8192 arası (adım: 64) |
| `blend_exponent` | Görünümler cos(görüş açısı)^üs ile ağırlıklandırılır. Daha yüksek değer en doğrudan görünümü tercih eder (daha keskin, daha sert dikişler); daha düşük değer daha fazla görünümün ortalamasını alır (daha yumuşak). Varsayılan: 4.0. | FLOAT | Hayır | 0.0 ile 32.0 arası (adım: 0.5) |
| `fill_unseen` | Hiçbir görünümün görmediği texel'ler, mesh'in kendi dokusu veya köşe renkleri yerine görülen yüzeyden genişletilen renk alır. Görünümler tüm dokuyu değiştirdiğinde bunu kullanın. Varsayılan: false. | BOOLEAN | Hayır | true<br>false |
| `mask` | Görünüm başına düzenlenen alanlar; yalnızca maskelenmiş pikseller yansıtılır. Tek bir maske her görünüme uygulanır. | MASK | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `base_color` | Bake edilmiş doku; Apply Texture to Mesh için. | IMAGE |
| `confidence` | Texel başına, en iyi görünümün onu ne kadar doğrudan gördüğü; 0 görülmedi anlamına gelir. | MASK |

Not: Görüntüleyici model dönüşümüyle yapılan render'lar bake ile hizalanmaz ve bir batch'in yalnızca ilk mesh'i kullanılır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromViews/tr.md)

---
**Source fingerprint (SHA-256):** `e5f2456977693dc09e69ce4d846f2ab775f2520115623d9f63a76807d6c9f797`
