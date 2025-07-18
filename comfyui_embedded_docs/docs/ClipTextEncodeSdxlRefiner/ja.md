このノードは、SDXL Refinerモデル専用に設計されており、テキストプロンプトを条件付け情報に変換する際に、美的スコアと寸法情報を組み込んで生成タスクの条件を向上させ、最終的な精製効果を改善します。プロのアートディレクターのように機能し、創造的な意図を伝えるだけでなく、正確な美的基準と仕様要件を作品に注入します。

## SDXL Refinerについて

SDXL Refinerは、SDXLベースモデルに基づいて画像の詳細と品質の向上に特化した精製モデルです。このプロセスは、アートレタッチャーを持つようなものです：

1. まず、ベースモデルによって生成された予備的な画像やテキストの説明を受け取ります
2. 次に、正確な美的スコアリングと寸法パラメータを通じて精製プロセスを導きます
3. 最後に、高周波画像の詳細処理に焦点を当てて全体的な品質を向上させます

Refinerは2つの方法で使用できます：

- ベースモデルによって生成された画像のポスト処理用の独立した精製ステップとして
- 生成の低ノイズフェーズ中に処理を引き継ぐエキスパート統合システムの一部として

## 入力

| パラメータ名 | データ型 | 入力タイプ | デフォルト値 | 値の範囲 | 説明 |
|------------|---------|------------|-------------|----------|------|
| `クリップ` | CLIP | Required | - | - | テキストのトークン化とエンコーディングに使用されるCLIPモデルインスタンス。テキストをモデルが理解できる形式に変換するための中核コンポーネント |
| `ascore` | FLOAT | Optional | 6.0 | 0.0-1000.0 | 生成される画像の視覚的品質と美的要素を制御します。アートワークの品質基準を設定するのに似ています：<br/>- 高スコア(7.5-8.5)：より洗練された、詳細な効果を追求<br/>- 中スコア(6.0-7.0)：バランスの取れた品質管理<br/>- 低スコア(2.0-3.0)：ネガティブプロンプトに適している |
| `幅` | INT | Required | 1024 | 64-16384 | 出力画像の幅（ピクセル）を指定します。8の倍数である必要があります。SDXLは総ピクセル数が1024×1024（約1Mピクセル）に近い場合に最適に機能します |
| `高さ` | INT | Required | 1024 | 64-16384 | 出力画像の高さ（ピクセル）を指定します。8の倍数である必要があります。SDXLは総ピクセル数が1024×1024（約1Mピクセル）に近い場合に最適に機能します |
| `text` | STRING | Required | - | - | テキストプロンプトの説明。複数行入力とダイナミックプロンプト構文をサポートします。Refinerでは、テキストプロンプトは望ましい視覚的品質と詳細の特徴の記述により重点を置くべきです |

## 出力

| 出力名 | データ型 | 説明 |
|--------|---------|------|
| `条件付け` | CONDITIONING | テキストのセマンティクス、美的基準、寸法情報の統合エンコーディングを含む精製された条件付け出力。SDXL Refinerモデルによる正確な画像精製を導くために特別に設計されています |

## 注意事項

1. このノードはSDXL Refinerモデル用に特別に最適化されており、通常のCLIPTextEncodeノードとは異なります
2. 美的スコア7.5がベースラインとして推奨されます。これはSDXLトレーニングで使用される標準設定です
3. すべての寸法パラメータは8の倍数である必要があり、総ピクセル数は1024×1024（約1Mピクセル）に近いことが推奨されます
4. Refinerモデルは画像の詳細と品質の向上に焦点を当てているため、テキストプロンプトはシーンの内容よりも望ましい視覚効果の記述に重点を置くべきです
5. 実際の使用では、Refinerは生成の後半段階（最後の約20%のステップ）で使用され、詳細の最適化に焦点を当てます
