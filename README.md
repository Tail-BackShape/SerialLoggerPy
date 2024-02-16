# SerialLoggerPy

Arduinoのシリアルプリントを簡易的に保存するやつ

To log Serial print and save text file for Arduino.


## Install

```bash
pip install serial
```

↑でエラーが出るときは以下のようにしてみるとうまくいくことがある。

If an error occurs in the above, the following may work.

```bash
pip uninstall serial
pip uninstall pyserial
pip install pyserial
```

## Update Schedule
- 更新予定(更新日時)
- タイムスタンプの追加
- 使えるCOMポートの一覧を最初に表示する
- ボーレートを指定できるようにする
- Serial.write的な機能を実装する<br><br>

- Update schedule (date and time of update)
- Add timestamp
- Display the list of available COM ports first
- Enable to specify baud rate
- Implement Serial.write-like functionality
