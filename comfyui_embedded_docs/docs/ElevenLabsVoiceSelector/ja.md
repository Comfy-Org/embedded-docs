> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/ja.md)

ElevenLabs Voice Selector ノードは、事前に定義された ElevenLabs テキスト読み上げ音声のリストから特定の音声を選択することができます。音声名を入力として受け取り、音声生成に必要な対応する音声識別子を出力します。このノードは、他の ElevenLabs オーディオノードで使用する互換性のある音声を選択するプロセスを簡素化します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `voice` | STRING | はい | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | 事前定義された ElevenLabs 音声から選択します。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `voice` | STRING | 選択された ElevenLabs 音声の一意の識別子です。この識別子は、テキスト読み上げ生成を行う他のノードに渡すことができます。 |