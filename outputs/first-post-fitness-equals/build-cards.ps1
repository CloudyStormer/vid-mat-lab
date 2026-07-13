Add-Type -AssemblyName System.Drawing

$ErrorActionPreference = 'Stop'
$OutputDir = if ($PSScriptRoot) {
    $PSScriptRoot
} else {
    Join-Path (Get-Location) 'outputs\first-post-fitness-equals'
}

$W = 1080
$H = 1440
$fontName = 'Microsoft YaHei'

function C([string]$hex) {
    return [System.Drawing.ColorTranslator]::FromHtml($hex)
}

function New-RoundRectPath([System.Drawing.RectangleF]$rect, [float]$radius) {
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $d = $radius * 2
    $path.AddArc($rect.X, $rect.Y, $d, $d, 180, 90)
    $path.AddArc($rect.Right - $d, $rect.Y, $d, $d, 270, 90)
    $path.AddArc($rect.Right - $d, $rect.Bottom - $d, $d, $d, 0, 90)
    $path.AddArc($rect.X, $rect.Bottom - $d, $d, $d, 90, 90)
    $path.CloseFigure()
    return $path
}

function Fill-RoundRect($g, [System.Drawing.Brush]$brush, [System.Drawing.RectangleF]$rect, [float]$radius) {
    $path = New-RoundRectPath $rect $radius
    $g.FillPath($brush, $path)
    $path.Dispose()
}

function Draw-RoundRect($g, [System.Drawing.Pen]$pen, [System.Drawing.RectangleF]$rect, [float]$radius) {
    $path = New-RoundRectPath $rect $radius
    $g.DrawPath($pen, $path)
    $path.Dispose()
}

function New-TextFormat([string]$align = 'Near', [string]$lineAlign = 'Near') {
    $sf = New-Object System.Drawing.StringFormat
    $sf.Alignment = [System.Drawing.StringAlignment]::$align
    $sf.LineAlignment = [System.Drawing.StringAlignment]::$lineAlign
    $sf.Trimming = [System.Drawing.StringTrimming]::Word
    $sf.FormatFlags = [System.Drawing.StringFormatFlags]::LineLimit
    return $sf
}

function Draw-Text($g, [string]$text, [float]$size, [System.Drawing.FontStyle]$style, [System.Drawing.Color]$color, [System.Drawing.RectangleF]$rect, [string]$align = 'Near', [string]$lineAlign = 'Near') {
    $font = New-Object System.Drawing.Font($fontName, $size, $style, [System.Drawing.GraphicsUnit]::Pixel)
    $brush = New-Object System.Drawing.SolidBrush($color)
    $sf = New-TextFormat $align $lineAlign
    $g.DrawString($text, $font, $brush, $rect, $sf)
    $sf.Dispose(); $brush.Dispose(); $font.Dispose()
}

function New-BaseCanvas([bool]$dark = $false) {
    $bmp = New-Object System.Drawing.Bitmap($W, $H, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    if ($dark) {
        $rect = New-Object System.Drawing.Rectangle(0, 0, $W, $H)
        $grad = New-Object System.Drawing.Drawing2D.LinearGradientBrush($rect, (C '#0B1D3A'), (C '#174A7A'), 42)
        $g.FillRectangle($grad, $rect)
        $grad.Dispose()
    } else {
        $g.Clear((C '#F4F7FB'))
    }
    return @($bmp, $g)
}

function Draw-TopBrand($g, [int]$num, [bool]$dark = $false) {
    $ink = if ($dark) { C '#DDEBFF' } else { C '#24405F' }
    Draw-Text $g '内耗儿绝缘体' 28 ([System.Drawing.FontStyle]::Bold) $ink (New-Object System.Drawing.RectangleF(76, 58, 400, 48))
    Draw-Text $g (("{0:D2} / 07" -f $num)) 24 ([System.Drawing.FontStyle]::Regular) $ink (New-Object System.Drawing.RectangleF(820, 58, 180, 48)) 'Far'
}

function Draw-Decor($g, [System.Drawing.Color]$color, [bool]$dark = $false) {
    $alpha = if ($dark) { 35 } else { 22 }
    $b = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb($alpha, $color))
    $g.FillEllipse($b, 770, 170, 360, 360)
    $g.FillEllipse($b, -90, 1080, 300, 300)
    $b.Dispose()
}

function Save-Card($bmp, $g, [string]$name) {
    $path = Join-Path $OutputDir $name
    $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose(); $bmp.Dispose()
}

