# Analysis Notes

## object 9
JavaScript action:
`this.exportDataObject({ cName: "template", nLaunch: 0 });`

Bu kod embedded dosyanın dışarı çıkarılması için kullanılır.

## object 10
Launch action:
- `cmd.exe` çağrılıyor
- kullanıcı dizinleri kontrol ediliyor
- `template.pdf` açılmaya çalışılıyor

Bu davranış, PDF içinde command execution mantığını göstermektedir.

## Extracted Payload
Çıkarılan payload bir PE32+ executable olarak tanımlanmıştır. Bu, PDF içerisinde Windows çalıştırılabilir dosya gömülü olduğunu göstermektedir.
