> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/tr.md)

ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

## Genel Bakış

Bu düğüm, bir nesnenin veya karakterin 2 ila 4 referans görüntüsünden 3B bir model oluşturur. Farklı açılardan (ön, sol, arka, sağ) görüntüler sağlarsınız ve düğüm, GLB formatında bir 3B ağ oluşturur. Ön görünüm gereklidir ve daha iyi sonuçlar için isteğe bağlı olarak diğer üç görünümün herhangi bir kombinasyonunu ekleyebilirsiniz.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Ön görünüm (0°). Gereklidir. |
| `image_left` | IMAGE | Hayır | - | Sol görünüm (90°), yani nesnenin sol tarafı. |
| `image_back` | IMAGE | Hayır | - | Arka görünüm (180°). |
| `image_right` | IMAGE | Hayır | - | Sağ görünüm (270°), yani nesnenin sağ tarafı. |
| `output_mode` | COMBO | Evet | `"geometry"`<br>`"textured"`<br>`"detailed"` | Oluşturulan model için çıktı modu. `"geometry"` ham bir ağ üretir, `"textured"` standart bir doku ekler ve `"detailed"` yüksek detaylı dokulu bir model oluşturur (varsayılan: `"textured"`). |
| `face_limit` | INT | Hayır | -1 ila 100000 | Çıktı ağı için maksimum yüz sayısı. Sınırsız için -1 olarak ayarlayın (varsayılan: -1). |
| `model_seed` | INT | Hayır | 0 ila 2147483647 | Tekrarlanabilir model oluşturma için tohum değeri. Rastgele için 0 olarak ayarlayın (varsayılan: 0). |
| `auto_size` | BOOLEAN | Hayır | True / False | Modeli standart bir sınırlama kutusuna sığacak şekilde otomatik olarak boyutlandırın (varsayılan: False). |
| `export_uv` | BOOLEAN | Hayır | True / False | Modelle birlikte UV koordinatlarını dışa aktarın (varsayılan: True). |
| `compress_geometry` | BOOLEAN | Hayır | True / False | Dosya boyutunu azaltmak için geometri verilerini sıkıştırın (varsayılan: False). |

**Not:** En az 2 görüntü sağlamalısınız: ön görünüm (`image`) artı diğer görünümlerden en az biri (`image_left`, `image_back` veya `image_right`). 2'den az görüntü sağlanırsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan GLB modelinin dosya adı (yalnızca geriye dönük uyumluluk için). |
| `model_task_id` | MODEL_TASK_ID | Bu model oluşturma isteği için benzersiz görev kimliği. |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3B model. |

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