function Draw-ContentCard([int]$num, [string]$filename, [string]$formula, [string]$verdict, [string]$body, [string]$symbol, [string]$accentHex, [string]$note) {
    $pair = New-BaseCanvas $false
    $bmp = $pair[0]; $g = $pair[1]
    $accent = C $accentHex
    Draw-Decor $g $accent $false
    Draw-TopBrand $g $num $false

    Draw-Text $g $formula 48 ([System.Drawing.FontStyle]::Bold) (C '#112A46') (New-Object System.Drawing.RectangleF(76, 150, 928, 160))

    $pillBrush = New-Object System.Drawing.SolidBrush($accent)
    Fill-RoundRect $g $pillBrush (New-Object System.Drawing.RectangleF(76, 330, 640, 92)) 30
    $pillBrush.Dispose()
    Draw-Text $g $verdict 35 ([System.Drawing.FontStyle]::Bold) ([System.Drawing.Color]::White) (New-Object System.Drawing.RectangleF(105, 342, 580, 62))

    $circleBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(26, $accent))
    $g.FillEllipse($circleBrush, 340, 485, 400, 400)
    $circleBrush.Dispose()
    $circlePen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(90, $accent), 5)
    $g.DrawEllipse($circlePen, 340, 485, 400, 400)
    $circlePen.Dispose()
    Draw-Text $g $symbol 156 ([System.Drawing.FontStyle]::Bold) $accent (New-Object System.Drawing.RectangleF(340, 500, 400, 350)) 'Center' 'Center'

    $bodyBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    Fill-RoundRect $g $bodyBrush (New-Object System.Drawing.RectangleF(76, 930, 928, 300)) 34
    $bodyBrush.Dispose()
    $borderPen = New-Object System.Drawing.Pen((C '#DDE5EF'), 2)
    Draw-RoundRect $g $borderPen (New-Object System.Drawing.RectangleF(76, 930, 928, 300)) 34
    $borderPen.Dispose()
    Draw-Text $g $body 36 ([System.Drawing.FontStyle]::Regular) (C '#203852') (New-Object System.Drawing.RectangleF(120, 978, 840, 192))
    Draw-Text $g $note 25 ([System.Drawing.FontStyle]::Regular) (C '#667A90') (New-Object System.Drawing.RectangleF(120, 1175, 840, 40))

    Draw-Text $g '健身应该释放压力，而不是制造新的内耗。' 27 ([System.Drawing.FontStyle]::Bold) (C '#24405F') (New-Object System.Drawing.RectangleF(76, 1320, 928, 48)) 'Center'
    Save-Card $bmp $g $filename
}

# 01 Cover
$pair = New-BaseCanvas $true
$bmp = $pair[0]; $g = $pair[1]
Draw-Decor $g (C '#62B1FF') $true
Draw-TopBrand $g 1 $true
Draw-Text $g '健身最怕' 62 ([System.Drawing.FontStyle]::Bold) (C '#B8D9FF') (New-Object System.Drawing.RectangleF(76, 260, 900, 90))
Draw-Text $g '乱写「等号」' 104 ([System.Drawing.FontStyle]::Bold) ([System.Drawing.Color]::White) (New-Object System.Drawing.RectangleF(76, 350, 930, 160))
Draw-Text $g '这 5 个健身公式，都省略了必要条件' 37 ([System.Drawing.FontStyle]::Regular) (C '#D9E9F9') (New-Object System.Drawing.RectangleF(80, 555, 900, 70))

$eqBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(34, (C '#FFFFFF')))
Fill-RoundRect $g $eqBrush (New-Object System.Drawing.RectangleF(180, 740, 720, 280)) 54
$eqBrush.Dispose()
Draw-Text $g '有氧  ＋  力量  ＋  饮食' 44 ([System.Drawing.FontStyle]::Bold) (C '#DCEBFA') (New-Object System.Drawing.RectangleF(210, 780, 660, 70)) 'Center'
Draw-Text $g '≠' 112 ([System.Drawing.FontStyle]::Bold) (C '#6DC2FF') (New-Object System.Drawing.RectangleF(390, 855, 300, 130)) 'Center' 'Center'
Draw-Text $g '一句话决定你的身体' 36 ([System.Drawing.FontStyle]::Bold) ([System.Drawing.Color]::White) (New-Object System.Drawing.RectangleF(210, 975, 660, 60)) 'Center'

$tagBrush = New-Object System.Drawing.SolidBrush((C '#5EAFFF'))
Fill-RoundRect $g $tagBrush (New-Object System.Drawing.RectangleF(255, 1125, 570, 92)) 32
$tagBrush.Dispose()
Draw-Text $g '健身别再制造新焦虑' 36 ([System.Drawing.FontStyle]::Bold) ([System.Drawing.Color]::White) (New-Object System.Drawing.RectangleF(275, 1138, 530, 62)) 'Center'
Draw-Text $g '压力可以来，但我不吃。' 28 ([System.Drawing.FontStyle]::Regular) (C '#DCEBFA') (New-Object System.Drawing.RectangleF(76, 1320, 928, 48)) 'Center'
Save-Card $bmp $g '01-cover.png'

