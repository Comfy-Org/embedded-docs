# FishAudioVoiceSelector

Fish Audio Voice Selector ノードは、テキスト読み上げ生成のために Fish Audio ライブラリから音声を選択します。内蔵のプリセット音声から1つを選ぶか、「custom」を選択して fish.audio の任意の音声モデルIDを入力できます。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `voice` | 音声を選択するか、「custom」を選択すると fish.audio の音声モデルIDを入力できます。 | DYNAMIC_COMBO | はい | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

プリセット音声オプションは、英語（en）、中国語（zh）、日本語（ja）の音声をカバーしており、追加の入力は必要ありません。

### カスタム入力

これらの入力は、`voice` が「custom」に設定されている場合に表示されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | fish.audio の音声モデルID。例: https://fish.audio/m/<id>/ 内のID。デフォルト: 空文字列。 | STRING | はい | 有効な Fish Audio 音声モデルID |

注：`voice` が「custom」に設定されている場合、`voice_id` は空白をトリムした後に空であってはなりません。空の場合は、ノードは「Custom voice ID is empty.」エラーを発生させます。認識できない音声オプションが渡された場合、ノードは「Unknown voice」エラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `voice` | 選択された Fish Audio 音声モデルID。プリセット音声の場合、Fish Audio ライブラリ内の対応する音声IDが返されます。「custom」の場合は、入力された `voice_id` の値が返されます。 | FISHAUDIO_VOICE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/ja.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
