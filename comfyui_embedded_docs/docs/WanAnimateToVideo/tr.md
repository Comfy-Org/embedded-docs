> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/tr.md)

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

WanAnimateToVideo düğümü, poz referansları, yüz ifadeleri ve arka plan öğeleri dahil olmak üzere birden fazla koşullandırma girdisini birleştirerek video içeriği oluşturur. Kareler arasında zamansal tutarlılığı korurken tutarlı animasyon dizileri oluşturmak için çeşitli video girdilerini işler. Düğüm, gizli uzay işlemlerini gerçekleştirir ve hareket modellerini devam ettirerek mevcut videoları genişletebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | İstenen içeriğe doğru yönlendirme için pozitif koşullandırma |
| `negatif` | CONDITIONING | Evet | - | İstenmeyen içerikten uzaklaştırma için negatif koşullandırma |
| `vae` | VAE | Evet | - | Görüntü verilerini kodlamak ve çözmek için kullanılan VAE modeli |
| `genişlik` | INT | Evet | 16 ile MAX_RESOLUTION arası | Çıktı video genişliği piksel cinsinden (varsayılan: 832, adım: 16) |
| `yükseklik` | INT | Evet | 16 ile MAX_RESOLUTION arası | Çıktı video yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) |
| `uzunluk` | INT | Evet | 1 ile MAX_RESOLUTION arası | Oluşturulacak kare sayısı (varsayılan: 77, adım: 4) |
| `toplu_iş_boyutu` | INT | Evet | 1 ile 4096 arası | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `clip_vision_çıkışı` | CLIP_VISION_OUTPUT | Hayır | - | Ek koşullandırma için isteğe bağlı CLIP görüş modeli çıktısı |
| `referans_görsel` | IMAGE | Hayır | - | Oluşturma için başlangıç noktası olarak kullanılan referans görüntü |
| `yüz_videosu` | IMAGE | Hayır | - | Yüz ifadesi yönlendirmesi sağlayan video girdisi |
| `poz_videosu` | IMAGE | Hayır | - | Poz ve hareket yönlendirmesi sağlayan video girdisi |
| `devam_eden_hareket_maksimum_kare_sayısı` | INT | Evet | 1 ile MAX_RESOLUTION arası | Önceki hareketten devam ettirilecek maksimum kare sayısı (varsayılan: 5, adım: 4) |
| `arka_plan_videosu` | IMAGE | Hayır | - | Oluşturulan içerikle birleştirilecek arka plan videosu |
| `karakter_maskesi` | MASK | Hayır | - | Seçici işleme için karakter bölgelerini tanımlayan maske |
| `devam_eden_hareket` | IMAGE | Hayır | - | Zamansal tutarlılık için devam ettirilecek önceki hareket dizisi |
| `video_kare_konumu` | INT | Evet | 0 ile MAX_RESOLUTION arası | Tüm giriş videolarında aranacak kare miktarı. Bir videoyu parça parça oluşturmak için kullanılır. Bir videoyu uzatmak için önceki düğümün video_frame_offset çıktısına bağlayın. (varsayılan: 0, adım: 1) |

**Parametre Kısıtlamaları:**

- `pose_video` sağlandığında, `trim_to_pose_video` mantığı etkinse (kaynak kodda şu anda `False` olarak ayarlıdır) çıktı uzunluğu poz videosu süresine göre ayarlanacaktır
- `face_video`, işlendiğinde otomatik olarak 512x512 çözünürlüğe yeniden boyutlandırılır ve -1,0 ile 1,0 aralığına normalleştirilir
- `continue_motion` kareleri, `continue_motion_max_frames` parametresiyle sınırlıdır; girdiden yalnızca son `continue_motion_max_frames` karesi kullanılır
- Giriş videoları (`face_video`, `pose_video`, `background_video`, `character_mask`), işlemeden önce `video_frame_offset` kadar kaydırılır; kaydırma video uzunluğunu aşarsa girdi yok sayılır
- `character_mask` yalnızca bir kare içeriyorsa, tüm kareler boyunca tekrarlanır
- `clip_vision_output` sağlandığında, hem pozitif hem de negatif koşullandırmaya uygulanır
- `reference_image` sağlanmazsa, varsayılan referans olarak siyah bir görüntü (tümü sıfır) kullanılır
- `continue_motion` sağlanmazsa, başlangıç kareleri gri (0,5 yoğunluk) gürültüyle doldurulur

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | CLIP görüş çıktısı, poz videosu gizli katmanı, yüz videosu pikselleri, birleştirilmiş gizli görüntü ve birleştirilmiş maske dahil olmak üzere ek video bağlamıyla değiştirilmiş pozitif koşullandırma |
| `gizli_uzay` | CONDITIONING | CLIP görüş çıktısı, poz videosu gizli katmanı, yüz videosu pikselleri (ters çevrilmiş), birleştirilmiş gizli görüntü ve birleştirilmiş maske dahil olmak üzere ek video bağlamıyla değiştirilmiş negatif koşullandırma |
| `kırpılmış_gizli_uzay` | LATENT | [batch_size, 16, latent_length + trim_latent, latent_height, latent_width] şeklinde gizli uzay formatında oluşturulan video içeriği |
| `kırpılmış_görsel` | INT | Baştan kırpılacak gizli kare sayısını gösteren gizli uzay kırpma bilgisi (referans görüntü gizli karelerine karşılık gelir) |
| `video_kare_konumu` | INT | Referans hareket kareleri için görüntü uzayı kırpma bilgisi, baştan kırpılacak görüntü karelerinin sayısını gösterir |
| `video_kare_konumu` | INT | Parçalar halinde video oluşturmaya devam etmek için güncellenmiş kare kaydırması, önceki kaydırma artı oluşturulan uzunluk olarak hesaplanır |

---
**Source fingerprint (SHA-256):** `c2ca90f4963f629d51cdd7f4bdb67e01c32ce5ca7d916b1f992ccd220f57566c`
