# [getissuu][1] - An ISSUU Downloader

getissuu is a [Python][2] script that downloads a document from [ISSUU][3]
and converts it to a high quality PDF file.

## Prerequisites

* [cURL][4]
* [ImageMagick][5]
* [SWFTools][6]

## Usage

```
usage: getissuu.py [-h] [--curl PATH] [--swfrender PATH] [--convert PATH]
                   [--document-name NAME] [--document-id ID] [--dpi DPI]
                   [--output OUTPUT]

Downloads a document from issuu.com and converts it to a high quality PDF file

optional arguments:
  -h, --help            show this help message and exit
  --curl PATH           path to curl (default: /usr/bin/curl)
  --swfrender PATH      path to swfrender (default: /usr/bin/swfrender)
  --convert PATH        path to convert (default: /usr/bin/convert)
  --document-name NAME  name of the document
  --document-id ID      issuu.com document id
  --dpi DPI             output DPI (default: 300)
  --output OUTPUT       output path (default: current directory)
```

[1]: https://github.com/scoobadog/getissuu "getissuu"
[2]: https://www.python.org/ "Python.org"
[3]: http://issuu.com/ "ISSUU"
[4]: http://curl.haxx.se/ "cURL"
[5]: http://www.imagemagick.org/ "ImageMagick"
[6]: http://www.swftools.org/ "SWFTools"