Draw-ContentCard 2 '02-aerobic-no-diet.png' '有氧 ＋ 不控制饮食' '≠  必然变胖' "有氧不会直接让人变胖。`n长期摄入持续大于消耗，`n体重才更可能上升。" '≠' '#E05A67' '有人运动后吃得更多，只是把消耗补回去了。'
Draw-ContentCard 3 '03-aerobic-diet.png' '有氧 ＋ 合理控制饮食' '→  更可能减重减脂' "前提是形成合理、可持续的能量缺口。`n短期体重还会受水分、糖原影响。" '→' '#2D9A72' '控制饮食，不等于挨饿。'
Draw-ContentCard 4 '04-strength-no-diet.png' '力量 ＋ 不控制饮食' '≠  自动变壮' "增肌需要训练刺激、营养、恢复和时间。`n长期吃得过多，也可能肌肉和脂肪一起增加。" '≠' '#E08A3E' '力量训练不是“一练就壮”的开关。'
Draw-ContentCard 5 '05-cortisol.png' '力量 ＋ 有氧 ＋ 控制饮食' '≠  皮质醇必然飙升' "运动后短暂升高，是正常生理反应。`n真正要注意：长期吃太少、练太多、睡太差。" '≠' '#7B66D2' '组合训练本身，不是问题。'
Draw-ContentCard 6 '06-strength-diet.png' '力量 ＋ 合理饮食' '→  更有利于降低体脂' "能量缺口合理时，力量训练有助于减脂并保留肌肉。`n体重不一定下降很快，但身体成分可能改善。" '→' '#2486C5' '别只盯体重，也要看围度和状态。'

# 07 Summary
$pair = New-BaseCanvas $false
$bmp = $pair[0]; $g = $pair[1]
Draw-Decor $g (C '#4B9CFF') $false
Draw-TopBrand $g 7 $false
Draw-Text $g '别背公式，记住 3 件事' 62 ([System.Drawing.FontStyle]::Bold) (C '#112A46') (New-Object System.Drawing.RectangleF(76, 165, 928, 110))

$items = @(
    @{n='1'; title='体重趋势'; body='看长期能量平衡'},
    @{n='2'; title='身体成分'; body='看训练、营养和恢复'},
    @{n='3'; title='能否坚持'; body='看计划是否适合自己'}
)
$y = 350
foreach($item in $items) {
    $cardBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
    Fill-RoundRect $g $cardBrush (New-Object System.Drawing.RectangleF(76, $y, 928, 205)) 34
    $cardBrush.Dispose()
    $numBrush = New-Object System.Drawing.SolidBrush((C '#4B9CFF'))
    $g.FillEllipse($numBrush, 115, $y + 47, 112, 112)
    $numBrush.Dispose()
    Draw-Text $g $item.n 48 ([System.Drawing.FontStyle]::Bold) ([System.Drawing.Color]::White) ([System.Drawing.RectangleF]::new(115, ($y + 47), 112, 112)) 'Center' 'Center'
    Draw-Text $g $item.title 35 ([System.Drawing.FontStyle]::Bold) (C '#173452') ([System.Drawing.RectangleF]::new(275, ($y + 40), 620, 55))
    Draw-Text $g $item.body 32 ([System.Drawing.FontStyle]::Regular) (C '#5C7188') ([System.Drawing.RectangleF]::new(275, ($y + 105), 620, 55))
    $y += 245
}

$endBrush = New-Object System.Drawing.SolidBrush((C '#163C65'))
Fill-RoundRect $g $endBrush (New-Object System.Drawing.RectangleF(76, 1110, 928, 190)) 38
$endBrush.Dispose()
Draw-Text $g '健身应该释放压力' 42 ([System.Drawing.FontStyle]::Bold) ([System.Drawing.Color]::White) (New-Object System.Drawing.RectangleF(110, 1150, 860, 62)) 'Center'
Draw-Text $g '而不是制造新的内耗' 36 ([System.Drawing.FontStyle]::Regular) (C '#BBD8F5') (New-Object System.Drawing.RectangleF(110, 1220, 860, 52)) 'Center'
Draw-Text $g '压力可以来，但我不吃。' 27 ([System.Drawing.FontStyle]::Bold) (C '#24405F') (New-Object System.Drawing.RectangleF(76, 1340, 928, 42)) 'Center'
Save-Card $bmp $g '07-summary.png'

# Contact sheet for QA
$files = 1..7 | ForEach-Object { Get-ChildItem $OutputDir -Filter (("{0:D2}-*.png" -f $_)) | Select-Object -First 1 }
$thumbW = 240; $thumbH = 320; $gap = 20; $cols = 4; $rows = 2
$sheetW = ($cols * $thumbW) + (($cols + 1) * $gap)
$sheetH = ($rows * $thumbH) + (($rows + 1) * $gap)
$sheet = New-Object System.Drawing.Bitmap($sheetW, $sheetH)
$sg = [System.Drawing.Graphics]::FromImage($sheet)
$sg.Clear((C '#DCE4EE'))
$sg.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
for($i = 0; $i -lt $files.Count; $i++) {
    $img = [System.Drawing.Image]::FromFile($files[$i].FullName)
    $col = $i % $cols; $row = [math]::Floor($i / $cols)
    $x = $gap + $col * ($thumbW + $gap)
    $y = $gap + $row * ($thumbH + $gap)
    $sg.DrawImage($img, $x, $y, $thumbW, $thumbH)
    $img.Dispose()
}
$sheet.Save((Join-Path $OutputDir 'contact-sheet.png'), [System.Drawing.Imaging.ImageFormat]::Png)
$sg.Dispose(); $sheet.Dispose()

Write-Output "Generated 7 cards and contact-sheet.png in $OutputDir"
