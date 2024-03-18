// SerialLoggerPyの動作テスト用プログラム
// シリアル割り込みで受信したデータをそのまま送信する
// 割り込み確認のためにカウンターをインクリメントして送信する

void setup()
{
  Serial.begin(9600);
  while (!Serial)
  {
    delay(10);
  }
  Serial.println("SerialLoggerPy test program started");
}

void loop()
{
  static int counter = 0;
  Serial.print("counter = ");
  Serial.println(counter);
  counter++;
  delay(1000);
}

void serialEvent()
{
  if (Serial.available() > 0)
  {
    // シリアルデータの受信 (改行まで)
    String data = Serial.readStringUntil('\n');

    // 受信したデータをそのまま送信
    Serial.print("Send:");
    Serial.println(data);
  }
}
