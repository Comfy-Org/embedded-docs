> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/tr.md)

`CLIPTextEncodeFlux`, ComfyUI'da Flux mimarisi için özel olarak tasarlanmış gelişmiş bir metin kodlama düğümüdür. Hem yapılandırılmış anahtar kelimeleri hem de ayrıntılı doğal dil açıklamalarını işlemek için çift kodlayıcı mekanizması (CLIP-L ve T5XXL) kullanır ve Flux modeline daha doğru ve kapsamlı metin anlama yeteneği sağlayarak metinden görüntü oluşturma kalitesini artırır.

Bu düğüm, bir çift kodlayıcı işbirliği mekanizmasına dayanır:

1. `clip_l` girişi, CLIP-L kodlayıcısı tarafından işlenerek stil, tema ve diğer anahtar kelime özelliklerini çıkarır—kısa açıklamalar için idealdir.
2. `t5xxl` girişi, karmaşık ve ayrıntılı doğal dil sahne açıklamalarını anlamada başarılı olan T5XXL kodlayıcısı tarafından işlenir.
3. Her iki kodlayıcının çıktıları birleştirilir ve `guidance` parametresiyle birleştirilerek, aşağı akıştaki Flux örnekleyici düğümleri için birleşik koşullandırma gömüleri (`CONDITIONING`) oluşturulur; bu, oluşturulan içeriğin metin açıklamasına ne kadar yakın olduğunu kontrol eder.

## Girişler

| Parametre | Veri Türü | Giriş Yöntemi | Varsayılan | Aralık | Açıklama |
|-----------|----------|-------------|---------|-------|-------------|
| `clip`    | CLIP     | Düğüm girişi  | Yok    | -     | Hem CLIP-L hem de T5XXL kodlayıcılarını içeren, Flux mimarisini destekleyen bir CLIP modeli olmalıdır |
| `clip_l`  | STRING   | Metin kutusu    | Yok    | En fazla 77 token | Kısa anahtar kelime açıklamaları için uygundur, stil veya tema gibi |
| `t5xxl`   | STRING   | Metin kutusu    | Yok    | Neredeyse sınırsız | Ayrıntılı doğal dil açıklamaları için uygundur, karmaşık sahneleri ve detayları ifade eder |
| `guidance`| FLOAT    | Sürgü      | 3.5     | 0.0 - 100.0 | Metin koşullarının oluşturma süreci üzerindeki etkisini kontrol eder; daha yüksek değerler metne daha sıkı bağlılık anlamına gelir |

## Çıkışlar

| Çıkış Adı   | Veri Türü    | Açıklama |
|--------------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Her iki kodlayıcıdan birleştirilmiş gömüleri ve guidance parametresini içerir, koşullu görüntü oluşturma için kullanılır |

## Kullanım Örnekleri

### Prompt Örnekleri

- **clip_l girişi** (anahtar kelime stili):
  - Yapılandırılmış, kısa anahtar kelime kombinasyonları kullanın
  - Örnek: `şaheser, en iyi kalite, portre, yağlı boya tablo, dramatik aydınlatma`
  - Stil, kalite ve ana konuya odaklanın

- **t5xxl girişi** (doğal dil açıklaması):
  - Tam, akıcı sahne açıklamaları kullanın
  - Örnek: `Yağlı boya tablo stilinde, derin gölgeler ve parlak vurgular oluşturan dramatik chiaroscuro aydınlatmasına sahip, rönesans tarzı kompozisyonla konunun özelliklerini vurgulayan oldukça detaylı bir portre.`
  - Sahne detayları, mekansal ilişkiler ve aydınlatma efektlerine odaklanın

### Notlar

1. Flux mimarisiyle uyumlu bir CLIP modeli kullandığınızdan emin olun
2. Çift kodlayıcı avantajından yararlanmak için hem `clip_l` hem de `t5xxl` alanlarını doldurmanız önerilir
3. `clip_l` için 77 token sınırını unutmayın
4. `guidance` parametresini oluşturulan sonuçlara göre ayarlayın