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
- タイムスタンプの追加(2024/2/17)
- 使えるCOMポートの一覧を最初に表示する(2024/2/18)
- ボーレートを指定できるようにする(2024/2/19)
- Serial.write的な機能を実装する
- タイムスタンプをミリ秒までとれるようにする<br><br>

- Update schedule (date and time of update)
- Add timestamp(2024/2/17-JST)
- Display the list of available COM ports first(2024/2/18-JST)
- Enable to specify baud rate(2024/2/19)
- Implement Serial.write-like functionality
- Time stamp to milliseconds
